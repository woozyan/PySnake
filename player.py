class Player(object):
    def __init__(self, player_id):
        self.player_id = player_id
        self.role = None

    def set_role(self, role):
        self.role = role
