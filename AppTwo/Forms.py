from django import forms
from django.core import validators
from AppTwo.models import Webpage
FAVORITE_COLORS_CHOICES = (
	('blue', 'Blue'),
	('green', 'Green'),
	('black', 'Black'),
)

def check_for_z(value):
	if value[0].lower() != 'z':
		raise forms.ValidationError("Name needs to start with z")

class User_Forms(forms.Form):
	name=forms.CharField(validators=[check_for_z])
	email=forms.EmailField()
	verify_email=forms.EmailField(label="Re-Enter E-Mail",)
	text=forms.CharField(widget=forms.Textarea)
	select=forms.BooleanField()
	birth_year = forms.DateField(widget=forms.SelectDateWidget())
	favorite_colors = forms.MultipleChoiceField(
		required=False,
		widget=forms.CheckboxSelectMultiple,
		choices=FAVORITE_COLORS_CHOICES,
	)
	bot_catcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

	def clean_bot_catcher(self):
		botcatcher = self.cleaned_data['bot_catcher']
		if len(botcatcher) > 0:
			raise forms.ValidationError("GOTCHA!")
		return botcatcher

	def clean(self):
		all_cleaned_data = super().clean()
		email=all_cleaned_data['email']
		v_email=all_cleaned_data['verify_email']
		if email != v_email:
			raise forms.ValidationError("Make Sure Email matches")

class web_form(forms.ModelForm):

	class Meta:
		model=Webpage
		fields = '__all__'
		