class SnakeHitsBoundaryError(Exception):
    def __init__(self):
        super().__init__("Snake hits boundary!")


class SnakeHitsItselfError(Exception):
    def __init__(self):
        super().__init__("Snake hits itself!")


class SnakeSpeedZeroError(Exception):
    def __init__(self):
        super().__init__("Snake speed is set to 0!")


class EggHitsSnakeError(Exception):
    def __init__(self):
        super().__init__("Egg hits snake!")
