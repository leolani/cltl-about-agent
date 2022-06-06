import unittest

from cltl.about.about import AboutImpl


class TestAbout(unittest.TestCase):
    def setUp(self) -> None:
        self.about = AboutImpl()

    def test_response(self):
        speaker_name = "Piek"
        response = self.about.respond("Tell me a joke", speaker_name)
        print(response)
        self.assertRegex(response, speaker_name)