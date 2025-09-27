"""
Integration tests for core library components of the LANscape application.
Tests scan configuration, network discovery, and subnet selection functionality.
"""

import unittest

from lanscape.libraries.net_tools import smart_select_primary_subnet
from lanscape.libraries.subnet_scan import ScanManager
from lanscape.libraries.scan_config import ScanConfig, ScanType

from ._helpers import right_size_subnet

sm = ScanManager()


class LibraryTestCase(unittest.TestCase):
    """
    Test cases for the core library functionality including scan configuration
    and network discovery capabilities.
    """

    def test_scan_config(self):
        """
        Test the ScanConfig class serialization and deserialization functionality.
        Verifies that configs can be properly converted to and from dictionaries.
        """
        subnet_val = '192.168.1.1/24'
        do_port_scan = False
        ping_attempts = 3
        arp_timeout = 2.0

        cfg = ScanConfig(
            subnet=subnet_val,
            port_list='small',
        )
        self.assertEqual(len(cfg.parse_subnet()), 254)

        cfg.task_scan_ports = do_port_scan
        cfg.ping_config.attempts = ping_attempts
        cfg.arp_config.timeout = arp_timeout
        cfg.lookup_type = [ScanType.POKE_THEN_ARP]

        data = cfg.to_dict()
        self.assertTrue(isinstance(data['ping_config'], dict))
        self.assertTrue(isinstance(data['arp_config'], dict))

        cfg2 = ScanConfig.from_dict(data)

        # ensure the config was properly converted back
        self.assertEqual(cfg2.subnet, subnet_val)
        self.assertEqual(cfg2.port_list, 'small')
        self.assertEqual(cfg2.task_scan_ports, do_port_scan)
        self.assertEqual(cfg2.ping_config.attempts, ping_attempts)
        self.assertEqual(cfg2.arp_config.timeout, arp_timeout)
        self.assertEqual(cfg2.lookup_type, [ScanType.POKE_THEN_ARP])

    def test_scan(self):
        """
        Test the network scanning functionality with a dynamically selected subnet.
        Verifies that devices can be discovered and that scan results are valid.
        """
        subnet = smart_select_primary_subnet()
        self.assertIsNotNone(subnet)
        cfg = ScanConfig(
            subnet=right_size_subnet(subnet),
            t_multiplier=1.0,
            port_list='small',
            lookup_type=[ScanType.POKE_THEN_ARP]
        )
        scan = sm.new_scan(cfg)
        self.assertTrue(scan.running)
        sm.wait_until_complete(scan.uid)

        self.assertFalse(scan.running)

        # ensure there are not any remaining running threads
        self.assertDictEqual(scan.job_stats.running, {})

        cnt_with_hostname = 0
        ips = []
        macs = []
        for d in scan.results.devices:
            if d.hostname:
                cnt_with_hostname += 1
            # ensure there arent dupe mac addresses

            if d.get_mac() in macs:
                print(f"Warning: Duplicate MAC address found: {d.get_mac()}")
            macs.append(d.get_mac())

            # ensure there arent dupe ips
            self.assertNotIn(d.ip, ips)
            ips.append(d.ip)

            # device must be alive to be in this list
            self.assertTrue(d.alive)

        # find at least one device
        self.assertGreater(len(scan.results.devices), 0)

        # ensure everything got scanned
        self.assertEqual(scan.results.devices_scanned,
                         scan.results.devices_total)
