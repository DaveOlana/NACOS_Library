from django.core.management.base import BaseCommand
from library.models import School, Department

YABATECH_STRUCTURE = {
    "School of Art, Design & Printing": [
        "Fine Art",
        "Industrial Design",
        "Graphic Design",
        "Printing Technology",
    ],
    "School of Engineering": [
        "Agricultural & Bio-Environmental Engineering",
        "Chemical Engineering",
        "Civil Engineering",
        "Computer Engineering",
        "Electrical & Electronics Engineering",
        "Industrial Maintenance Engineering",
        "Marine Engineering",
        "Mechanical Engineering",
        "Mechatronics Engineering",
        "Metallurgical Engineering",
        "Mineral & Petroleum Engineering",
        "Welding & Fabrication Engineering",
    ],
    "School of Environmental Studies": [
        "Architecture",
        "Building Technology",
        "Estate Management",
        "Quantity Surveying",
        "Surveying & Geo-Informatics",
        "Urban & Regional Planning",
    ],
    "School of Management & Business Studies": [
        "Accountancy",
        "Banking & Finance",
        "Business Administration & Management",
        "Marketing",
        "Office Technology & Management",
        "Public Administration",
    ],
    "School of Science": [
        "Biological Sciences",
        "Chemical Sciences",
        "Physical Sciences",
        "Mathematics",
        "Statistics",
        "Science Laboratory Technology",
    ],
    "School of Technical Education": [
        "Art Education",
        "Business Education",
        "Computer Education",
        "Educational Foundations",
        "Home Economics Education",
        "Industrial Technical Education",
        "Integrated Science Education",
        "Mathematics Education",
        "Science Education",
        "Vocational Education",
    ],
    "School of Liberal Studies": [
        "Languages",
        "Mass Communication",
        "Social Sciences",
    ],
    "School of Technology": [
        "Agricultural Technology",
        "Computer Technology",
        "Food Technology",
        "Hospitality Management",
        "Leisure & Tourism Management",
        "Nutrition & Dietetics",
        "Polymer & Textile Technology",
    ],
}


class Command(BaseCommand):
    help = "Seed YABATECH school & department structure"

    def handle(self, *args, **kwargs):
        for school_name, departments in YABATECH_STRUCTURE.items():
            school, created = School.objects.get_or_create(name=school_name)

            for dept in departments:
                Department.objects.get_or_create(
                    school=school,
                    name=dept
                )

        self.stdout.write(self.style.SUCCESS("YABATECH structure loaded successfully"))
