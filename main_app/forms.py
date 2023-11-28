from django.forms import ModelForm

from .models import Comment, Meal_Had

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]
        
class Meal_Had_Form(ModelForm):
    class Meta:
        model = Meal_Had
        fields = ['date', 'description', ]
        