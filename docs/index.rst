==========================
Plone Vulnerability Checks
==========================

The Plone Vulnerability Checks Packages exists to inform Webmasters and Administrators if their Plone Setup is running a version that is:

* under active security support
* under active maintenance
* or if vulnerabilities exists for which a hotfix is avaliable but not applied

Plone Vulnerability Checks constists of a core package (plone.vulnerabilitychecks.core) with basis utils and 3 specif packages for action:

* plone.vulnerabilitychecks.buildout
* plone.vulnerabilitychecks.instance_startup
* plone.vulnerabilitychecks.tests

Plone Security Recommendations
==============================

*Security matters.*
That is what the Plone Community believe in. 

As an Administrator of any Web Application and Website you should be aware that this is primary technical attack vector. 
Independent Security Agencies and Security Authorities recommend that you should take at least 15 minutes per day to check if your System is secure, and you run the latest bugfix release and have applied all hotfixes.
Plone Vulnerability Checks aims at this and try to provide a way to inform you as a System Owner to know if your System is up to date.

Please Ensure you have subscribed to the Plone Announcement mailing list: announcement@list.plone.org / list.plone.org/announcement

What does Plone Vulnerability Checks do?
========================================




Side-Effects
------------

As Plone Vulnerability Checks needs to know which Plone Versions are Vulnerabil it has to communicat with an authoritive. 
By Default, plone.vulnerabilitychecks.core uses https://plone.org/security/hotfix_json as authorative. 
But as we are aware of, that a lot of Plone installations are for Intranets of set up by security aware personal you normaly don't want your servers to "call home". 






.. code:: ini

    #############################################################################
    # Plone Vulnerability Checks Configuration
    # you might have these applied if you use one of the following packages
    # enabled in your buildout:
    # * plone.vulnerabilitychecks.instance_startup
    # * plone.vulnerabilitychecks.tests
    # * plone.vulnerabilitychecks.buildout
    # * plone.vulnerabilitychecks.control_panel <-- might be renamed to plone.security_control_panel
    # all of these packages depend on plone.vulnerabilitychecks.core.
    #
    # Detailed parameters are described below.
    #
    # If you set break-level and warn to 0 and handle-offline to nothing you
    # propably should better remove p.v.instance_startup and p.v.buildout from
    # your buildout config.
    #############################################################################
    [vulnerabilitychecks]
    # source-url
    #  source-url could be used for an alternative Source to gain information
    #  about hotfixes in Plone. This Source could be a caching-proxy or a system
    #  that supplies same information as following plone.app.vulnerabilities views:
    #  * hotfix_json
    #  * hotfix_feed
    #  Use this if you would like to use p.v.* in a closed network or would not like
    #  Zope / Plone to call home.
    #
    #  Default: https://plone.org/
    source-url = http://testplone.org/

    # break-level / warn-level
    #  0 --> no break / warning
    #  1 --> break / warn on current known vulnerability
    #  2 --> break / warn on current version has a newer bugfix release
    #        and this is in scurity support
    #  3 --> break / warn on release series (whole minor release series)
    #        is security support but not in active maintenance anymore
    #  4 --> break / warn on release series (whole minor release series)
    #        is not in security support anymore

    # break-level Default 1 --> only break on current known vulnerability
    break-level = 1
    # warn-level Default 4 --> warn on any security condition
    warn-level = 4

    # handle-offline:
    #  nothing  --> do nothing if no connection to source-url is possible
    #               --> always assume secure
    #  warn     --> warn if no connection to source-url is possible
    #               --> assume insecure
    #  break    --> break if no connection to source-url is possible
    #               --> assume insecure
    # Default: warn
    handle_offline = warn

    [vulnerabilitychecks_control_panel]
    # warn-roles
    # due to the fact that multiple Plone instances could be served by a
    # zope instance / cluster
    warn-roles =
        manager
        site-administrator

    # send e-mail to site manager on upcoming hotfix / existing vulnerability
    # multiple e-mail addresses possible (one per line)
    mail-to =
    #    webmaster@example.com
    mail-attempts = -1
