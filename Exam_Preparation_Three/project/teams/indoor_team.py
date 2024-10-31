from projecttest.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    INITIAL_BUDGET = 500.0

    def __init__(self, name, country, advantage):
        super().__init__(name, country, advantage, IndoorTeam.INITIAL_BUDGET)

    def win(self):
        self.advantage += 145
        self.wins += 1
