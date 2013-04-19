#!/usr/bin/env python
from distutils.core import setup
from django_coverage import __version__

setup(
      name='django-coverage',
      version=__version__,
      author='George Song',
      author_email='george@55minutes.com',
      maintainer = 'Mikhail Korobov',
      maintainer_email = 'kmike84@gmail.com',
      url = 'https://bitbucket.org/kmike/django-coverage/',

      description = 'Django Test Coverage App',
      long_description = "A test coverage reporting tool that utilizes "
                         "Ned Batchelder's excellent coverage.py to show how "
                         "much of your code is exercised with your tests.",

      license = 'Apache License 2.0',
      packages=['django_coverage',
                'django_coverage.management',
                'django_coverage.management.commands',
                'django_coverage.utils',
                'django_coverage.utils.module_tools',
                'django_coverage.utils.coverage_report',
                'django_coverage.utils.coverage_report.templates'],
      package_data={'django_coverage': ['utils/coverage_report/badges/*/*.png']},

      requires = ['django (>=1.2)', 'coverage (>= 2.85)'],

      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: Testing',
      ],
)
