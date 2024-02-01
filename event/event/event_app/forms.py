from django import forms
from .models import Soccerbot, LineFollow, IdeaGen, ChatGPT, RoboRace


class SoccerbotForm(forms.ModelForm):
    class Meta:
        model = Soccerbot
        exclude = ['payment_status','member_count']

class LineFollowForm(forms.ModelForm):
    class Meta:
        model = LineFollow
        exclude = ['payment_status', 'member_count']

class RoboRaceForm(forms.ModelForm):
    class Meta:
        model = RoboRace
        exclude = ['payment_status', 'member_count']

class IdeaGenForm(forms.ModelForm):
    class Meta:
        model = IdeaGen
        exclude = ['payment_status', 'member_count']

class ChatGPTForm(forms.ModelForm):
    class Meta:
        model = ChatGPT
        exclude = ['payment_status']