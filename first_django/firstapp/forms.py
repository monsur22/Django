from django import forms
from firstapp.models import Firstapp
# class FirstappForm(forms.ModelForm):
#     class Meta:
#         model = Firstapp
#         fields = {
#             "first_name",
#             "last_name",
#             "desc"
#         }
class FirstappForm(forms.ModelForm):

    class Meta:
        model = Firstapp
        fields = ('first_name', 'last_name', 'desc',)