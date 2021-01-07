from app.models.contestants import Contestant


def get_all_contestants():
    """Get all contestants."""
    return Contestant.objects


def get_contestant(contestant_id):
    """Get single contestant from id."""
    return Contestant.objects.get(id=contestant_id)


def draft_contestant(contestant_id):
    """Set drafted status of contestant to true."""
    contestant = get_contestant(contestant_id)
    contestant.drafted = True
    contestant.save()


def reset_draft_status(contestant_id):
    """Set drafted status of contestant to false."""
    contestant = get_contestant(contestant_id)
    contestant.drafted = False
    print(contestant)
    contestant.save()


def reset_all_draft_statuses():
    """Reset all contestant draft statuses to false."""
    contestants = get_all_contestants()
    for contestant in contestants:
        print(contestant)
        # TODO: Fix error occuring on following line: Contestant has no field _id
        #       look to see if _id is addressed anywhere else, maybe add _id to Contestant model.
        reset_draft_status(contestant._id)


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


def subtract_rose(contestant_id):
    """Decrease roses of contestant by one."""
    contestant = get_contestant(contestant_id)
    contestant.roses -= 1
    contestant.save()
