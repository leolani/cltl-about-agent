import abc


class About(abc.ABC):
    def respond(self, statement: str, speaker_name: str = None, language: str = "nl") -> str:
        raise NotImplementedError("")
