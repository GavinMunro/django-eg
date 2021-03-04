from django import forms


class CarForm(forms.Form):
    vin = forms.CharField(
        max_length=64,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Vehicle Identification Number"
        })
    )
    
    rego = forms.CharField(
        max_length=6,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Registration number"
        })
    )
    
    make = forms.CharField(
        max_length=32,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Manufacturering company eg Holden"
        })
    )
    
    model = forms.CharField(
        max_length=32,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "The model of your car eg. Commodore"
        })
    )
    
    year = forms.CharField(
        max_length=4,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Year of manufacture"
        })
    )


class CustomerForm(forms.Form):
    email = forms.CharField(
        max_length=80,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your email address"
        })
    )
    
    firstname = forms.CharField(
        max_length=32,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your first name"
        })
    )
    
    lastname = forms.CharField(
        max_length=32,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your last name"
        })
    )
    
    mobile = forms.CharField(
        max_length=16,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your mobile number"
        })
    )
