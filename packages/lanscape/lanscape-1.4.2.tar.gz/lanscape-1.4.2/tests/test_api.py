"""
API integration tests for the LANscape application.
Tests REST API endpoints for port management, subnet validation, and scan operations.
"""
import json
import time
import unittest
from unittest.mock import patch

from lanscape.ui.app import app
from lanscape.libraries.net_tools import get_network_subnet

from ._helpers import right_size_subnet


class ApiTestCase(unittest.TestCase):
    """
    Test cases for the LANscape REST API.
    Tests the full lifecycle of API operations including port list management,
    subnet validation, and network scanning functionality.
    """
    app = app.test_client()

    def test_port_lifecycle(self):
        """
        Test the complete lifecycle of port list management through the API.
        Creates, retrieves, updates, and deletes a port list through API endpoints.
        """
        # Delete the new port list if it exists
        self.app.delete('/api/port/list/test_port_list_lifecycle')

        # Get the list of port lists
        response = self.app.get('/api/port/list')
        self.assertEqual(response.status_code, 200)
        port_list_start = json.loads(response.data)

        # Create a new port list
        new_port_list = {'80': 'http', '443': 'https'}
        response = self.app.post(
            '/api/port/list/test_port_list_lifecycle', json=new_port_list)
        self.assertEqual(response.status_code, 200)

        # Get the list of port lists again
        response = self.app.get('/api/port/list')
        self.assertEqual(response.status_code, 200)
        port_list_new = json.loads(response.data)
        # Verify that the new port list is in the list of port lists
        self.assertEqual(len(port_list_new), len(port_list_start) + 1)

        # Get the new port list
        response = self.app.get('/api/port/list/test_port_list_lifecycle')
        self.assertEqual(response.status_code, 200)
        port_list = json.loads(response.data)
        self.assertEqual(port_list, new_port_list)

        # Update the new port list
        updated_port_list = {'22': 'ssh', '8080': 'http-alt'}
        response = self.app.put(
            '/api/port/list/test_port_list_lifecycle', json=updated_port_list)
        self.assertEqual(response.status_code, 200)

        # Get the new port list again
        response = self.app.get('/api/port/list/test_port_list_lifecycle')
        self.assertEqual(response.status_code, 200)
        port_list = json.loads(response.data)

        # Verify that the new port list has been updated
        self.assertEqual(port_list, updated_port_list)

        # Delete the new port list
        response = self.app.delete('/api/port/list/test_port_list_lifecycle')
        self.assertEqual(response.status_code, 200)

    def test_scan(self):
        """
        Test the scan API functionality by creating and monitoring a network scan.
        Verifies scan creation, status retrieval, and UI rendering for scan results.
        """
        # Delete the new port list if it exists
        self.app.delete('/api/port/list/test_port_list_scan')

        # Create a new port list
        new_port_list = {'80': 'http', '443': 'https'}
        response = self.app.post(
            '/api/port/list/test_port_list_scan', json=new_port_list)
        self.assertEqual(response.status_code, 200)

        # Create a new scan, wait for completion
        new_scan = {
            'subnet': right_size_subnet(get_network_subnet()),
            'port_list': 'test_port_list_scan',
            'lookup_type': ['POKE_THEN_ARP']
        }
        response = self.app.post('/api/scan/async', json=new_scan)
        self.assertEqual(response.status_code, 200)
        scan_info = json.loads(response.data)
        self.assertEqual(scan_info['status'], 'complete')
        scanid = scan_info['scan_id']
        self.assertIsNotNone(scanid)

        # Validate the scan worked without error
        response = self.app.get(f"/api/scan/{scanid}")
        self.assertEqual(response.status_code, 200)
        scan_data = json.loads(response.data)
        self.assertEqual(scan_data['errors'], [])
        self.assertEqual(scan_data['stage'], 'complete')

        self._render_scan_ui(scanid)

        # Delete the new port list
        response = self.app.delete('/api/port/list/test_port_list_scan')
        self.assertEqual(response.status_code, 200)

    def test_subnet_ports(self):
        """
        Test to ensure multi-subnet dectection is working
        """

        response = self.app.get('/api/tools/subnet/list')
        self.assertEqual(response.status_code, 200)

        subnets = json.loads(response.data)
        self.assertIsNot(len(subnets), 0)
        self.assertIsInstance(subnets[0], dict)
        subnet: dict = subnets[0]
        self.assertIsNotNone(subnet.get('address_cnt'))

    def test_subnet_validation(self):
        """
        test subnet validation and parsing is working as expected
        """
        subnet_tests = {
            # subnet : count (-1 == invalid)
            '10.0.0.0/24': 254,
            '10.0.0.2/24': 254,
            '10.0.0.1-100': 100,
            '192.168.1.1/25': 126,
            '10.0.0.1/24, 192.168.1.1-100': 354,
            '10.0.0.1/20': 4094,
            '10.0.0.1/19': 8190,
            '': -1,  # blank
            '10.0.1/24': -1,  # invalid
            '10.0.0.1/2': -1,  # too big
            '10.0.0.1/19, 192.168.1.1/20': 12284,
            '10.0.0.1/17, 192.168.0.1/16': 98300,
            '10.0.0.1/20, 192.168.0.1/20, 10.100.0.1/20': 12282,
            '10.0.0.1/17, 192.168.0.1/16, 10.100.0.1/20': -1
        }

        for subnet, count in subnet_tests.items():
            uri = f'/api/tools/subnet/test?subnet={subnet}'
            response = self.app.get(uri)
            self.assertEqual(response.status_code, 200)

            data: dict = json.loads(response.data)
            self.assertEqual(data.get('count'), count)
            self.assertIsNotNone(data.get('msg'))
            if count == -1:
                self.assertFalse(data.get('valid'))

    def test_default_scan_configs_adjust_for_arp_support(self):
        """Accurate preset should fall back when ARP lookup is unavailable."""
        with patch('lanscape.ui.blueprints.api.tools.is_arp_supported', return_value=False):
            response = self.app.get('/api/tools/config/defaults')

        self.assertEqual(response.status_code, 200)
        configs = json.loads(response.data)

        accurate_lookup = configs['accurate']['lookup_type']
        self.assertNotIn('ARP_LOOKUP', accurate_lookup)
        self.assertIn('POKE_THEN_ARP', accurate_lookup)

    def test_default_scan_configs_keep_arp_when_supported(self):
        """Accurate preset should retain ARP lookup when supported."""
        with patch('lanscape.ui.blueprints.api.tools.is_arp_supported', return_value=True):
            response = self.app.get('/api/tools/config/defaults')

        self.assertEqual(response.status_code, 200)
        configs = json.loads(response.data)

        accurate_lookup = configs['accurate']['lookup_type']
        self.assertIn('ARP_LOOKUP', accurate_lookup)

    def _render_scan_ui(self, scanid):
        uris = [
            '/info',
            f'/?scan_id={scanid}',
            f'/scan/{scanid}/overview',
            f'/scan/{scanid}/table',
            f'/scan/{scanid}/table?filter=test',
            f'/export/{scanid}'
        ]
        for uri in uris:
            response = self.app.get(uri)
            self.assertEqual(response.status_code, 200)

    def test_scan_api(self):
        """
        Test the scan API endpoints
        """
        # Create a new scan
        new_scan = {
            'subnet': right_size_subnet(get_network_subnet()),
            'port_list': 'small',
            'lookup_type': ['POKE_THEN_ARP']
        }
        response = self.app.post('/api/scan', json=new_scan)
        self.assertEqual(response.status_code, 200)
        scan_info = json.loads(response.data)
        self.assertEqual(scan_info['status'], 'running')
        scan_id = scan_info['scan_id']
        self.assertIsNotNone(scan_id)

        percent_complete = 0
        while percent_complete < 100:
            # Get scan summary
            response = self.app.get(f'/api/scan/{scan_id}/summary')
            self.assertEqual(response.status_code, 200)
            summary = json.loads(response.data)
            self.assertTrue(summary['running']
                            or summary['stage'] == 'complete')
            percent_complete = summary['percent_complete']
            self.assertGreaterEqual(percent_complete, 0)
            self.assertLessEqual(percent_complete, 100)
            # Wait for a bit before checking again

            self._render_scan_ui(scan_id)
            time.sleep(2)

        self.assertEqual(summary['running'], False)
        self.assertEqual(summary['stage'], 'complete')
        self.assertGreater(summary['runtime'], 0)

        devices_alive = summary['devices']['alive']
        devices_scanned = summary['devices']['scanned']
        devices_total = summary['devices']['total']

        self.assertEqual(devices_scanned, devices_total)
        self.assertGreater(devices_alive, 0)


if __name__ == '__main__':
    unittest.main()
