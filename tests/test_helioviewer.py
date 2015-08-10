import unittest
import sys
import httpretty
from bowshock import helioviewer

class helioviewer_UnitTests(unittest.TestCase):
    @httpretty.activate
    def test_helioviewer_getjp2image_without_sourceId(self):
        correct_url = ("http://helioviewer.org/api/v1/getJP2Image/"
                       "?date=2014-01-01T23:59:59Z"
                       "&observatory=SDO&instrument=AIA&detector=AIA"
                       "&measurement=335&jpip=true")
        correct_body = ("jpip://helioviewer.org:8090/AIA/2014/01/02/335/"
                        "2014_01_02__00_00_02_62__SDO_AIA_AIA_335.jp2")

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = helioviewer.getjp2image(date="2014-01-01T23:59:59",
                                    observatory="SDO",
                                    instrument="AIA",
                                    detector="AIA",
                                    measurement="335")

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)

    @httpretty.activate
    def test_helioviewer_getpy2image_with_sourceId(self):
        correct_url = ("http://helioviewer.org/api/v1/getJP2Image/"
                       "?date=2014-01-01T23:59:59Z"
                       "&sourceId=14&jpip=true")
        correct_body = ("jpip://helioviewer.org:8090/AIA/2014/01/02/335/"
                        "2014_01_02__00_00_02_62__SDO_AIA_AIA_335.jp2")

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = helioviewer.getjp2image(date="2014-01-01T23:59:59",
                                    sourceId=14)

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)

    @httpretty.activate
    def test_helioviewer_getjp2header(self):
        correct_url = ("http://helioviewer.org/api/v1/getJP2Header/"
                       "?id=7654321")
        f = "fixtures/helioviewer_getjp2header.xml"
        with open(f) as fixture:
            correct_body = fixture.read()

        httpretty.register_uri(httpretty.GET,
                               correct_url,
                               body = correct_body)

        r = helioviewer.getjp2header(Id=7654321)

        self.assertEqual(r.url, correct_url)
        self.assertEqual(r.text, correct_body)


if __name__ == "__main__":

    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(helioviewer_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
