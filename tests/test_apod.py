import unittest
import os
import httpretty
from freezegun import freeze_time
from bowshock import apod

API_KEY = os.environ["NASA_API_KEY"]

class apod_UnitTests(unittest.TestCase):

    @httpretty.activate
    def test_apod_endpoint_full(self):
        correct_url = ("http://api.data.gov/nasa/planetary/apod?"
                       "date=2015-02-02&concept_tags=True&"
                       "api_key={api_key}").format(api_key = API_KEY)
        f = "fixtures/apod_endpoint_full.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = apod.apod(date="2015-02-02", concept_tags=True)

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)

    @httpretty.activate
    def test_apod_endpoint_notags(self):
        correct_url = ("http://api.data.gov/nasa/planetary/apod?"
                       "date=2015-02-02&"
                       "api_key={api_key}").format(api_key = API_KEY)
        f = "fixtures/apod_endpoint_notags.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = apod.apod(date="2015-02-02")

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)

    @freeze_time("2015-06-16") # <~ the 20th anniversary of APOD
    @httpretty.activate
    def test_apod_endpoint_noargs(self):
        # no tags should pass, as no date defaults to today
        correct_url = ("http://api.data.gov/nasa/planetary/apod?"
                       "api_key={api_key}").format(api_key = API_KEY)
        f = "fixtures/apod_endpoint_noargs.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = apod.apod()

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)


if __name__ == "__main__":

    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(apod_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
