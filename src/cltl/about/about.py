from cltl.about.query import QnA
from random import choice
from cltl.about.api import About


class AboutImpl(About):
    ADDRESS = [
        "Well",
        "You see",
        "See",
        "Look",
        "I'll tell you",
        "Guess what",
        "Ok",
    ]

    ADDRESS_NL = [
        "Tja",
        "Kijk",
        "Dat moet je zo zien",
        "Luister",
        "Ik zeg je",
        "Raad eens",
        "Ok",
        "Dat maakt mijn dag",
        "Wat heb ik nu aan mijn broek.",
        "Dat zit zo"
    ]

    def __init__(self):
        self._qna = QnA()
        self.started = False

    def respond(self, statement: str, speaker_name: str = None, language: str = "nl") -> str:
        if language == "nl":
            result = self._qna.query_nl(statement)
            if result:
                score, answer = result
                say = "{}{} {}".format(choice(self.ADDRESS_NL),
                                       f" {speaker_name}," if speaker_name and not speaker_name == "nl" else " vreemdeling",
                                       answer)
                return say
        else:
            result = self._qna.query(statement)

            if result:
                score, answer = result
                say = "{}{} {}".format(choice(self.ADDRESS), f" {speaker_name}," if speaker_name else " stranger",
                                       answer)
                return say
