import unittest
import os
import httpretty
from freezegun import freeze_time
from bowshock import earth

API_KEY = os.environ["NASA_API_KEY"]

class earth_UnitTests(unittest.TestCase):

    @httpretty.activate
    def test_imagery_endpoint_full(self):
        correct_url = ("http://api.data.gov/nasa/planetary/earth/imagery?"
                       "lon=100.75&lat=1.5&dim=1.5&date=2015-02-02"
                       "&cloud_score=True&"
                       "api_key={api_key}").format(api_key = API_KEY)
        f = "fixtures/earth_imagery_endpoint_full.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = earth.imagery(lon=100.75,
                          lat=1.5,
                          dim=1.5,
                          date="2015-02-02",
                          cloud_score=True)

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)

    @httpretty.activate
    def test_imagery_endpoint_nodim(self):
        correct_url = ("http://api.data.gov/nasa/planetary/earth/imagery?"
                       "lon=100.75&lat=1.5&date=2015-02-02&cloud_score=True"
                       "&api_key={api_key}").format(api_key = API_KEY)
        f = "fixtures/earth_imagery_endpoint_nodim.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = earth.imagery(lon=100.75,
                          lat=1.5,
                          date="2015-02-02",
                          cloud_score=True)

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)

    @httpretty.activate
    def test_imagery_endpoint_nocloudscore(self):
        correct_url = ("http://api.data.gov/nasa/planetary/earth/imagery?"
                       "lon=100.75&lat=1.5&date=2015-02-02"
                       "&api_key={api_key}").format(api_key = API_KEY)
        f = "fixtures/earth_imagery_endpoint_nocloudscore.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = earth.imagery(lon=100.75, lat=1.5, date="2015-02-02")

        self.assertEqual(r.url, correct_url)
        print(r.text)
        self.assertEqual(r.text, correct_body)

    @httpretty.activate
    @freeze_time("2015-07-04") # <~ the closest image to this date was on 6/15
    def test_imagery_endpoint_nodate(self):
        correct_url = ("http://api.data.gov/nasa/planetary/earth/imagery?"
                       "lon=100.75&lat=1.5"
                       "&api_key={api_key}").format(api_key = API_KEY)
        f = "fixtures/earth_imagery_endpoint_nodate.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = earth.imagery(lon=100.75, lat=1.5)

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)

    @httpretty.activate
    @freeze_time("2015-07-04") # <~ a real call on this day brings back 8
    def test_assets_endpoint_noenddate(self):
        correct_url = ("http://api.data.gov/nasa/planetary/earth/assets?"
                       "lon=100.75&lat=1.5&begin=2015-02-02"
                       "&api_key={api_key}").format(api_key = API_KEY)
        f = "fixtures/earth_assets_endpoint_noenddate.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = earth.assets(lon=100.75, lat=1.5, begin="2015-02-02")

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)

    @httpretty.activate
    def test_assets_endpoint_full(self):
        correct_url = ("http://api.data.gov/nasa/planetary/earth/assets?"
                       "lon=100.75&lat=1.5&begin=2015-02-02&end=2015-02-10"
                       "&api_key={api_key}").format(api_key = API_KEY)
        f = "fixtures/earth_assets_endpoint_full.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = earth.assets(lon=100.75,
                         lat=1.5,
                         begin="2015-02-02",
                         end="2015-02-10")

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)


if __name__ == "__main__":

    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(earth_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
