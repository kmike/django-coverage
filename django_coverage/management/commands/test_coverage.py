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
"""

from django.conf import settings
from django.core.management import call_command
from django.core.management.commands import test

from django_coverage import settings as coverage_settings

class Command(test.Command):
    help = ("Runs the test suite for the specified applications, or the "
            "entire site if no apps are specified. Then generates coverage "
            "report both onscreen and as HTML.")

    def handle(self, *test_labels, **options):
        """
        Replaces the original test runner with the coverage test runner, but
        keeps track of what the original runner was so that the coverage
        runner can inherit from it.  Then, call the test command. This
        plays well with apps that override the test command, such as South.
        """
        coverage_settings.ORIG_TEST_RUNNER = settings.TEST_RUNNER
        settings.TEST_RUNNER = coverage_settings.COVERAGE_TEST_RUNNER
        call_command('test', *test_labels, **options)

