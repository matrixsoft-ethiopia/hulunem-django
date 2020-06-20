from django import forms


class ProductsForm(forms.Form):
    
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "input",
            "placeholder": "የአስቤዛ ስም",
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
    price = forms.FloatField(widget=forms.TextInput(
        attrs={
            "class": "input3",
            "placeholder": "ዋጋ (ብር)",
            "name": "price",
        }
    ),
    label=""
    )
    stock_qty = forms.FloatField(widget=forms.TextInput(
        attrs={
            "class": "input3",
            "placeholder": "ዝቅተኛ የትእዛዝ መጠን",
            "name": "stock_qty",
        }
    ),
    label=""
    )
    mainimage = forms.ImageField(widget=forms.FileInput(
        attrs={
            "class": "input3",
            "placeholder": "picture",
        }
    ),
    label="", required=False)