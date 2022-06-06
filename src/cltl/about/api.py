import abc


class About(abc.ABC):
    def respond(self, statement: str) -> str:
        raise NotImplementedError("")
