# -*- coding: utf-8 -*-

from pkg_resources import parse_version, Requirement
from setuptools import package_index

import json
import logging
import urllib2

plone_instance_url = "http://testplone.org/"
#plone_instance_url = "http://plone.org/"
pypi_url = "https://pypi.python.org/pypi/"

class SecurityError(Exception):
    """Security Error that indicates that an insecure Plone version is in use."""

    def __str__(self):
        return " ".join(map(str, self.args))


class VulnerabilityCheck(object):
	"""

	"""

	def __init__(self, version, patch_list=[]):
		"""

		"""
		self.requested_version = version

		# relevant Pattern of response 
		#data = { 
		#	"hotfixes":[],
   		#	"security":True,
   		#	"maintenance":True,
   		#	}

   		data = None

   		try:
			request = urllib2.Request(plone_instance_url+"hotfix_json?version="+version)
			response = urllib2.urlopen(request, timeout=5)
			data = json.load(response)
		except:

			pass
		if data == None:
			# Requested a URL that eigther don't respond 
			# or the requested version is not avaliable.
			data = { 
				"hotfixes":[],
	   			"security":True,
	   			"maintenance":True,
	   			}

		self.data = data

		self.__isInSecuritySupport = data.get(u'security', True)
		self.__isInActiveMaintenanceSupport = data.get(u'maintenance', True)
		self.__hotfixes = data.get(u'hotfixes', [])
		patch_prefix = 'Products.PloneHotfix'
		self.__patches = []
		for hotfix in self.__hotfixes:
			self.__patches.append(patch_prefix+hotfix[u'name'])
		if self.__hotfixes is None or self.__hotfixes == []:
			self.__isSecure = True
		else:
			if self.__patches in patch_list:
				self.__isSecure = True
			else:
				self.__isSecure = False

		import ipdb; ipdb.set_trace()

	def isSecure(self):
		"""

		"""
		return self.__isSecure


	def isInSecuritySupport(self):
		"""

		"""
		return self.__isInSecuritySupport

	def isInActiveMaintenanceSupport(self):
		"""

		"""
		return self.__isInActiveMaintenanceSupport

	def getPatches(self):
		"""

		"""
		return self.__patches

	def __getLatestVersion_via_JSON(self):
		request = urllib2.Request(pypi_url+"Plone/json")
		response = urllib2.urlopen(request, timeout=5)
		data = json.load(response)
		return data['info']['version']

	def __getLatestVersion_via_Setuptools(self):
		pi = package_index.PackageIndex(search_path=())
		req = Requirement.parse('Plone')
		pi.find_packages(req)
		data = pi[req.key][0]
		return data.version


	def getLatestBugfixRelease(self):
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
		my_version = splitVersion(self.requested_version)
		
		for version in data:
			this_version = splitVersion(version['name'])
			if  this_version[0] == my_version[0] and \
				this_version[1] == my_version[1] and \
				this_version[2] >= my_version[2]:
				version_list.append(this_version)
		version_list.sort(key=lambda k: k[2], reverse=True)
		return ".".join(version_list[0])

	def getLatestVersion(self):
		json_version = self.__getLatestVersion_via_JSON()
		pkg_version = self.__getLatestVersion_via_Setuptools()
		if json_version == pkg_version:
			return pkg_version
		else:
			return json_version

def splitVersion(inputVersion):
	"""

	"""
	version = [1,0,0]
	splittedVersion = inputVersion.split('.')
	if len(splittedVersion) == 3:
		version[2] = splittedVersion[2]
	version[0] = splittedVersion[0]
	version[1] = splittedVersion[1]
	return tuple(version)
