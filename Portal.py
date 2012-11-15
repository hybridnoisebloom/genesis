# Portal.py controls the dimensions and such.

class Portal:
    def teleport(self, player_object, dimension):
        if dimension == "Hell":
            player_object.dimension = "Hell"
        elif dimension == "Sky":
            player_object.dimension = "Sky Dimension"
        elif dimension == "Base":
            player_object.dimension = "Base"
        else:
            return None
