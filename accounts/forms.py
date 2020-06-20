from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class loginForm(forms.Form):
     
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "input",
            "placeholder": "ኢሜይል"
        }
    ),
    label=""
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "input",
             "placeholder": "የይለፍ ቃል"
        }

    ),
    label=""
    )
class registerForm(forms.Form):
     
    firstName = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "input",
            "placeholder": "ስም"
        }
    ),
    label=""
    )
    lastName = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "input",
            "placeholder": "የአባት ስም"
        }
    ),
    label=""
    )
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            "class": "input",
            "placeholder": "ኢሜይል"
        }
    ),
    label=""
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "input",
             "placeholder": "የይለፍ ቃል"
        }

    ),
    label=""
    )
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "input",
             "placeholder": "የይለፍ ቃልዎን በድጋሚ ያስገቡ"
        }

    ),
    label=""
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("ያስገቡት ኢሜይል ከዚህ በፊት የተመዘገበ ነው")
        return email

    def clean(self):
        data = self.cleaned_data
        passwod = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != passwod:
            raise forms.ValidationError("ያስገቡት የይለፍ ቃል ተመሳሳይ አይደለም")
        return data


class UpdateProfileForm(forms.ModelForm):
     
    firstName = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "input-register",
            "placeholder": "ስም",
            "name": "firstname"
        }
    ),
    label=""
    )
    lastName = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "input-register",
            "placeholder": "የአባት ስም"
        }
    ),
    label=""
    )
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            "class": "input-register",
            "placeholder": "ኢሜይል"
        }
    ),
    label=""
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("ያስገቡት ኢሜይል ከዚህ በፊት የተመዘገበ ነው")
        return email

    def save(self, commit=True):
        user = super(UpdateProfileForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_Name = self.cleaned_data['firstname']
        user.last_name = self.cleaned_data['lastname']
        if commit:
            user.save()

        return user