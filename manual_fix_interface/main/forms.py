from django import forms

class PolygonForm(forms.Form):
    polygon_id = forms.IntegerField(widget=forms.HiddenInput())
    polygon_class = forms.IntegerField(widget=forms.HiddenInput())

class MatchForm(forms.Form):
    polygon_id_text = forms.IntegerField(widget=forms.HiddenInput())
    text = forms.CharField(widget=forms.HiddenInput())