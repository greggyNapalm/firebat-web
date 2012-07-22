Firebat-Web
===========

Web application which aggregates, stores and represent load tests results.

Documentation
-------------

Coming soon

Requirements
------------

* GNU Linux
* Python >= 2.7 (Not Python3)

Installation
------------

Use pip and `vurtualev/virtualenvwrapper <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_

Stable version:

::

    Coming soon

Development version:

::

    $ git clone git://github.com/greggyNapalm/firebat-web.git; cd firebat-web
    $ pip install -r requirements-dev.txt
    $ cp -p firebat-web.default.cfg firebat-web.local.cfg
    $ export FIRE_WEB_CFG=`readlink -e firebat-web.local.cfg`
    $ ./run.py


Screenshots
-----------

Coming soon

Issues
------

Find a bug? Want a feature? Submit an `<https://github.com/greggyNapalm/firebat-web/issues>`_. Patches welcome!

License
-------
Major components:

* jQuery: MIT/GPL license.
* Highcharts: Creative Commons Attribution-NonCommercial 3.0 License.
* Twitter Bootstrap: Apache License, Version 2.0

Everything else:
BSD `Read more <http://opensource.org/licenses/BSD-3-Clause>`_
