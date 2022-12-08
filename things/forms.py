"""Forms of the project."""
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator
from .models import Thing

# Create your forms here.

class ThingForm(forms.ModelForm):

    class Meta:
        """Form options."""

        model = Thing
        fields = ['name', 'description', 'quantity']

    name = forms.CharField()
    description = forms.Textarea()
    quantity = forms.NumberInput()

    def save(self):
        """Create a new user."""
        super().clean()
        super().save(commit=False)
        thing = Thing.objects.create(
            name=self.cleaned_data.get('name'),
            description=self.cleaned_data.get('description'),
            quantity=self.cleaned_data.get('quantity'),
        )
        return thing
