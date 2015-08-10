import unittest
import sys
import httpretty
from time import sleep
from bowshock import techport


class techport_UnitTests(unittest.TestCase):

    @httpretty.activate
    def test_techport_api(self):
        correct_url = "http://techport.nasa.gov/xml-api/4795"
        f = "fixtures/techport_endpoint.xml"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = techport.techport(Id="4795")

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)


if __name__ == "__main__":

    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(techport_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
