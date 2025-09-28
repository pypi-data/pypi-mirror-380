import logging
import mimetypes
import pathlib
import sys

import ckan.lib.datapreview as datapreview
from ckan.lib.plugins import DefaultPermissionLabels
import ckan.lib.signals
from ckan import authz, config, common, logic, model
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

import dclab
from dcor_shared import DC_MIME_TYPES, s3cc


from . import actions
from . import auth as dcor_auth
from .cli import get_commands
from . import jobs
from . import helpers as dcor_helpers
from . import resource_schema_supplements as rss
from . import signals
from . import validate as dcor_validate


logger = logging.getLogger(__name__)

# Used for disabling `after_resource_create` in background jobs
IS_BACKGROUND_JOB = bool(" ".join(sys.argv).count("jobs worker"))

#: ignored schema fields (see default_create_package_schema in
#: https://github.com/ckan/ckan/blob/master/ckan/logic/schema.py)
REMOVE_PACKAGE_FIELDS = [
    "author",
    "author_email",
    "maintainer",
    "maintainer_email",
    "url",
    "version",
]


# Monkey-patch away the `manage_group` permission for group members.
# We need this to prevent simple group members (non-editors and non-admins)
# from adding or removing datasets to a group.
if "manage_group" in authz.ROLE_PERMISSIONS["member"]:
    authz.ROLE_PERMISSIONS["member"].remove("manage_group")


