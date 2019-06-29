from django.forms import ModelForm
from .models import Masterpiece


class MasterpieceModelForm(ModelForm):

    class Meta:
        model = Masterpiece
        fields = '__all__'
