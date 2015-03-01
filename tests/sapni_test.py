#!/usr/bin/env python
# ===========
# SAP Dissector Plugin for Wireshark
#
# Copyright (C) 2015 Core Security Technologies
#
# The plugin was designed and developed by Martin Gallo from the Security
# Consulting Services team of Core Security Technologies.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# ==============

# Standard imports
import unittest
# External imports
from scapy.all import *
from pysap.SAPNI import SAPNI
# Custom imports
from basetestcase import WiresharkTestCase


class WiresharkSAPNITestCase(WiresharkTestCase):

    def test_sapni_dissection(self):
        """Test dissection of a basic SAP NI packet. """
        pkt = Ether()/IP()/TCP(dport=3299)/SAPNI()/"LALA"
        
        packet = self.get_capture(pkt)[0]
        
        self.assertIn('sapni', packet)
        self.assertEqual(int(packet['sapni'].length), 4)


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(WiresharkSAPNITestCase))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())
