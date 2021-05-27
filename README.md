This source code has been forked from [libnetconf2](https://github.com/CESNET/libnetconf2/) because the Python binding has been removed from the main source tree.

Requirements
------------

* Python 3
* libnetconf2

Building
--------
From the libnetconf2 main build:

$ python setup.py build 
$ python setup.py install

Usage
-----

>>> import netconf2
>>> session = netconf2.Session('localhost', 830)
>>> del(session)

