from django import forms
from django.contrib.auth.models import User
from library.models import School, Department, Level


class StudentRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm Password"
    )

    school = forms.ModelChoiceField(
        queryset=School.objects.all()
    )

    department = forms.ModelChoiceField(
        queryset=Department.objects.none()
    )

    level = forms.ModelChoiceField(
        queryset=Level.objects.all()
    )

    class Meta:
        model = User
        fields = ["username", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "school" in self.data:
            try:
                school_id = int(self.data.get("school"))
                self.fields["department"].queryset = Department.objects.filter(
                    school_id=school_id
                )
            except:
                pass

    def clean(self):
        cleaned = super().clean()

        if cleaned.get("password1") != cleaned.get("password2"):
            self.add_error("password2", "Passwords do not match")

        return cleaned
