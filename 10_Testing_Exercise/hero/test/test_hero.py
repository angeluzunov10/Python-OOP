from unittest import TestCase, main

from project1.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.fighter = Hero("fighter", 1, 100, 100)
        self.enemy = Hero("enemy", 1, 50, 50)

    def test_correct_init(self):
        self.assertEqual("fighter", self.fighter.username)
        self.assertEqual(1, self.fighter.level)
        self.assertEqual(100, self.fighter.health)
        self.assertEqual(100, self.fighter.damage)

    def test_starting_battle_between_two_same_usernames_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.fighter.battle(self.fighter)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_starting_battle_when_your_health_is_zero_raises_value_error(self):
        self.fighter.health = 0
        with self.assertRaises(ValueError) as ve:
            self.fighter.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))
        
    def test_starting_battle_when_enemy_has_zero_health_raises_value_error(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.fighter.battle(self.enemy)

        self.assertEqual("You cannot fight enemy. He needs to rest", str(ve.exception))

    def test_ending_battle_when_both_heroes_have_zero_health_after_fight_returns_draw(self):
        self.fighter.health = 50
        result = self.fighter.battle(self.enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(-50, self.enemy.health)
        self.assertEqual(0, self.fighter.health)

    def test_ending_battle_when_enemy_has_zero_health_after_fight_returns_you_are_winner_and_stats_increase(self):
        expected_level = self.fighter.level + 1
        expected_damage = self.fighter.damage + 5
        expected_health = self.fighter.health - self.enemy.damage + 5

        result = self.fighter.battle(self.enemy)

        self.assertEqual("You win", result)
        self.assertEqual(expected_level, self.fighter.level)
        self.assertEqual(expected_health, self.fighter.health)
        self.assertEqual(expected_damage, self.fighter.damage)

    def test_ending_battle_when_enemy_beats_me_after_fight_returns_you_are_loosing_and_stats_of_enemy_increases(self):
        self.fighter, self.enemy = self.enemy, self.fighter

        expected_level = self.enemy.level + 1
        expected_damage = self.enemy.damage + 5
        expected_health = self.enemy.health - self.fighter.damage + 5

        result = self.fighter.battle(self.enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(expected_level, self.enemy.level)
        self.assertEqual(expected_health, self.enemy.health)
        self.assertEqual(expected_damage, self.enemy.damage)

    def test_correct_str(self):
        self.assertEqual("Hero fighter: 1 lvl\n"
                         "Health: 100\n"
                         "Damage: 100\n", self.fighter.__str__())

if __name__ == '__main__':
    main()
