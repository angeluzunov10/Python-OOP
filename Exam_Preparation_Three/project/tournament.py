from projecttest.equipment.elbow_pad import ElbowPad
from projecttest.equipment.knee_pad import KneePad
from projecttest.teams.indoor_team import IndoorTeam
from projecttest.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPES = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad
    }

    VALID_TEAMS = {
        "OutdoorTeam": OutdoorTeam,
        "IndoorTeam": IndoorTeam
    }

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type):
        if equipment_type not in self.VALID_EQUIPMENT_TYPES:
            raise ValueError("Invalid equipment type!")

        equipment = self.VALID_EQUIPMENT_TYPES[equipment_type]()
        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type, team_name, country, advantage):
        if team_type not in self.VALID_TEAMS:
            raise ValueError("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        team = self.VALID_TEAMS[team_type][team_name, country, advantage]
        if team not in self.teams:
            self.teams.append(team)

            return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type, team_name):
        team = next(filter(lambda t: t.name == team_name, self.teams))
        equipment = next(filter(lambda e: e.__class__.__name__ == equipment_type, reversed(self.equipment)))

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        team.equipment.append(equipment)
        team.budget -= equipment.price
        self.equipment.remove(equipment)

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name):
        team = next(filter(lambda t: t.__class__.__name__ == team_name, self.teams), None)

        if team is None:
            raise Exception("No such team!")

        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)

        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type):
        equipment_from_the_same_type = filter(lambda e: e.__class__.__name__ == equipment_type, self.equipment)

        for e in equipment_from_the_same_type:
            e.increase_price()

        return f"Successfully changed {len(equipment_from_the_same_type)}pcs of equipment."

    def play(self, team_name1, team_name2):
        pass

    def get_statistics(self):
        pass