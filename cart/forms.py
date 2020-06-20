from django import forms


class DetailForm(forms.Form):
    location1 = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "input",
            "placeholder": "አድራሻ፣ መለያ የአካባቢ ስም፣ ህንጻ",
            "name": "location1",
        }
    ),
    label=""
    )
    location2 = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "input",
            "placeholder": "ቀበሌ/ክፍለ ከተማ",
            "name": "location2",
        }
    ),
    label=""
    )
    location3 = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "input",
            "name": "location3",
        }
    ),
    label=""
    )
    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "input",
            "placeholder": "ስልክ ቁጥር",
            "name": "phone_number",
        }
    ),
    label=""
    )