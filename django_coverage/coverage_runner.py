"""
Copyright 2009 55 Minutes (http://www.55minutes.com)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Changed by Mikhail Korobov.
"""

import coverage, os, sys

from django_coverage import settings
from django.db.models import get_app, get_apps
from django.test.simple import run_tests as base_run_tests

from utils.module_tools import get_all_modules
from utils.coverage_report import html_report

def _get_app_package(app_model_module):
    """
    Returns the app module name from the app model module.
    """
    return '.'.join(app_model_module.__name__.split('.')[:-1])

def run_tests(test_labels, verbosity=1, interactive=True,
              extra_tests=[]):
    """
    Test runner which displays a code coverage report at the end of the
    run.
    """
    coverage.use_cache(0)
    for e in settings.COVERAGE_CODE_EXCLUDES:
        coverage.exclude(e)
    coverage.start()
    results = base_run_tests(test_labels, verbosity, interactive, extra_tests)
    coverage.stop()

    coverage_modules = []
    if test_labels:
        for label in test_labels:
            label = label.split('.')[0]
            app = get_app(label)
            coverage_modules.append(_get_app_package(app))
    else:
        for app in get_apps():
            coverage_modules.append(_get_app_package(app))

    coverage_modules.extend(settings.COVERAGE_ADDITIONAL_MODULES)

    packages, modules, excludes, errors = get_all_modules(
        coverage_modules, settings.COVERAGE_MODULE_EXCLUDES,
        settings.COVERAGE_PATH_EXCLUDES)

    coverage.report(modules.values(), show_missing=1)
    if excludes:
        print >>sys.stdout
        print >>sys.stdout, "The following packages or modules were excluded:",
        for e in excludes:
            print >>sys.stdout, e,
        print >>sys.stdout
    if errors:
        print >>sys.stdout
        print >>sys.stderr, "There were problems with the following packages or modules:",
        for e in errors:
            print >>sys.stderr, e,
        print >>sys.stdout

    outdir = settings.COVERAGE_REPORT_HTML_OUTPUT_DIR
    outdir = os.path.abspath(outdir)
    html_report(outdir, modules, excludes, errors)
    print >>sys.stdout
    print >>sys.stdout, "HTML reports were output to '%s'" %outdir

    return results

