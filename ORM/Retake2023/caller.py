import os
import django
from django.db.models import Q, Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import TennisPlayer, Tournament, Match


def get_tennis_players(search_name=None, search_country=None):
    if search_name is None and search_country is None:
        return ""

    query = Q()

    if search_name is not None:
        query &= Q(full_name__icontains=search_name)
    if search_country is not None:
        query &= Q(country__icontains=search_country)

    result = TennisPlayer.objects.filter(
        query
    ).order_by('ranking')

    if not result.exists():
        return ""

    return "\n".join(f"Tennis Player: {p.full_name}, country: {p.country}, ranking: {p.ranking}"
                     for p in result)


def get_top_tennis_player():
    player = TennisPlayer.objects.get_tennis_players_by_wins_count().first()

    if player is None:
        return ""

    return f"Top Tennis Player: {player.full_name} with {player.wins_number} wins."


def get_tennis_player_by_matches_count():
    player = TennisPlayer.objects.annotate(
        matches_played=Count('matches')
    ).order_by(
        '-matches_played',
        'ranking'
    ).first()

    if player is None or player.matches_played == 0:
        return ""

    return f"Tennis Player: {player.full_name} with {player.matches_played} matches played."


def get_tournaments_by_surface_type(surface=None):
    if surface is None:
        return ""

    tournament = Tournament.objects.prefetch_related(
        'matches'
    ).annotate(
        num_matches=Count('matches')
    ).filter(
        surface_type__icontains=surface
    ).order_by('-start_date')

    if not tournament.exists():
        return ""

    return "\n".join(f"Tournament: {t.name}, start date: {t.start_date}, matches: {t.num_matches}"
                     for t in tournament)


def get_latest_match_info():

    last_match = Match.objects.prefetch_related(
        "players"
    ).order_by(
        "-date_played",
        "-id",
    ).first()

    if last_match is None:
        return ""

    players = last_match.players.order_by("full_name")
    player_one = players.first().full_name
    player_two = players.last().full_name
    winner_name = "TBA" if last_match.winner is None else last_match.winner.full_name

    return (f"Latest match played on: {last_match.date_played},"
            f" tournament: {last_match.tournament.name},"
            f" score: {last_match.score},"
            f" players: {player_one} vs {player_two},"
            f" winner: {winner_name}, summary: {last_match.summary}")


def get_matches_by_tournament(tournament_name=None):
    if tournament_name is None:
        return "No matches found."

    matches = Match.objects.select_related('tournament', 'winner') \
        .filter(tournament__name__exact=tournament_name) \
        .order_by('-date_played')

    if not matches:
        return "No matches found."

    return "\n".join(f"Match played on: {match.date_played},"
                     f" score: {match.score},"
                     f" winner: {match.winner.full_name if match.winner else 'TBA'}" for match in matches)
