
from django import forms
from sms.models import*

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        # ['name','address','mobileno']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'
            field.widget.attrs['placeholder']='Enter '+field.label+'*'

class PaymentDetailForm(forms.ModelForm):
    class Meta:
        model=PaymentDetails
        fields='__all__'
 
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'

   