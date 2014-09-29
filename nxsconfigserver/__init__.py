#!/usr/bin/env python
#   This file is part of nexdatas - Tango Server for NeXus data writer
#
#    Copyright (C) 2012-2014 DESY, Jan Kotanski <jkotan@mail.desy.de>
#
#    nexdatas is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    nexdatas is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with nexdatas.  If not, see <http://www.gnu.org/licenses/>.
## \package mcs nexdatas
## \file __init__.py
# package constructor

""" Implementation of NexDaTaS Configuration Server """

## version number
__version__ = "1.6.4"

import sys


## runs the TANGO server
# \param argv command-line arguments
def run(argv):
    """ runs the Configuration TANGO server """
    import PyTango
    from .NXSConfigServer import NXSConfigServer as NXSCnfSrv
    from .NXSConfigServer import NXSConfigServerClass as NXSCnfSrvClass
    try:
        pyutil = PyTango.Util(argv)
        pyutil.add_class(NXSCnfSrvClass, NXSCnfSrv, 'NXSConfigServer')

        util = PyTango.Util.instance()
        util.server_init()
        util.server_run()

    except PyTango.DevFailed as ex:
        print '-------> Received a DevFailed exception:', ex
    except Exception as ex:
        print '-------> An unforeseen exception occured....', ex
