from django.forms import ModelForm
from conferences.models import Feedback
from captcha.fields import CaptchaField


class FeedbackForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
