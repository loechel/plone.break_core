from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='plone.break_core',
    version=version,
    description="hCore Package for plone.break.* products",
    long_description=open("README.txt").read() + "\n" +
                     open(os.path.join("docs", "HISTORY.txt")).read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
      'Framework :: Plone',
      'Programming Language :: Python',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GPL',
      'Programming Language :: Python',
      'Natural Language :: English',
      'Operating System :: OS Independent',
      'Topic :: Software Development :: Quality Assurance',
      ],
    keywords='buildout plone zope test security break',
    author='Alexander Loechel',
    author_email='Alexander.Loechel@lmu.de',
    url='https://github.com/collective/plone.break_core',
    license='GPL',
    packages=find_packages('src',exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['plone'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
