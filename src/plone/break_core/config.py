# -*- coding: utf-8 -*-

import logging

#: Logger instance globaly used in this package 
logger = logging.getLogger("plone.break_core")

#: URL of the vulnerability data base
VULNERABILITY_DB_URL = "http://testplone.org/"
#vulnerability_db_url = "http://plone.org/"

#: URL of Python Package Index 
#: used to recive JSON data from package index
PYPI_URL = "https://pypi.python.org/pypi/"


class VulnerabilityError(Exception):
    """VulnerabilityError is an Exception that indicates 
    that an insecure Plone version is in use.
    """

    def __str__(self):
        return " ".join(map(str, self.args))
