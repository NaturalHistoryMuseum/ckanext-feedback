# !/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-feedback
# Created by the Natural History Museum in London, UK

from ckan.plugins import SingletonPlugin, implements, interfaces, toolkit


class FeedbackPlugin(SingletonPlugin):
    '''CKAN Contact Extension'''
    implements(interfaces.IConfigurer)

    ## IConfigurer
    def update_config(self, config):
        '''

        :param config: 

        '''
        toolkit.add_template_directory(config, u'theme/templates')
        toolkit.add_resource(u'theme/public', u'ckanext-feedback')
