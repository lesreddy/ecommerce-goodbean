from Django import forms
from .models import *

class ReviewForm(forms.ModelForm):
    class = Meta:
        fields = "comment", "rating")