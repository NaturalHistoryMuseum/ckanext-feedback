
#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-feedback
# Created by the Natural History Museum in London, UK

import ckan.plugins as p

class FeedbackPlugin(p.SingletonPlugin):
    '''CKAN Contact Extension'''
    p.implements(p.IConfigurer)

    ## IConfigurer
    def update_config(self, config):
        '''

        :param config: 

        '''
        p.toolkit.add_template_directory(config, u'theme/templates')
        p.toolkit.add_resource(u'theme/public', u'ckanext-feedback')
