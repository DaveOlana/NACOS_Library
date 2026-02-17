from django.db import transaction
from .models import AcademicState, StudentProfile, Level


def advance_academic_state():
    """
    Moves the institution forward by one academic step.

    Rules:
    - 1st → 2nd semester: only semester changes
    - 2nd → 1st semester: semester resets and all students advance one level
    """

    state = AcademicState.objects.first()

    if state.current_semester == "1":
        state.current_semester = "2"
        state.save()
        return "Semester advanced to 2nd semester."

    # We are in 2nd semester → roll over
    next_levels = {
        "ND1": "ND2",
        "ND2": "HND1",
        "HND1": "HND2",
    }

    with transaction.atomic():
        for student in StudentProfile.objects.select_related("level"):
            current = student.level.name

            if current in next_levels:
                student.level = Level.objects.get(name=next_levels[current])
                student.save()

        state.current_semester = "1"
        state.save()

    return "New academic session started. Students promoted."


def rollback_academic_state():
    """
    Safely reverts the last academic move.
    Used when an admin advances by mistake.
    """

    state = AcademicState.objects.first()

    if state.current_semester == "2":
        state.current_semester = "1"
        state.save()
        return "Reverted back to 1st semester."

    previous_levels = {
        "ND2": "ND1",
        "HND1": "ND2",
        "HND2": "HND1",
    }

    with transaction.atomic():
        for student in StudentProfile.objects.select_related("level"):
            current = student.level.name

            if current in previous_levels:
                student.level = Level.objects.get(name=previous_levels[current])
                student.save()

        state.current_semester = "2"
        state.save()

    return "Reverted to previous academic session."
