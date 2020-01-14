from django import forms
from multiselectfield import MultiSelectFormField

class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    rating = forms.IntegerField(
        label="Enter Your Rating",
        widget=forms.NumberInput(
            attrs={
            'class':'form-control',
                'placeholder':'Your Rating'
            }
        )
    )
    feedback = forms.CharField(
        label="Enter Your Feedback",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your Feedback'
            }
        )
    )

class EnquiryForm(forms.Form):
    name = forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your Name'
            }
        )
    )

    email = forms.EmailField(
        label="Enter Your Email",
         widget=forms.EmailInput(
             attrs={
                 'class': 'form-control',
                 'placeholder': 'your Email'
                    }
             )
        )

    mobile = forms.IntegerField(
        label="Enter Your Mobile",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your Mobile Number'
            }
        )
    )
    Gender_Choices = (
        ('F',"Female"),
        ('M',"Male")
    )
    gender = forms.ChoiceField(
        widget=forms.RadioSelect,choices=Gender_Choices
    )
    Courses_Choices = (
        ('PY', "PYTHON"),
        ('DJ', 'Django'),
        ('RA', 'Rest Api')
    )
    course=MultiSelectFormField(choices=Courses_Choices)
    Shifts_Choices = (
        ('Morning', 'Morning shift'),
        ('Afternoon', 'Afternoon_shift'),
        ('Evening', 'Evening_shift'),
        ('Night', 'Night_shift')
    )
    shifts = MultiSelectFormField(choices=Shifts_Choices)
    start_date = forms.DateField(
        widget=forms.SelectDateWidget()
    )