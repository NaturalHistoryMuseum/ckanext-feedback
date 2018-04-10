#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-feedback
# Created by the Natural History Museum in London, UK

from setuptools import setup, find_packages

version = u'0.1'

setup(
	name=u'ckanext-feedback',
	version=version,
	description=u'CKAN Extension providing feedback form',
	classifiers=[],
	keywords=u'',
	author=u'Ben Scott',
	author_email=u'ben@benscott.co.uk',
	url=u'',
	license=u'',
    packages=find_packages(exclude=[u'tests']),
    namespace_packages=[u'ckanext', u'ckanext.feedback'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[],
	entry_points=\
	u'''
    [ckan.plugins]
    	feedback=ckanext.feedback.plugin:FeedbackPlugin
	''',
)