class DCORDatasetFormPlugin(plugins.SingletonPlugin,
                            toolkit.DefaultDatasetForm,
                            DefaultPermissionLabels):
    """This plugin makes views of DC data"""
    plugins.implements(plugins.IActions, inherit=True)
    plugins.implements(plugins.IAuthFunctions, inherit=True)
    plugins.implements(plugins.IClick, inherit=True)
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.IConfigDeclaration, inherit=True)
    plugins.implements(plugins.IDatasetForm, inherit=True)
    plugins.implements(plugins.IPermissionLabels, inherit=True)
    plugins.implements(plugins.IResourceController, inherit=True)
    plugins.implements(plugins.IPackageController, inherit=True)
    plugins.implements(plugins.ISignal, inherit=True)
    plugins.implements(plugins.ITemplateHelpers, inherit=True)
    plugins.implements(plugins.IValidators, inherit=True)

    # IActions
    def get_actions(self):
        return {
            "resource_upload_s3_urls":
                actions.get_resource_upload_s3_urls,
            "resource_schema_supplements":
                actions.get_resource_schema_supplements,
            "supported_resource_suffixes":
                actions.get_supported_resource_suffixes,
        }

    # IAuthFunctions
    def get_auth_functions(self):
        # - `*_patch` has same authorization as `*_update`
        # - If you are wondering why group_create and organization_create
        #   are not here, it's because authz.py always checks whether
        #   anonymous access is allowed via the auth_allow_anonymous_access
        #   flag. So we just leave it at the defaults.
        return {
            'bulk_update_delete': dcor_auth.deny,
            'bulk_update_private': dcor_auth.deny,
            'dataset_purge': dcor_auth.dataset_purge,
            'group_list': dcor_auth.group_list,
            'group_show': dcor_auth.content_listing,
            'member_create': dcor_auth.member_create,
            'member_roles_list': dcor_auth.content_listing,
            'organization_list': dcor_auth.content_listing,
            'package_create': dcor_auth.package_create,
            'package_delete': dcor_auth.package_delete,
            'package_update': dcor_auth.package_update,
            'resource_create': dcor_auth.resource_create,
            'resource_delete': dcor_auth.deny,
            'resource_update': dcor_auth.resource_update,
            'resource_upload_s3_urls':  dcor_auth.resource_upload_s3_urls,
            'tag_list': dcor_auth.content_listing,
            'tag_show': dcor_auth.content_listing,
            'user_autocomplete': dcor_auth.user_autocomplete,
            'user_create': dcor_auth.user_create,
            'user_list': dcor_auth.user_list,
            'user_show': dcor_auth.user_show,
            'vocabulary_show': dcor_auth.content_listing,
        }

    # IClick
    def get_commands(self):
        return get_commands()

    # IConfigurer
    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_resource('assets', 'dcor_schemas')
        # Add DC mime types
        for key in DC_MIME_TYPES:
            mimetypes.add_type(key, DC_MIME_TYPES[key])
        # Set licenses path if no licenses_group_url was given
        if not (common.config.get("licenses_group_url") or "").strip():
            logger.error("`licenses_group_url` is not set. Consider "
                         "running `dcor inspect`.")

    def update_config_schema(self, schema):
        ignore_missing = toolkit.get_validator('ignore_missing')
        if not (common.config.get("licenses_group_url") or "").strip():
            # Only update the schema if no licenses_group_url was given
            schema.update({
                # This is an existing CKAN core configuration option, we are
                # just making it available to be editable at runtime
                'licenses_group_url': [ignore_missing],
            })
        return schema

    # IConfigDeclaration
    def declare_config_options(
            self,
            declaration: config.declaration.Declaration,
            key: config.declaration.Key):

        schema_group = key.ckanext.dcor_schemas

        declaration.declare_bool(
            schema_group.allow_content_listing_for_anon, True).set_description(
            "allow anonymous users to list all circles, groups, tags"
        )

        declaration.declare_bool(
            schema_group.allow_public_datasets, True).set_description(
            "allow users to create publicly-accessible datasets"
        )

        declaration.declare(
            schema_group.json_resource_schema_dir, "package").set_description(
            "directory containing .json files that define the supplementary "
            "resource schema"
        )

        declaration.declare_bool(
            schema_group.notify_user_create, True).set_description(
            "notify the maintainer when a new user is created"
        )

        dcor_group = key.dcor_object_store

        declaration.declare(
            dcor_group.endpoint_url).set_description(
            "S3 storage endpoint URL"
        )

        declaration.declare(
            dcor_group.bucket_name).set_description(
            "S3 storage bucket name schema"
        )

        declaration.declare(
            dcor_group.access_key_id).set_description(
            "S3 storage access key ID"
        )

        declaration.declare(
            dcor_group.secret_access_key).set_description(
            "S3 storage secret access key"
        )

        declaration.declare_bool(
            dcor_group.ssl_verify, True).set_description(
            "S3 storage verify SSL connection (disable for testing)"
        )

    # IDatasetForm
    def _modify_package_schema(self, schema):
        # remove default fields
        for key in REMOVE_PACKAGE_FIELDS:
            if key in schema:
                schema.pop(key)
        schema.pop("state")
        schema.update({
            'authors': [
                toolkit.get_validator('unicode_safe'),
                toolkit.get_validator('dcor_schemas_dataset_authors'),
                toolkit.get_validator('not_empty'),
                toolkit.get_converter('convert_to_extras'),
            ],
            'doi': [
                toolkit.get_validator('ignore_missing'),
                toolkit.get_validator('dcor_schemas_dataset_doi'),
                toolkit.get_validator('unicode_safe'),
                toolkit.get_converter('convert_to_extras'),
            ],
            'id': [
                toolkit.get_validator('ignore_missing'),
                toolkit.get_validator('package_id_not_changed'),
                toolkit.get_validator('unicode_safe'),
                toolkit.get_validator('dcor_schemas_dataset_id'),
            ],
            'license_id': [
                toolkit.get_validator('dcor_schemas_dataset_license_id'),
            ],
            'references': [
                toolkit.get_validator('ignore_missing'),
                toolkit.get_validator('dcor_schemas_dataset_references'),
                toolkit.get_validator('unicode_safe'),
                toolkit.get_converter('convert_to_extras'),
            ],
            'state': [
                toolkit.get_validator('ignore_missing'),
                toolkit.get_validator('dcor_schemas_dataset_state'),
            ],
        })
        schema['resources'].update({
            # ETag given by S3 backend
            'etag': [
                toolkit.get_validator('ignore_missing'),
            ],
            'id': [
                toolkit.get_validator('ignore_missing'),
                toolkit.get_validator('unicode_safe'),
                toolkit.get_validator('dcor_schemas_resource_id'),
            ],
            'name': [
                toolkit.get_validator('ignore_missing'),
                toolkit.get_validator('unicode_safe'),
                toolkit.get_validator('dcor_schemas_resource_name'),
            ],
            'sha256': [
                toolkit.get_validator('ignore_missing'),
            ],
            # Whether the resource is available in an S3-compatible object
            # store.
            's3_available': [
                toolkit.get_validator('ignore_missing'),
                toolkit.get_validator('boolean_validator'),
            ],
            # The URL to the resource in the object store. This only makes
            # sense for public datasets. For private datasets, the URL to the
            # resource must be obtained via the API.
            's3_url': [
                toolkit.get_validator('ignore_missing'),
                toolkit.get_validator('url_validator'),
            ],
        })
        # Add dclab configuration parameters
        for sec in dclab.dfn.CFG_METADATA:
            for key in dclab.dfn.config_keys[sec]:
                schema['resources'].update({
                    'dc:{}:{}'.format(sec, key): [
                        toolkit.get_validator('ignore_missing'),
                        toolkit.get_validator(
                            'dcor_schemas_resource_dc_config'),
                    ]})
        # Add supplementary resource schemas
        for composite_key in rss.get_composite_item_list():
            schema['resources'].update({
                composite_key: [
                    toolkit.get_validator('ignore_missing'),
                    toolkit.get_validator(
                        'dcor_schemas_resource_dc_supplement'),
                ]})

        return schema

    def create_package_schema(self):
        schema = super(DCORDatasetFormPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        schema.update({
            'name': [
                toolkit.get_validator('unicode_safe'),
                toolkit.get_validator('dcor_schemas_dataset_name_create'),
            ],
        })

        return schema

    def update_package_schema(self):
        schema = super(DCORDatasetFormPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(DCORDatasetFormPlugin, self).show_package_schema()
        # remove default fields
        for key in REMOVE_PACKAGE_FIELDS:
            if key in schema:
                schema.pop(key)
        schema.update({
            'authors': [
                toolkit.get_converter('convert_from_extras'),
                toolkit.get_validator('ignore_missing'),
                toolkit.get_validator('unicode_safe'),
            ],
            'doi': [
                toolkit.get_converter('convert_from_extras'),
                toolkit.get_validator('ignore_missing'),
                toolkit.get_validator('unicode_safe'),
            ],
            'references': [
                toolkit.get_converter('convert_from_extras'),
                toolkit.get_validator('ignore_missing'),
                toolkit.get_validator('unicode_safe'),
            ],
        })
        schema['resources'].update({
            'etag': [
                toolkit.get_validator('ignore_missing'),
            ],
            'sha256': [
                toolkit.get_validator('ignore_missing'),
            ],
        })
        # Add dclab configuration parameters
        for sec in dclab.dfn.CFG_METADATA:
            for key in dclab.dfn.config_keys[sec]:
                schema['resources'].update({
                    'dc:{}:{}'.format(sec, key): [
                        toolkit.get_validator('ignore_missing'),
                    ]})
        # Add supplementary resource schemas
        for composite_key in rss.get_composite_item_list():
            schema['resources'].update({
                composite_key: [
                    toolkit.get_validator('ignore_missing'),
                ]})
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    # IPackageController
    def after_dataset_update(self, context, data_dict):
        # This is a workaround for https://github.com/ckan/ckan/issues/6472.
        # `after_resource_create` is not triggered when updating a dataset
        # via `package_revise`. The workaround is to check in
        # `after_dataset_upgrade` which *is* triggered by `package_revise`.
        # To avoid running all of this every time a background job updates
        # a resource, we have this background-check case.
        # DCOR isue: https://github.com/DCOR-dev/ckanext-dcor_schemas/issues/19
        if not (IS_BACKGROUND_JOB
                or bool(context.get("is_background_job")) is True
                ):
            # Check for resources that have been added (e.g. using
            # package_revise) during this dataset update.
            # We need the "position" of each resource, so we must fetch
            # the whole dataset once.
            ds_dict = logic.get_action('package_show')(
                context,
                {'id': data_dict["id"]})

            for resource in data_dict.get('resources', []):
                # Do not perform any actions if the resource already
                # contains the "etag", which means that all background
                # jobs already ran.
                if resource and "id" in resource and "etag" not in resource:
                    # Update with current
                    for res in ds_dict["resources"]:
                        if resource["id"] == res["id"]:
                            res.update(resource)
                            resource = res
                            break
                    # Run jobs after resource create
                    for plugin in plugins.PluginImplementations(
                            plugins.IResourceController):
                        plugin.after_resource_create(context, resource)

            private = data_dict.get("private")
            if (private is not None and not private
                    # Only do this for "active" datasets, otherwise this will
                    # be run after *every* resource update (package_revise).
                    and data_dict["state"] == "active"):
                # Normally, we would only get here if the user specified the
                # "private" key in `data_dict`. Thus, it is not an overhead
                # for normal operations.
                # We now have a public dataset. And it could be that this
                # dataset has been private before. If we already have resources
                # in this dataset, then we have to set the S3 object tag
                # "public:true", so everyone can access it.
                # Make sure the S3 resources get the "public:true" tag.
                for res in data_dict["resources"]:
                    s3cc.make_resource_public(res["id"])

    # IPermissionLabels
    def get_dataset_labels(self, dataset_obj):
        """
        Add labels according to groups the dataset is part of.
        """
        labels = super(DCORDatasetFormPlugin, self).get_dataset_labels(
            dataset_obj)
        groups = dataset_obj.get_groups()
        labels += [u'group-%s' % grp.id for grp in groups]
        return labels

    def get_user_dataset_labels(self, user_obj):
        """
        Include group labels (If user is part of a group, then he
        should be able to see all private datasets therein).
        """
        labels = super(DCORDatasetFormPlugin, self
                       ).get_user_dataset_labels(user_obj)
        if user_obj and not user_obj.is_anonymous and hasattr(user_obj, "id"):
            # I initially meant to use `group_authz_list` for this, but
            # this one checks for `manage_group` while regular members only
            # have the `read` permission. Thus, directly ask the DB:
            q = (model.Session.query(model.Member.group_id)
                 .filter(model.Member.table_name == 'user')
                 .filter(model.Member.capacity.in_(["member"]))
                 .filter(model.Member.table_id == user_obj.id)
                 .filter(model.Member.state == 'active')
                 )
            grps = []
            for row in q:
                grps.append(row.group_id)
            labels.extend(u'group-%s' % g for g in grps)
        return labels

    # IResourceController
    def before_resource_create(self, context, resource):
        if "upload" in resource:
            # set/override the filename
            upload = resource["upload"]
            if hasattr(upload, "filename"):
                filename = upload.filename
            elif hasattr(upload, "name"):
                filename = pathlib.Path(upload.name).name
            else:
                raise ValueError(
                    f"Could not determine filename for {resource}")
            resource["name"] = filename
        resource.update(jobs.get_base_metadata(resource))

    def after_resource_create(self, context, resource):
        """Add custom jobs"""
        if not context.get("is_background_job"):
            # Make sure mimetype etc. are set properly
            resource.update(jobs.get_base_metadata(resource))

            # All jobs are defined via decorators in jobs.py
            jobs.RQJob.enqueue_all_jobs(resource, ckanext="dcor_schemas")

            # https://github.com/ckan/ckan/issues/7837
            datapreview.add_views_to_resource(context={"ignore_auth": True},
                                              resource_dict=resource)

    # ISignal
    def get_signal_subscriptions(self):
        # Let the admin know that a new user signed up
        subs = {}
        subs[ckan.lib.signals.user_created] = [signals.notify_user_created]
        return subs

    # ITemplateHelpers
    def get_helpers(self):
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        hlps = {
            'dcor_schemas_get_user_name': dcor_helpers.get_user_name,
            'dcor_schemas_get_reference_dict': dcor_helpers.get_reference_dict,
            'dcor_schemas_license_options': dcor_helpers.license_options,
            'dcor_schemas_get_composite_section_item_list':
            rss.get_composite_section_item_list
        }
        return hlps

    # IValidators
    def get_validators(self):
        return {
            "dcor_schemas_dataset_authors":
                dcor_validate.dataset_authors,
            "dcor_schemas_dataset_doi":
                dcor_validate.dataset_doi,
            "dcor_schemas_dataset_id":
                dcor_validate.dataset_id,
            "dcor_schemas_dataset_license_id":
                dcor_validate.dataset_license_id,
            "dcor_schemas_dataset_name_create":
                dcor_validate.dataset_name_create,
            "dcor_schemas_dataset_references":
                dcor_validate.dataset_references,
            "dcor_schemas_dataset_state":
                dcor_validate.dataset_state,
            "dcor_schemas_resource_dc_config":
                dcor_validate.resource_dc_config,
            "dcor_schemas_resource_dc_supplement":
                dcor_validate.resource_dc_supplement,
            "dcor_schemas_resource_id":
                dcor_validate.resource_id,
            "dcor_schemas_resource_name":
                dcor_validate.resource_name,
        }
