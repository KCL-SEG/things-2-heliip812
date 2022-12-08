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

    name = forms.CharField(
        validators=[
            MaxLengthValidator(35, message='name cannot be more than 50 characters')
        ]
    )

    description = forms.Textarea(
        validators=[
            MaxLengthValidator(120, message='name cannot be more than 50 characters')
        ]
    )

    quantity = forms.NumberInput(
        validators=[
            MinValueValidator(0, message='quantity cannot be less than 0'),
            MaxValueValidator(50, message='quantity cannot be larger than 50')
        ]
    )

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
