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

