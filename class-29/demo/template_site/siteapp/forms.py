from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from .models import Thing
from django.contrib.auth import get_user_model


class BaseThingForm(forms.ModelForm):
    label = "Submit"

    class Meta:
        model = Thing
        fields = "__all__"

    name = forms.CharField(
        label="Enter a favorite thing.",
        max_length=80,
        required=True
    )

    description = forms.TextInput()

    owner = forms.ModelChoiceField(queryset=get_user_model().objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'description',
            'owner',
            Submit('submit', self.label, css_class="submit"),
        )

        self.helper.label_class = "form-label"
        self.helper.form_class = "form"


class ThingCreateForm(BaseThingForm):
    label = "CREATE"


class ThingUpdateForm(BaseThingForm):
    label = "UPDATE"
