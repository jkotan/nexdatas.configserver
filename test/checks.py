#!/usr/bin/env python
#   This file is part of nexdatas - Tango Server for NeXus data writer
#
#    Copyright (C) 2012-2017 DESY, Jan Kotanski <jkotan@mail.desy.de>
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
# \package test nexdatas.configserver
# \file checks.py
# checks
#
import xml.etree.ElementTree as et
from lxml.etree import XMLParser


def checknodes(utest, n1, n2):
    """ compare etree nodes via unittests

    :param utest: unittest case object
    :type utest: :obj:`unittest.TestCase`
    :param n1: first node
    :type n1: :obj:`xml.etree.ElementTree.Element`
    :param n2: second node
    :type n2: :obj:`xml.etree.ElementTree.Element`
o    """
    utest.assertEqual(n1.tag, n2.tag)
    utest.assertEqual(n1.text, n2.text)
    utest.assertEqual(n1.tail, n2.tail)
    utest.assertEqual(len(n1), len(n2))
    utest.assertEqual(len(n1.attrib), len(n2.attrib))
    for k, v in n1.attrib.items():
        utest.assertTrue(k in n2.attrib.keys())
        utest.assertTrue(v, n2.attrib[k])
    for c1, c2 in zip(n1, n2):
        checknodes(utest, c1, c2)


def checkxmls(utest, xml1, xml2):
    """ compare xmls via unittests

    :param utest: unittest case object
    :type utest: :obj:`unittest.TestCase`
    :param xml1: first xml
    :type xml1: :obj:`str`
    :param xml2: second xml
    :type xml: :obj:`str`
    """
    n1 = et.fromstring(
        xml1,
        parser=XMLParser(collect_ids=False,
                         remove_blank_text=True))
    n2 = et.fromstring(
        xml2,
        parser=XMLParser(collect_ids=False,
                         remove_blank_text=True))
    checknodes(utest, n1, n2)
