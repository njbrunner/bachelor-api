import logging
from app.models.contestants import Contestant


def get_all_contestants():
    """Get all contestants."""
    contestants = Contestant.objects
    return sorted(contestants, key=lambda x: x.active, reverse=True)


def get_contestant(contestant_id):
    """Get single contestant from id."""
    return Contestant.objects.get(pk=contestant_id)


def draft_contestant(contestant_id):
    """Set drafted status of contestant to true."""
    contestant = get_contestant(contestant_id)
    contestant.drafted = True
    contestant.save()


def reset_draft_status(contestant_id):
    """Set drafted status of contestant to false."""
    contestant = get_contestant(contestant_id)
    contestant.drafted = False
    contestant.save()


def reset_all_draft_statuses():
    """Reset all contestant draft statuses to false."""
    contestants = get_all_contestants()
    for contestant in contestants:
        reset_draft_status(contestant.pk)


def deactivate_contestant(contestant_id):
    """Set active status of contestant to false."""
    contestant = get_contestant(contestant_id)
    contestant.active = False
    contestant.save()


def add_rose(contestant_id):
    """Increase roses of contestant by one."""
    contestant = get_contestant(contestant_id)
    contestant.roses += 1
    contestant.save()


def add_rose_to_all_active():
    """Increase roses of all active contestants by one."""
    contestants = get_all_contestants()
    for contestant in contestants:
        if contestant.active:
            add_rose(contestant.pk)


def subtract_rose(contestant_id):
    """Decrease roses of contestant by one."""
    contestant = get_contestant(contestant_id)
    contestant.roses -= 1
    contestant.save()


def subtract_rose_from_all_active():
    """Decrease roses of all active contestants by one."""
    contestants = get_all_contestants()
    for contestant in contestants:
        if contestant.active:
            subtract_rose(contestant.pk)
