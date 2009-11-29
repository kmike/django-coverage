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
* Django_ 1.0.2 and above. It may work with earlier versions, but I
  haven't tested anything prior to 1.0.2 explicitly.
* coverage.py_

How do I use it?
================
Install as a Django app
-----------------------
1. Place the entire ``test_coverage`` app in your third-party apps
   directory.
2. Update your ``settings.INSTALLED_APPS`` to include ``test_coverage``.
3. Include test coverage specific settings in your own settings file.
   See ``settings.py`` for more detail.

Once you've completed all the steps, you'll have a new custom command
available to you via ``manage.py test_coverage``. It works just like
``manage.py test``.

Use it as a test runner
-----------------------
You don't have to install ``test_coverage`` as an app if you don't want
to. You can simply use the test runner if you like.

1. Update ``settings.TEST_RUNNER =
   'test_coverage.coverage_runner.run_tests'``
2. Include test coverage specific settings in your own settings file.
   See ``settings.py`` for more detail.
3. Run ``manage.py test`` like you normally do.

And that's it.


.. _George Song: mailto:george@55minutes.com
.. _55 Minutes: http://www.55minutes.com/
.. _Ned Batchelder: http://nedbatchelder.com
.. _coverage.py: http://bitbucket.org/ned/coveragepy/
.. _Django: http://www.djangoproject.com/