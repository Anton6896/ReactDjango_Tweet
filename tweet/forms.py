from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

from django import forms
from .models import Tweet

MAX_TWEET_LENGTH = 240


# tweet form with field content also change label and placeholder for text field
class CreateTweetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateTweetForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = "New tweet"

    content = forms.CharField(
        widget=forms.Textarea(attrs={
            "id": "tweet_field",
            "rows": "3",
            "label": "tweets",
            'placeholder': 'Please enter your tweet here , max size 240 chars'
        }),
        error_messages={'required': 'max size 240 chars'},

    )

    # todo crispy forms layout ?
    helper = FormHelper()
    helper.layout = Layout(
        Field('content', css_class='form-control-lg'),
    )

    class Meta:
        model = Tweet
        fields = ("content",)

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("this is to big tweet size")

        return content
