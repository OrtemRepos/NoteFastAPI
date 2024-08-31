class MissingException(Exception):
    def __init__(self, message: str):
        self.msg = message


class DuplicateException(Exception):
    def __init__(self, message: str):
        self.msg = message
