========================
Django Test Coverage App
========================

.. contents::

What is it?
===========
A test coverage reporting tool that utilizes `Ned Batchelder`_'s
excellent coverage.py_ to show how much of your code is exercised with
your tests.

Dependencies
============
* Django_ 1.2 and above. For earlier versions, try version 1.0.3 of
  django-coverage.
* coverage.py_

How do I use it?
================
Install as a Django app
-----------------------
1. Place the entire ``django_coverage`` app in your third-party apps
   directory.
2. Update your ``settings.INSTALLED_APPS`` to include ``django_coverage``.
3. Include test coverage specific settings in your own settings file.
   See ``settings.py`` for more detail.

Once you've completed all the steps, you'll have a new custom command
available to you via ``manage.py test_coverage``. It works just like
``manage.py test``.

Use it as a test runner
-----------------------
You don't have to install ``django_coverage`` as an app if you don't want
to. You can simply use the test runner if you like.

1. Update ``settings.TEST_RUNNER =
   'django_coverage.coverage_runner.CoverageRunner'``
2. Include test coverage specific settings in your own settings file.
   See ``settings.py`` for more detail.
3. Run ``manage.py test`` like you normally do.


Extras
======
Coverage badges
---------------
``django_coverage`` will also generate a badge image that represents
the percentage coverage that your project has.

This will be stored in the same directory as the coverage report data:
``$PROJECT/.coverage/coverage_status.png``.

Currently, the only badge type that is included is drone.io_. When other
types are included, you will be able to select which is used by 
``settings.COVERAGE_BADGE_TYPE``.

To prevent the badge generation, you could set this to ``None``.

Using the coverage badge with drone.io_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

drone.io_ has no native support for coverage reporting. However, you
can save build artifacts: just tell it to save one called:
``.coverage/coverage_status.png``. Then you can reference it in your
project's README.

And that's it.


.. _George Song: mailto:george@55minutes.com
.. _55 Minutes: http://www.55minutes.com/
.. _Ned Batchelder: http://nedbatchelder.com
.. _coverage.py: http://bitbucket.org/ned/coveragepy/
.. _Django: http://www.djangoproject.com/
.. _drone.io: http://drone.io/
