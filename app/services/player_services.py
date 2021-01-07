from app.models.player import Player
from app.services import contestant_services

def get_all_players():
    """Get all players."""
    return Player.objects

def get_player(player_id):
    """Get single player from id."""
    return Player.objects.get(id=player_id)

def create_player(player_name: str):
    """Create new player."""
    new_player = Player(name=player_name, team=[])
    new_player.save()
    return new_player

def remove_player(player_id):
    """Remove single player."""
    player = get_player(player_id)
    player.delete()

def draft_contestant(player_id, contestant_id):
    """Draft a contestant to a team."""
    player = get_player(player_id)
    contestant = contestant_services.get_contestant(contestant_id)

    contestant.drafted = True
    contestant.save()
    player.team.append(contestant)
    player.save()
