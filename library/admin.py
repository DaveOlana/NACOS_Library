from django.contrib import admin
from .models import (School, Department, Level, Semester, StudentProfile, 
                     AcademicState, Course, Material, MaterialUpload)
from .services import advance_academic_state, rollback_academic_state

admin.site.register(School)
admin.site.register(Department)
admin.site.register(Level)
admin.site.register(Semester)
admin.site.register(StudentProfile)

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

admin.site.register(Course)
admin.site.register(Material)
admin.site.register(MaterialUpload)

