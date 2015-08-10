import unittest
import httpretty
from bowshock import skymorph

class skymorph_UnitTests(unittest.TestCase):

    @httpretty.activate
    def test_skymorph_object_search(self):
        correct_url = ("http://asterank.com/api/skymorph/search?"
                       "target=J99TS7A")
        f = "fixtures/skymorph_object_search.json"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = skymorph.search_target_obj("J99TS7A")

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)


if __name__ == "__main__":
    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(skymorph_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
