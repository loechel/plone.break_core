# -*- coding: utf-8 -*-

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
		data = { 
			"hotfixes":[],
   			"security":True,
   			"maintenance":True,
   			}

   		try:
			plone_request = urllib2.Request(plone_instance_url+"hotfix_json?version="+version)
			response = urllib2.urlopen(request, timeout=5)
			data = json.load(response)
		except:
			pass
		self.data = data
		self.__isInSecuritySupport = data[u'security']
		self.__isInActiveMaintenanceSupport = data[u'maintenance']
		self.__hotfixes = data[u'hotfixes']
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

	def getLatestVersion(self):
		request = urllib2.Request(pypi_url+"Plone/json")
		response = urllib2.urlopen(request, timeout=5)
		data = json.load(response)
		return data['info']['version']

	def getLatestBugfixRelease(self):
		"""

		"""
		data = []
   		try:
			request = urllib2.Request(plone_instance_url+"hotfix_json")
			response = urllib2.urlopen(request, timeout=5)
			data = json.load(response)
		except:
			pass

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
