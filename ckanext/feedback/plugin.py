"""
CKAN Contact Extension
"""

import ckan.plugins as p

class FeedbackPlugin(p.SingletonPlugin):
    """
    CKAN Contact Extension
    """
    p.implements(p.IConfigurer)

    ## IConfigurer
    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'theme/templates')
        p.toolkit.add_resource('theme/public', 'ckanext-feedback')