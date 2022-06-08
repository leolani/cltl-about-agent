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

    def __init__(self):
        self._qna = QnA()
        self.started = False


    def respond(self, statement: str, speaker_name: str = None) -> str:
        result = self._qna.query(statement)

        if result:
            score, answer = result
            say = "{}{} {}".format(choice(self.ADDRESS), f" {speaker_name}," if speaker_name else "", answer)
            return say
