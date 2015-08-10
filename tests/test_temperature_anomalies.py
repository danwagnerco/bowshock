import unittest
import sys
import os
import httpretty
from bowshock import temperature_anomalies

API_KEY = os.environ["NASA_API_KEY"]

class temperatureAnomalies_UnitTests(unittest.TestCase):

    @httpretty.activate
    def test_ta_address_endpoint_noend(self):
        address = "1800 F Street, NW, Washington DC"
        correct_url = ("http://api.data.gov/nasa/planetary/earth/temperature/"
                       "address?text=1800%20F%20Street,%20NW,"
                       "%20Washington%20DC&begin=1990"
                       "&api_key={api_key}").format(api_key = API_KEY)
        f = "fixtures/ta_address_endpoint_noend.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = temperature_anomalies.address(address=address,
                                          begin="1990")

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)

    @httpretty.activate
    def test_ta_address_endpoint_full(self):
        address = "1800 F Street, NW, Washington DC"
        correct_url = ("http://api.data.gov/nasa/planetary/earth/temperature/"
                       "address?text=1800%20F%20Street,%20NW,"
                       "%20Washington%20DC&begin=1990&end=2000"
                       "&api_key={api_key}").format(api_key = API_KEY)
        f = "fixtures/ta_address_endpoint_full.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = temperature_anomalies.address(address=address,
                                          begin="1990",
                                          end="2000")

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)

    @httpretty.activate
    def test_ta_coordinate_endpoint_noend(self):
        correct_url = ("http://api.data.gov/nasa/planetary/earth/temperature/"
                       "coords?lon=100.75&lat=1.5&begin=1990"
                       "&api_key={api_key}").format(api_key = API_KEY)
        f = "fixtures/ta_coordinate_endpoint_noend.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = temperature_anomalies.coordinate(lon=100.75, lat=1.5, begin="1990")

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)

    @httpretty.activate
    def test_ta_coordinate_endpoint_full(self):
        correct_url = ("http://api.data.gov/nasa/planetary/earth/temperature/"
                       "coords?lon=100.75&lat=1.5&begin=1990&end=2005"
                       "&api_key={api_key}").format(api_key = API_KEY)
        f = "fixtures/ta_coordinate_endpoint_full.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = temperature_anomalies.coordinate(lon=100.75, lat=1.5,
                                             begin="1990", end="2005")

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)


if __name__ == "__main__":
    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(temperatureAnomalies_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
