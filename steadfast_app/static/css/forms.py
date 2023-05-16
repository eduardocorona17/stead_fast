from django import forms 

class BuildSite(forms.Form):
    first_name = forms.CharField(label="First Name:", max_length=30)
    last_name = forms.CharField(label="Last Name:", max_length=30)
    email = forms.CharField(label="Email Adress:", max_length=100)
    