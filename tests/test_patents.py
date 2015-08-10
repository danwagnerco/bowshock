import unittest
import os
import httpretty
from bowshock import patents

API_KEY = os.environ["NASA_API_KEY"]

class patents_UnitTests(unittest.TestCase):

    @httpretty.activate
    def test_patents_endpoint_full(self):
        correct_url = ("http://api.data.gov/nasa/patents/content?"
                       "query=temperature&concept_tags=True"
                       "&limit=5&api_key={api_key}").format(api_key = API_KEY)
        f = "fixtures/patents_endpoint_full.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = patents.patents(query = "temperature",
                            concept_tags = True,
                            limit = 5)

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)

    @httpretty.activate
    def test_patents_endpoint_notags(self):
        correct_url = ("http://api.data.gov/nasa/patents/content?"
                       "query=temperature&limit=5"
                       "&api_key={api_key}").format(api_key = API_KEY)
        f = "fixtures/patents_endpoint_notags.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = patents.patents(query = "temperature", limit = 5)

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)

    @httpretty.activate
    def test_patents_endpoint_nolimit(self):
        correct_url = ("http://api.data.gov/nasa/patents/content?"
                       "query=temperature"
                       "&api_key={api_key}").format(api_key = API_KEY)
        f = "fixtures/patents_endpoint_nolimit.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = patents.patents(query = "temperature")

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)


if __name__ == "__main__":

    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(patents_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
