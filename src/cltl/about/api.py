import abc


class About(abc.ABC):
    def respond(self, statement: str, speaker_name: str = None) -> str:
        raise NotImplementedError("")
