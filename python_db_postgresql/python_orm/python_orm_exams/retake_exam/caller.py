import os
import django
from django.db.models import Count

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import TennisPlayer, Match, Tournament


def get_tennis_players(search_name=None, search_country=None):
    if search_name is None and search_country is None:
        return ""

    tennis_players = TennisPlayer.objects.all()

    if search_name:
        tennis_players = tennis_players.filter(full_name__icontains=search_name)

    if search_country:
        tennis_players = tennis_players.filter(country__icontains=search_country)

    tennis_players = tennis_players.order_by('ranking')

    result = [
        f"Tennis Player: {tp.full_name}, country: {tp.country}, ranking: {tp.ranking}"
        for tp in tennis_players
    ]

    return "\n".join(result)


def get_top_tennis_player():
    best_player = TennisPlayer.objects.get_tennis_players_by_wins_count().first()

    if not best_player:
        return ""

    return f"Top Tennis Player: {best_player.full_name} with {best_player.count_wins} wins."


def get_tennis_player_by_matches_count():
    player_with_most_matches = TennisPlayer.objects.annotate(num_matches=Count('matches')
                                                             ).order_by('-num_matches', 'ranking').first()

    if not player_with_most_matches or player_with_most_matches.num_matches == 0:
        return ""

    return f"Tennis Player: {player_with_most_matches.full_name}" \
           f" with {player_with_most_matches.num_matches} matches played."


def get_tournaments_by_surface_type(surface=None):
    if surface is None:
        return ""

    tournaments = Tournament.objects.filter(surface_type__icontains=surface
                                            ).annotate(num_matches=Count('match')
                                                       ).order_by('-start_date')

    if not tournaments:
        return ""

    result = [
        f"Tournament: {t.name}, start date: {t.start_date}, matches: {t.num_matches}"
        for t in tournaments
    ]

    return "\n".join(result)


def get_latest_match_info():
    last_match = Match.objects.prefetch_related('players__match_set__tournament').order_by('date_played').last()

    if not last_match:
        return ""

    player1, player2 = last_match.players.all().order_by('full_name')

    winner = last_match.winner.full_name if last_match.winner else "TBA"

    return f"Latest match played on: {last_match.date_played}," \
           f" tournament: {last_match.tournament.name}, " \
           f"score: {last_match.score}," \
           f" players: {player1} vs {player2}," \
           f" winner: {winner}," \
           f" summary: {last_match.summary}"


def get_matches_by_tournament(tournament_name=None):
    if tournament_name is None:
        return "No matches found."

    tournament = Tournament.objects.filter(name__exact=tournament_name).prefetch_related('match_set').first()

    if not tournament:
        return "No matches found."

    matches = tournament.match_set.all().order_by('-date_played')

    if not matches:
        return "No matches found."

    result = []

    for match in matches:
        winner = match.winner.full_name if match.winner else "TBA"

        result.append(f"Match played on: {match.date_played}, "
                      f"score: {match.score}, "
                      f"winner: {winner}")

    return "\n".join(result)

