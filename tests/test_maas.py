import unittest
import httpretty
from freezegun import freeze_time
from bowshock import maas

class maas_UnitTests(unittest.TestCase):

    @httpretty.activate
    @freeze_time("2015-07-05") # <~ closest obs at this time was 2015-07-02
    def test_maas_latest_endpoint(self):
        correct_url = ("http://marsweather.ingenology.com/v1/latest/")
        f = "fixtures/maas_latest.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = maas.maas_latest()

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)

    @httpretty.activate
    def test_maas_archive_endpoint_w_dates(self):
        correct_url = ("http://marsweather.ingenology.com/v1/archive/"
                       "?terrestrial_date_start=2012-10-01"
                       "&terrestrial_date_end=2012-10-31")
        f = "fixtures/maas_archive_w_dates.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = maas.maas_archive("2012-10-01", "2012-10-31")

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)


if __name__ == "__main__":
    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(maas_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
