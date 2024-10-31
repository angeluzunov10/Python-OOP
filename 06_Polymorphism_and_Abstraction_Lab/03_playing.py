class Guitar:
    @staticmethod
    def play():
        return "Playing the guitar"


guitar = Guitar()


def start_playing(obj):
    return obj.play()


print(start_playing(guitar))
