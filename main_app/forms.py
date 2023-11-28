from django.forms import ModelForm
from .models import Meal_Had

class Meal_Had_Form(ModelForm):
    class Meta:
        model = Meal_Had
        fields = ['date', 'description', ]