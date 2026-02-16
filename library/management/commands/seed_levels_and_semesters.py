from django.core.management.base import BaseCommand
from library.models import Level, Semester

LEVELS = [
    "ND1",
    "ND2",
    "HND1",
    "HND2",
]

SEMESTERS = [
    "1st Semester",
    "2nd Semester",
]


class Command(BaseCommand):
    help = "Seed academic levels and semesters"

    def handle(self, *args, **kwargs):
        for level in LEVELS:
            Level.objects.get_or_create(name=level)

        for semester in SEMESTERS:
            Semester.objects.get_or_create(name=semester)

        self.stdout.write(self.style.SUCCESS("Levels and semesters loaded successfully"))
