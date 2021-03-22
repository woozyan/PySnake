class SnakeHitsBoundaryError(Exception):
    def __init__(self, message):
        super().__init__(message)


class SnakeHitsItselfError(Exception):
    def __init__(self, message):
        super().__init__(message)


class EggHitsSnakeError(Exception):
    def __init__(self, message):
        super().__init__(message)


class SnakeEatsEggError(Exception):
    def __init__(self, message):
        super().__init__(message)
