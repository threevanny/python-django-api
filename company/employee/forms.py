from django import forms
from .models import Employee


# creating a form
class EmployeeForm(forms.ModelForm):
    edob = forms.DateField(widget=forms.TextInput(attrs=
    {
        'class': 'datepicker'
    }))

    
    # create meta class
    class Meta:
        # specify model to be used
        model = Employee

        fields = ['eid', 'ename', 'eemail', 'econtact', 'edob']

        #fields = '__all__'

       

       


       

        