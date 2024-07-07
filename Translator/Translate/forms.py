from django import forms

LANGUAGE_CHOICES = [
    ('es', 'Spanish'),
    ('fr', 'French'),
    ('eg', 'English'),
    ('hi', 'Hindi'),
    ('de', 'German')
]

class TranslateForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Text to translate')
    target_language = forms.ChoiceField(choices=LANGUAGE_CHOICES, label='Target language')
