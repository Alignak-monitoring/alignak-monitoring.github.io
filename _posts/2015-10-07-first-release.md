---
layout: post
title:  "First release of Alignak: 0.1!"
date:   2015-10-07 18:40:42
categories: release
---

It has been 5 months now since the Alignak project started. It's time for the first minor release (0.1). [Alignak project](https://github.com/Alignak-monitoring/alignak) is a monitoring framework based on Shinken who tend to follow OpenStack standards and integrate with it.

In others words, it is a Shinken distribution more OpenStack "compliant". OpenStack rules are [really stricts](http://governance.openstack.org/reference/new-projects-requirements.html) and it was not possible to follow them in Shinken. For example, code review is required in the development process which was declined by the project creator.

Consequently, the team took Shinken source code and started to develop this way.

Alignak project worked hard this summer, here are a few things we did: 

* Pylint code quality. There is still ~20% to do (errors found / total errors before starting). This allowed us to find a lot a code issue and add docstrings (documentation). Python is programming language made to be readable and easily understandable.
* Rewrite daemon communication. Client side is based on python-requests (previously pycurl). Server side has been partially rewritten. Cherrypy is the only backend available and it is also used as a framework (instead of bottle). We chose those lib for the python3 and Pypy compatibility (OpenStack requirement).
* Removal of external lib shipped in the code (bottle, termcolor, importlib). Libs needed are now in the python requirement file.
* Removal of dead or very old code. Some part where python 2.5 specific or android (2.x) specific.
* Partial rewrite of timeperiods. Parsing and timeperiod detection was not using standard python lib to deal with calendar dates. This is now fixed and tests have been added.
* Configuration files structure. Configuration files for the arbiter were is the same folder than other daemon configuration file. This could lead to confusion for new users or distributed setup.
* Namespace support for module setup. Alignak modules can be setup as python namespaces. It allows a standard Alignak module setup (python setup.py install) and Alignak will automatically load it (instead of copying sources to "modules_dir" directory)
* Functional tests. For now, tests are focuses on the API HTTP part, used for inter-daemon communication. New tests will be added shortly.
* Clean unit tests. Unit tests configuration file were duplicated a lot. It's now easier to create a simple case and understand how they work.


In addition, the team have found an agreement on development process. Here it is:

* Master branch is only used to release and tags. There is only merge __from__ develop  _to_  master. This ensure a stable master branch and a version of Alignak that can be setup.
* Develop branch is used for common development. No commit is made directly to this branch without review.
* Reviews are made with GitHub Pull Requests. Every PR needs to meet some requirements to be merged. For example, tests and documentation are needed. You can have a look in the documentation.


For an easy setup, DEB (Debian/Ubuntu) and RPM (RHEL/CentOS/Fedora) are available. Packaging sources are available on a [specific repository](https://github.com/Alignak-monitoring/alignak-packaging)
Build packages are also available on the [website](http://alignak-monitoring.github.io/)

Documentation is available on readthedocs : [http://alignak-doc.rtfd.org](http://alignak-doc.rtfd.org) (user),  [http://alignak.rtfd.org](http://alignak.rtfd.org) (developer)

Two mailing lists are also available to registration : alignak@freelists.org ( user, registration  [http://www.freelists.org/list/alignak](http://www.freelists.org/list/alignak) ), alignak-devel@freelists.org ( developer, registration [http://www.freelists.org/list/alignak-devel](http://www.freelists.org/list/alignak-devel) )

You can also reach us on IRC (chan #alignak on Freenode) or on Twitter @alignak_monitor.

