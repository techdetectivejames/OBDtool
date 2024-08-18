import unittest

from obd_diagnostic.obd_reader import OBDTool

class TestOBDReader(unittest.TestCase):
    def setUp(self):
        self.reader = OBDTool(interface='usb')

    def test_read_data(self):
        response = self.reader.read_data('RPM')
        self.assertIsNotNone(response)
        #Replace rpm with a valid pid for my setup

    def tearDown(self):
        self.reader.disconnect()

if _name_ == '_main_':
    unittest.main()

