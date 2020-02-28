from django import forms
from django.contrib.auth import get_user_model

from beer.models import Beer, Vote

class VoteForm(forms.ModelForm):

    user = forms.ModelChoiceField(
        widget = forms.HiddenInput,
        queryset = get_user_model().objects.all(),
        disabled = True,
    )

    beer = forms.ModelChoiceField(
        widget = forms.HiddenInput,
        queryset = Beer.objects.all(),
        disabled = True,
    )

    value = forms.ChoiceField(
        label = 'Vote',
        widget = forms.RadioSelect,
        choices = Vote.VALUE_CHOICES,
    )

    class Meta:
        model = Vote
        fields = (
            'value', 'user', 'beer',
        )
