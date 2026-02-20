from django.contrib import admin

from .models import (
    School,
    Department,
    Level,
    AcademicState,
    StudentProfile,
    Course,
    Material,
    MaterialUpload,
)

from .services import advance_academic_state, rollback_academic_state


# Core academic structure
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Level)
admin.site.register(StudentProfile)
admin.site.register(Course)
admin.site.register(Material)
admin.site.register(MaterialUpload)


@admin.register(AcademicState)
class AcademicStateAdmin(admin.ModelAdmin):
    list_display = ("current_semester",)
    actions = ["advance", "rollback"]

    def advance(self, request, queryset):
        message = advance_academic_state()
        self.message_user(request, message)

    advance.short_description = "Advance academic state"

    def rollback(self, request, queryset):
        message = rollback_academic_state()
        self.message_user(request, message)

    rollback.short_description = "Rollback academic state"
