import unittest
import sys
import httpretty
from bowshock import star


class star_UnitTests(unittest.TestCase):

    @httpretty.activate
    def test_stars(self):
        correct_url = "http://star-api.herokuapp.com/api/v1/stars"
        f = "fixtures/star_stars_endpoint.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = star.stars()

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)

    @httpretty.activate
    def test_search_star(self):
        correct_url = "http://star-api.herokuapp.com/api/v1/stars/Sun"
        f = "fixtures/star_search_star_endpoint.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = star.search_star("Sun")

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)

    @httpretty.activate
    def test_exoplanets(self):
        correct_url = "http://star-api.herokuapp.com/api/v1/exo_planets"
        f = "fixtures/star_exoplanets_endpoint.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = star.exoplanets()

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)

    @httpretty.activate
    def test_search_exoplanet(self):
        correct_url = ("http://star-api.herokuapp.com/api/v1/"
                       "exo_planets/11%20Com")
        f = "fixtures/star_search_exoplanets_endpoint.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = star.search_exoplanet("11 Com")

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)

    @httpretty.activate
    def test_local_group_of_galaxies(self):
        correct_url = "http://star-api.herokuapp.com/api/v1/local_groups"
        f = "fixtures/star_local_group_of_galaxies_endpoint.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = star.local_group_of_galaxies()

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)

    @httpretty.activate
    def test_search_local_galaxies(self):
        correct_url = ("http://star-api.herokuapp.com/api/v1/"
                       "local_groups/IC%2010")
        f = "fixtures/star_search_local_galaxies_endpoint.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = star.search_local_galaxies("IC 10")

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)

    @httpretty.activate
    def test_star_clusers(self):
        correct_url = "http://star-api.herokuapp.com/api/v1/open_cluster"
        f = "fixtures/star_star_clusers_endpoint.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = star.star_clusters()

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)

    @httpretty.activate
    def test_search_star_clusters(self):
        correct_url = ("http://star-api.herokuapp.com/api/v1/"
                       "open_cluster/Berkeley%2059")
        f = "fixtures/star_search_star_clusters_endpoint.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = star.search_star_cluster("Berkeley 59")

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)


if __name__ == "__main__":

    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(star_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
