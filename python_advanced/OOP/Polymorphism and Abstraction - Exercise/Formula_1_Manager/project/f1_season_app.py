from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    @staticmethod
    def new_team(team_name) -> str:
        return f"{team_name} has joined the new F1 season."

    def register_team_for_season(self, team_name: str, budget: int) -> str:

        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)

            return self.new_team(team_name)

        elif team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)
            return self.new_team(team_name)

        raise ValueError("Invalid team name!")


    def new_race_results(self, race_name, red_bull_pos: int, mercedes_pos: int) -> str:
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception("Not all teams have registered for the season.")

        ahead = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"

        return f"Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}." \
               f" Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}." \
               f" {ahead}" \
               f" is ahead at the {race_name} race."













