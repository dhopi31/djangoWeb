from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(min_length=3,
        widget=forms.TextInput(
            attrs= {
                'class':'form-control',
                'placeholder':'Username',
            }
        )
    )

    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs= {
                'class':'form-control',
                'placeholder':'Password',
                'id':'inputPassword'
            }
        )
    )

class SignUpForm1(forms.Form):
    first_name = forms.CharField(
        label="First Name", widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Nama Depan',
            }
        )
    ) 
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Nama Belakang',
            }
        )
    )

class SignUpForm2(forms.Form):
    username = forms.CharField(min_length=5,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Username',
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type':'email',
                'class':'form-control',
                'placeholder':'Email',
            }
        )
    )
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id':'inputPassword',
                'type':'password',
                'class':'form-control',
                'placeholder':'Password',
            }
        )
    )