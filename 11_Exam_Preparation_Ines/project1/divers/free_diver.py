from project1.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 120

    def __init__(self, name):
        super().__init__(name, FreeDiver.INITIAL_OXYGEN_LEVEL)

    def miss(self, time_to_catch):
        reduce_amount = time_to_catch * 0.6

        if (self.oxygen_level - reduce_amount) < 0:
            self.oxygen_level = 0
            self.has_health_issue = True
        else:
            self.oxygen_level -= reduce_amount
            if self.oxygen_level == 0:
                self.has_health_issue = True
            self.oxygen_level = float(self.oxygen_level)

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN_LEVEL
