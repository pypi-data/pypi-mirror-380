class GitStarsException(Exception):
    def __init__(self, status_code, message, *args):
        super().__init__(args)
        self.__status_code = status_code
        self.__message = message

    def __str__(self):
        return f"status: {self.__status_code} | message: {self.__message}"
