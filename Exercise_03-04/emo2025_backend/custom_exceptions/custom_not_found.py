class CustomNotFound(Exception):
    def __init__(self, message='Not found'):
        super(CustomNotFound, self).__init__(message)
        self.message = message

