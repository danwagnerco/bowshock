import unittest
import httpretty
from collections import OrderedDict
from bowshock import asterank

class asterank_UnitTests(unittest.TestCase):

    @httpretty.activate
    def test_asterank_endpoint_full(self):
        correct_url = ("http://asterank.com/api/asterank?query=%7B"
                       "%22a%22:%20%7B%22$lt%22:%201.5%7D,%20"
                       "%22e%22:%20%7B%22$lt%22:%200.1%7D,%20"
                       "%22i%22:%20%7B%22$lt%22:%204%7D%7D&limit=1")
        f = "fixtures/asterank_endpoint_full.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        ordered_q = OrderedDict()
        ordered_q["a"] = {"$lt": 1.5}
        ordered_q["e"] = {"$lt": 0.1}
        ordered_q["i"] = {"$lt": 4}

        r = asterank.asterank(query=ordered_q, limit=1)

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)


if __name__ == "__main__":

    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(asterank_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
