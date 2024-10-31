from project1.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        self.players.append(player)
        if player.guild != "Unaffiliated":
            if player.guild == self.name:
                return f"Player {player.name} is already in the guild."

            return f"Player {player.name} is in another guild."

        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                player.guild = "Unaffiliated"
                self.players.remove(player)

                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        message = f"Guild: {self.name}\n"
        for p in self.players:
            message += "\n".join(p.player_info() for p in self.players)

        return message


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
