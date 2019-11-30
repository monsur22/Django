    from django import forms  
  from .models import Firstapp
    class FirstappForm(forms.ModelForm):  
        class Meta:  
            model = Firstapp  
            fields = "__all__"  