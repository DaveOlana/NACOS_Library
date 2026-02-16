from django.core.management.base import BaseCommand
from library.models import AcademicState, Level, Semester


class Command(BaseCommand):
    help = "Initialize academic state"

    def handle(self, *args, **kwargs):
        level = Level.objects.get(name="ND1")
        semester = Semester.objects.get(name="1st Semester")

        AcademicState.objects.get_or_create(
            id=1,
            defaults={
                "current_level": level,
                "current_semester": semester
            }
        )

        self.stdout.write(self.style.SUCCESS("Academic state initialized"))
