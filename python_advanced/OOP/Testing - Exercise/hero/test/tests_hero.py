from project.hero import Hero
from unittest import TestCase, main


class HeroTests(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Username", 60, 250.0, 5.5)
        self.enemy_hero = Hero("Enemy Hero", 50, 240.0, 4.5)

    def test_correct_initializing(self):
        self.assertEqual("Username", self.hero.username)
        self.assertEqual(60, self.hero.level)
        self.assertEqual(50.0, self.hero.health)
        self.assertEqual(5.5, self.hero.damage)

    def test_battle_fighting_same_hero_raises(self):
        self.enemy_hero.username = "Username"

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)
        expected_message = "You cannot fight yourself"
        self.assertEqual(expected_message, str(ex.exception))

    def test_battle_with_no_health_left_raises(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)

        expected_message = "Your health is lower than or equal to 0. You need to rest"
        self.assertEqual(expected_message, str(ex.exception))

    def test_battle_with_enemy_has_no_health_raises(self):
        self.enemy_hero.health = 0

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)

        expected_message = "You cannot fight Enemy Hero. He needs to rest"
        self.assertEqual(expected_message, str(ex.exception))

    def test_draw_battle(self):
        first_hero = Hero("First hero", 50, 250, 5)
        second_hero = Hero("Second hero", 50, 250, 5)

        result = first_hero.battle(second_hero)

        self.assertEqual(0, first_hero.health)
        self.assertEqual(0, second_hero.health)
        self.assertEqual("Draw", result)

    def test_hero_win_in_battle(self):
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(61, self.hero.level)
        self.assertEqual(30, self.hero.health)
        self.assertEqual(10.5, self.hero.damage)
        self.assertEqual("You win", result)

    def test_hero_lose_in_battle(self):
        result = self.enemy_hero.battle(self.hero)
        self.assertEqual(61, self.hero.level)
        self.assertEqual(30, self.hero.health)
        self.assertEqual(10.5, self.hero.damage)
        self.assertEqual("You lose", result)

    def test_string_method_return_correct_message(self):
        result = str(self.hero)
        expected = f"Hero Username: 60 lvl\n" \
               f"Health: 250.0\n" \
               f"Damage: 5.5\n"

        self.assertEqual(expected, result)



if __name__ == "__main__":
    main()