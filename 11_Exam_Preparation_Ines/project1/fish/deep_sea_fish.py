from project1.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):
    def __init__(self, name, points):
        super().__init__(name, points, 180)

    def fish_details(self):
        return f"{self.__class__.__name__}: {self.name} [Points: {self.points}, " \
               f"Time to Catch: {self.time_to_catch} seconds]"
