"""
CKAN Contact Extension
"""
import os
from logging import getLogger
import ckan.plugins as p
from ckanext.feedback.auth import send_feedback

log = getLogger(__name__)

class FeedbackPlugin(p.SingletonPlugin):
    """
    CKAN Contact Extension
    """
    p.implements(p.IRoutes, inherit=True)
    p.implements(p.IConfigurer)
    p.implements(p.IAuthFunctions)

    ## IConfigurer
    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'theme/templates')

    ## IRoutes
    def before_map(self, map):

        # Add controller for KE EMu specimen records
        map.connect('feedback_form', '/feedback',
                    controller='ckanext.feedback.controllers.feedback:FeedbackController',
                    action='form')

        return map

    ## IAuthFunctions
    def get_auth_functions(self):
        return {'send_feedback': send_feedback}

