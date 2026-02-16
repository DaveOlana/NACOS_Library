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
    current_level = models.ForeignKey(Level, on_delete=models.CASCADE)
    current_semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.current_level} - {self.current_semester}"



# -------------------------
# User Profile
# -------------------------

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


# -------------------------
# Learning Materials
# -------------------------

class Material(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
    ]

    title = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class MaterialPage(models.Model):
    material = models.ForeignKey(Material, related_name="pages", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="material_pages/")
    page_number = models.PositiveIntegerField()

    class Meta:
        ordering = ["page_number"]

    def __str__(self):
        return f"{self.material.title} - Page {self.page_number}"


# -------------------------
# Approval System
# -------------------------

class Approval(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE)
    approved_at = models.DateTimeField(auto_now_add=True)


class Rejection(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    rejected_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    rejected_at = models.DateTimeField(auto_now_add=True)


# -------------------------
# Audit Log
# -------------------------

class ActionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


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
