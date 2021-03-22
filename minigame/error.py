class SnakeHitsBoundaryError(Exception):
    def __init__(self, message):
        super().__init__(message)


class SnakeHitsItselfError(Exception):
    def __init__(self, message):
        super().__init__(message)
