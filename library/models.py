from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# -------------------------
# Academic structure
# -------------------------

class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Department(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.school.name} - {self.name}"


class Level(models.Model):
    name = models.CharField(max_length=20)  # e.g ND1, ND2, HND1

    def __str__(self):
        return self.name


class Semester(models.Model):
    name = models.CharField(max_length=20)  # 1st, 2nd

    def __str__(self):
        return self.name

class AcademicState(models.Model):
    SEMESTER_CHOICES = [
        ("1", "1st Semester"),
        ("2", "2nd Semester"),
    ]

    current_semester = models.CharField(
        max_length=1,
        choices=SEMESTER_CHOICES,
        default="1",
    )

    def __str__(self):
        return f"Current Semester: {self.get_current_semester_display()}"









class StudentProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    school = models.ForeignKey(
        School,
        on_delete=models.PROTECT,
        related_name="students"
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="students"
    )

    level = models.ForeignKey(
        Level,
        on_delete=models.PROTECT,
        related_name="students"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.department.name} - {self.level.name}"


class Course(models.Model):
    """
    Represents a course in a department.
    Courses are stable across years.
    """
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} - {self.title}"


class Material(models.Model):
    """
    A logical book or document (e.g. 'Computer Architecture Notes').
    """
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MaterialUpload(models.Model):
    """
    A specific PDF upload awaiting or having passed admin approval.
    """
    STATUS_CHOICES = [
        ("pending", "Pending Review"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to="materials/")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    rejection_reason = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.material.title} ({self.status})"

