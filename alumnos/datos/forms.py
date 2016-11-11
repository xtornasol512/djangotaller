from django.forms import ModelForm
from .models import InfoGeneral


class InfoGeneralForm(ModelForm):
    class Meta:
        model = InfoGeneral
        fields = ["nombre", "email", "semestre", "edad"]
