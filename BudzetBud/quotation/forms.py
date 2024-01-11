from django.forms import forms


class CreateHalfStageForm(forms.Form):
    GEEKS_CHOICES = (
        ("1", "-"),
        ("2", "Mb"),
        ("3", "m2"),
        ("4", "m3"),
        ("5", "kg"),
    )

    title = forms.CharField()
    unit = forms.ChoiceField(choice = GEEKS_CHOICES)
    value = forms.DecimalField(widget = forms.NumberInput)
    priceforunit = forms.DecimalField(widget = forms.NumberInput)
    fullprice = forms.DecimalField(widget = forms.NumberInput)
