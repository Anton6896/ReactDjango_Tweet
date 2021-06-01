from django import forms
from .models import Tweet

MAX_TWEET_LENGTH = 240


class CreateTweetForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        "id": "tweet_field",
        "rows": "3",
        'placeholder': 'Please enter your tweet here , max size 240 chars'
    }))

    class Meta:
        model = Tweet
        fields = "__all__"

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("this is to big tweet size")
        return content
