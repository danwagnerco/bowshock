import unittest
import httpretty
from bowshock import predictthesky

@unittest.skip("Predictthesky.org API still in development")
class predictthesky_UnitTests(unittest.TestCase):

    @httpretty.activate
    def test_spaceevents_endpoint_latlon(self):
        correct_url = ("http://api.predictthesky.org/events?lon=1.5&lat=100.75")
        f = "fixtures/predictthesky_spaceevents_latlon.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = predictthesky.space_events(lon = 100.75, lat = 1.5)

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)


if __name__ == "__main__":

    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(predictthesky_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
