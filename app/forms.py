from django import forms
from app.models import Tweet

class TweetForm(forms.ModelForm):
	class Meta:
		model = Tweet
		fields = ['tweet']