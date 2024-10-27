from django import forms

from FurryFunnies.mixins import ReadOnlyMixin
from FurryFunnies.post_app.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content']

    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Put an attractive and unique title...'}),
        error_messages={'unique': "Oops! That title is already taken. How about something fresh and fun?"},
        label='Title:'
    )

    image_url = forms.URLField(
        help_text="Share your funniest furry photo URL!",
        label='Post Image URL:'
    )

    content = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Share some interesting facts about your adorable pets...'}),
        label='Content:'
    )

class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content']

        labels = {
            'image_url': 'Post Image URL:',
        }

        error_messages = {
            'title': {
                'unique': "Oops! That title is already taken. How about something fresh and fun?",
            },
        }

class PostDeleteForm(ReadOnlyMixin, forms.ModelForm):
    readonly_fields = ['title', 'image_url', 'content']

    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content']
        labels = {
            'image_url': 'Post Image URL:',
        }
