import random
import copy
from app.models.player import Player
from app.services import contestant_services


def get_all_players():
    """Get all players."""
    players = Player.objects
    return sorted(players, key=lambda x: x.draft_position)


def get_player(player_id):
    """Get single player from id."""
    return Player.objects.get(_id=player_id)


def create_player(player_name: str):
    """Create new player."""
    new_player = Player(name=player_name, team=[], draft_position=0)
    new_player.save()
    return new_player


def remove_player(player_id):
    """Remove single player."""
    player = get_player(player_id)
    player.delete()


def draft_contestant(player_id, contestant_id):
    """Draft a contestant to a player."""
    player = get_player(player_id)
    contestant = contestant_services.get_contestant(contestant_id)
    contestant.drafted = True
    contestant.save()
    player.team.append(contestant)
    player.save()


def remove_drafted_contestants(player_id):
    """Remove all contestants from player team."""
    player = get_player(player_id)
    player.team = []
    player.save()


def remove_all_drafted_contestants():
    """Remove all contestants from all players."""
    players = get_all_players()
    for player in players:
        remove_drafted_contestants(player._id)


def shuffle_players():
    """Set random draft positions for each player."""
    players = get_all_players()
    available_players = copy.deepcopy(players)
    for x in range(len(players)):
        player = random.choice(available_players)
        available_players.remove(player)
        player.draft_position = x
        player.save()
