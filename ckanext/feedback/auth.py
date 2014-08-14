#!/usr/bin/env python
# encoding: utf-8
"""
Created by 'bens3' on 2013-06-21.
Copyright (c) 2013 'bens3'. All rights reserved.
"""


import ckan.new_authz as new_authz
from ckan.common import _

def send_feedback(context, data_dict):
    user = context['user']
    if new_authz.auth_is_anon_user(context):
        return {'success': False, 'msg': _('User %s not authorized to create packages') % user}
    return {'success': True}