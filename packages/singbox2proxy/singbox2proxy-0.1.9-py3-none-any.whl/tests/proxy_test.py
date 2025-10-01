from singbox2proxy import SingBoxProxy
import unittest
import os


TEST_LINK = os.environ.get("TEST_SINGBOX_LINK")


@unittest.skipIf(not TEST_LINK, "TEST_SINGBOX_LINK environment variable not set")
class TestSingBoxFetch(unittest.TestCase):
    def test_pick_unused_port(self):
        port = SingBoxProxy._pick_unused_port()
        self.assertIsNotNone(port)

    def test_proxy_client(self):
        proxy = SingBoxProxy(TEST_LINK)
        ip = proxy.get("https://api.ipify.org?format=json").json()
        self.assertIsNotNone(ip)
        self.assertIn("ip", ip)


if __name__ == "__main__":
    unittest.main()
