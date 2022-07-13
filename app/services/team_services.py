import logging
import random
import copy
from app.models.team import Team
from app.services import contestant_services


def get_all_teams():
    """Get all Teams."""
    teams = Team.objects
    return sorted(teams, key=lambda x: x.draft_position)


def get_team(team_id):
    """Get single team from id."""
    return Team.objects.get(pk=team_id)


def create_team(team_name: str, owner: str):
    """Create new team."""
    new_team = Team(name=team_name, owner=owner, team_members=[], draft_position=0)
    new_team.save()
    return new_team


def remove_team(team_id):
    """Remove single team."""
    team = get_team(team_id)
    team.delete()


def draft_contestant(team_id, contestant_id):
    """Draft a contestant to a team."""
    team = get_team(team_id)
    contestant = contestant_services.get_contestant(contestant_id)
    contestant.drafted = True
    contestant.save()
    team.team.append(contestant)
    team.save()


def remove_drafted_contestants(team_id):
    """Remove all contestants from team's team."""
    team = get_team(team_id)
    team.team_members = []
    team.save()


def remove_all_drafted_contestants():
    """Remove all contestants from all teams."""
    teams = get_all_teams()
    for team in teams:
        remove_drafted_contestants(team.pk)


def shuffle_teams():
    """Set random draft positions for each team."""
    teams = get_all_teams()
    available_teams = copy.deepcopy(teams)
    for x in range(len(teams)):
        team = random.choice(available_teams)
        available_teams.remove(team)
        team.draft_position = x
        team.save()
