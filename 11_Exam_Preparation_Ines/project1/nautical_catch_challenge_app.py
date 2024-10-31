from project1.divers.free_diver import FreeDiver
from project1.divers.scuba_diver import ScubaDiver
from project1.fish.deep_sea_fish import DeepSeaFish
from project1.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVER_TYPES = {
        "FreeDiver": FreeDiver,
        "ScubaDiver": ScubaDiver,
    }

    VALID_FISH_TYPES = {
        "PredatoryFish": PredatoryFish,
        "DeepSeaFish": DeepSeaFish,
    }

    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type, diver_name):
        try:
            diver = self.VALID_DIVER_TYPES[diver_type](diver_name)
        except KeyError:
            return f"{diver_type} is not allowed in our competition."

        try:
            next(filter(lambda d: d.name == diver_name, self.divers))
            return f"{diver_name} is already a participant."
        except StopIteration:
            self.divers.append(diver)
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type, fish_name, points):
        try:
            fish = self.VALID_FISH_TYPES[fish_type](fish_name, points)
        except KeyError:
            return f"{fish_type} is forbidden for chasing in our competition."

        try:
            next(filter(lambda f: f.name == fish_name, self.fish_list))
            return f"{fish_name} is already permitted."
        except StopIteration:
            self.fish_list.append(fish)
            return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name, fish_name, is_lucky):
        try:
            diver = next(filter(lambda d: d.name == diver_name, self.divers))
        except StopIteration:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = next(filter(lambda f: f.name == fish_name, self.fish_list))
        except StopIteration:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."
        else:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        divers_with_health_issues = [d for d in self.divers if d.has_health_issue]

        for diver in divers_with_health_issues:
            diver.has_health_issue = False
            diver.renew_oxy()

        return f"Divers recovered: {len(divers_with_health_issues)}"

    def diver_catch_report(self, diver_name):
        diver = [d for d in self.divers if d.name == diver_name][0]

        result = f"**{diver_name} Catch Report**\n"

        result += "\n".join(f.fish_details() for f in diver.catch)

        return result

    def competition_statistics(self):
        sorted_divers = sorted(self.divers, key =lambda d: (-d.competition_points, -(len(d.catch)), d.name))

        healthy_divers = [d for d in sorted_divers if not d.has_health_issue]

        result = "**Nautical Catch Challenge Statistics**\n"

        result += '\n'.join(str(d) for d in healthy_divers)

        return result
