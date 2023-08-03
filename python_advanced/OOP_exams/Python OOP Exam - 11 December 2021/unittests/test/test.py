from project.team import Team
from unittest import TestCase, main


class TeamTests(TestCase):
    def setUp(self) -> None:
        self.team = Team("MyTeam")

    def test_constructor(self):
        self.assertEqual("MyTeam", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_team_with_invalid_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            Team("Team 5")
        expected_message = "Team Name can contain only letters!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_adding_new_members_to_the_team(self):
        self.assertEqual({}, self.team.members)
        result = self.team.add_member(Player1=20, Player2=21)
        expected_message = "Successfully added: Player1, Player2"
        self.assertEqual(expected_message, result)
        self.assertEqual({"Player1": 20, "Player2": 21}, self.team.members)

        result = self.team.add_member(Player3=22, Player1=20)
        expected_message = "Successfully added: Player3"
        self.assertEqual(expected_message, result)
        self.assertEqual({"Player1": 20, "Player2": 21, "Player3": 22}, self.team.members)


    def test_remove_member_twice(self):
        self.team.add_member(Player1=20, Player2=21)
        self.assertEqual({"Player1": 20, "Player2": 21}, self.team.members)
        result = self.team.remove_member("Player1")
        expected = "Member Player1 removed"
        self.assertEqual(expected, result)
        self.assertEqual({"Player2": 21}, self.team.members)

        result = self.team.remove_member("Player1")
        expected = "Member with name Player1 does not exist"
        self.assertEqual(expected, result)
        self.assertEqual({"Player2": 21}, self.team.members)

    def test_greater_then_method(self):
        other_team = Team("OtherTeam")

        self.team.add_member(Player1=23, Player2=20)
        self.assertEqual({"Player1": 23, "Player2": 20}, self.team.members)

        other_team.add_member(Player3=22)
        self.assertEqual({"Player3": 22}, other_team.members)

        result = self.team > other_team
        self.assertEqual(True, result)

        other_team.add_member(Player4=20, Player5=28)
        self.assertEqual({"Player1": 23, "Player2": 20}, self.team.members)
        self.assertEqual({"Player3": 22, "Player4":20, "Player5": 28}, other_team.members)
        result = self.team > other_team
        self.assertEqual(False, result)

        self.team.add_member(Player6=24)
        self.assertEqual({"Player1": 23, "Player2": 20, "Player6": 24}, self.team.members)
        self.assertEqual({"Player3": 22, "Player4": 20, "Player5": 28}, other_team.members)
        result = self.team > other_team
        self.assertEqual(False, result)

    def test_len_dunder_method(self):
        self.team.add_member(Player1=20, Player2=21)
        self.assertEqual({"Player1": 20, "Player2": 21}, self.team.members)
        result = len(self.team)
        self.assertEqual(2, result)

    def test_add_dunder_method(self):
        self.team.add_member(Player1=20)
        self.assertEqual({"Player1": 20}, self.team.members)

        other_team = Team("OtherTeam")
        other_team.add_member(Player2=21)
        self.assertEqual({"Player2": 21}, other_team.members)

        new_team = self.team + other_team
        self.assertIsInstance(new_team, Team)
        self.assertEqual("MyTeamOtherTeam", new_team.name)
        self.assertEqual({"Player1": 20, "Player2": 21}, new_team.members)

    def test_str_dunder_method(self):
        self.team.add_member(Aivan=21, Petur=23, Bobi=21)
        self.assertEqual({"Aivan": 21, "Petur": 23, "Bobi": 21}, self.team.members)

        result = str(self.team)
        expected = "Team name: MyTeam\n" \
                   "Member: Petur - 23-years old\n" \
                   "Member: Aivan - 21-years old\n" \
                   "Member: Bobi - 21-years old"
        self.assertEqual(expected, result)

if __name__ == "__main__":
    main()
