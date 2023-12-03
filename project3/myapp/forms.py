from django import forms 
from .models import Django_Table

class Django_form(forms.ModelForm):
   class Meta:
      model = Django_Table
      fields = "__all__"







