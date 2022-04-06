from django import forms

class SalaryForm(forms.Form):
	salary = forms.CharField(label='salary', max_length=50)