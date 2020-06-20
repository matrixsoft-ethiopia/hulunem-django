from django import forms


class ShopForm(forms.Form):
    
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "input",
            "placeholder": "የድርጅት ስም",
            "name": "name",
        }
    ),
    label=""
    )
    detail_text = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "input2",
            "placeholder": "መግለጫ",
            "name": "detail_text",
        }
    ),
    label=""
    )
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
    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "input",
            "placeholder": "ስልክ ቁጥር",
            "name": "phone_number",
        }
    ),
    label=""
    )
    TIN_number = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "input",
            "placeholder": "TIN NO",
            "name": "TIN_number",
        }
    ),
    label=""
    )
    mainimage = forms.ImageField(widget=forms.FileInput(
        attrs={
            "class": "input3",
            "placeholder": "የTIN-NO ፎቶ",
            }
    ),
    label=""
    )