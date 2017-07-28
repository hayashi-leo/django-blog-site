### lin,leo - this file must be named 'forms.py' so it can
# be recognized by django

from django import forms
from . models import Post

# our Form is named 'PostForm' and it inherits from django ModelForm
class PostForm(forms.ModelForm):
    # with meta, we tell django which model should be used to create
    # this form (model = Post)
    class Meta:
        model = Post
        fields = ('title', 'text',)
