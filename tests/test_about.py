import unittest

from cltl.about.about import AboutImpl


class TestAbout(unittest.TestCase):
    def setUp(self) -> None:
        self.about = AboutImpl()

    def test_response(self):
        speaker_name = "Piek"
        response = self.about.respond("Tell me a joke", speaker_name)
        self.assertRegex(response, f" {speaker_name}")