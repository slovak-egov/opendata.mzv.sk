from flask import Blueprint

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.plugins import DefaultTranslation
from ckanext.mzv_theme.controller import MzvController


class MzvThemePlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
                             'mzv_theme')

    def get_blueprint(self):
        blueprint = Blueprint(self.name, self.__module__)
        # blueprint.template_folder = u'templates'

        rules = [
            (u'/technical-support', u'technical_support', MzvController.technical_support),
            (u'/content-manager', u'content_manager', MzvController.content_manager),
            (u'/cookies', u'cookies', MzvController.cookies),
            (u'/accessibility-statement', u'accessibility_statement', MzvController.accessibility_statement),
            (u'/contact', u'contact', MzvController.contact),
            (u'/docs', u'docs', MzvController.docs),
            (u'/api_docs', u'api_docs', MzvController.api_docs),
            (u'/', u'index', MzvController.index),
        ]
        for rule in rules:
            blueprint.add_url_rule(*rule)

        return blueprint

    def get_helpers(self):
        from ckanext.mzv_theme import helpers as mzv_helpers
        '''Register funkcie hore ako template helper funkcie'''

        # Nazvy helper funkcii pre sablony by mali zacinat
        # nazvom rozsirenia, do ktoreho patria, aby sa zabranilo konfliktom
        return {
            'mzv_theme_sum_organization': mzv_helpers.sum_organization,
            'mzv_theme_sum_group': mzv_helpers.sum_group,
            'mzv_theme_sum_dataset': mzv_helpers.sum_dataset,
            'mzv_theme_sum_resource': mzv_helpers.sum_resource,
            'mzv_theme_declension_dataset': mzv_helpers.declension_dataset,
            'mzv_theme_declension_group': mzv_helpers.declension_group,
            'mzv_api_resource_id': mzv_helpers.api_resource_id,
        }
