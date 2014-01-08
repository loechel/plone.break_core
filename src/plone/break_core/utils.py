# -*- coding: utf-8 -*-

from pkg_resources import parse_version
from pkg_resources import Requirement
from setuptools import package_index

import json
import logging
import urllib2

plone_instance_url = "http://testplone.org/"
#plone_instance_url = "http://plone.org/"
pypi_url = "https://pypi.python.org/pypi/"



def _getLatestVersion_via_JSON(package='Plone'):
	request = urllib2.Request(pypi_url+package+"/json")
	response = urllib2.urlopen(request, timeout=5)
	data = json.load(response)
	return data['info']['version']

def _getLatestVersion_via_Setuptools(package='Plone'):
	pi = package_index.PackageIndex(search_path=())
	req = Requirement.parse(package)
	pi.find_packages(req)
	data = pi[req.key][0]
	return data.version


def _getLatestBugfixRelease_via_JSON(package='Plone', version='0.0.0'):
	"""

	"""
	data = None
		try:
		request = urllib2.Request(plone_instance_url+"hotfix_json")
		response = urllib2.urlopen(request, timeout=5)
		data = json.load(response)
	except:
		pass
	if data == None:
		data = []

	version_list = []
	my_version = splitVersion(version)
	
	for version_item in data:
		this_version = splitVersion(version_item['name'])
		if  this_version[0] == my_version[0] and \
			this_version[1] == my_version[1] and \
			this_version[2] >= my_version[2]:
			version_list.append(this_version)
	version_list.sort(key=lambda k: k[2], reverse=True)
	return ".".join(version_list[0])

def _getLatestBugfixRelease_via_Setuptools(package='Plone', version='0.0.0'):
	pi = package_index.PackageIndex(search_path=())
	req = Requirement.parse(package)
	pi.find_packages(req)
	data = pi[req.key]
	result_version = '0.0.0'
	for version_item in data:
		this_version = version_item.version()
		return this_version ? compareVersions(this_version, version) : version


def getLatestVersion(package='Plone', version='0.0.0'):
	json_version = _getLatestVersion_via_JSON(package)
	pkg_version = _getLatestVersion_via_Setuptools(package)
	if json_version == pkg_version:
		return pkg_version
	else:
		return json_version

def getLatestBugfixRelease(package='Plone', version='0.0.0'):
	json_version = _getLatestBugfixRelease_via_JSON(package)
	pkg_version = _getLatestBugfixRelease_via_Setuptools(package)
	if json_version == pkg_version:
		return pkg_version
	else:
		return json_version


def split_version(inputVersion):
	"""

	"""
	version = [1,0,0]
	splittedVersion = inputVersion.split('.')
	if len(splittedVersion) == 3:
		version[2] = splittedVersion[2]
	version[0] = splittedVersion[0]
	version[1] = splittedVersion[1]
	return tuple(version)

def compare_versions(current_version, new_version):
	"""

	"""
	return parse_version(current_version) > parse_version(new_version)



__final_parts = '*final-', '*final'
def is_final_version(parsed_version):
    """Function copied from zc.buildout.easy_install._final_version"""
    for part in parsed_version:
        if (part[:1] == '*') and (part not in __final_parts):
            return False
    return True

def is_pre_final_version(parsed_version):
	"""

	"""
	return not is_final_version(parsed_version)
