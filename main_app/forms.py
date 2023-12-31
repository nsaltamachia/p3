from django.forms import ModelForm
from .models import Comment, Meal_Had, Seat
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]
        
class Meal_Had_Form(ModelForm):
    class Meta:
        model = Meal_Had
        fields = ['date', 'description', ]
        
class SeatForm(ModelForm):
    class Meta:
        model = Seat
        fields = ['table_type', 'table_capacity', 'indoor_or_outdoor']
     