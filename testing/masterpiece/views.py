import requests
import json
from django.views.generic import CreateView, ListView
from .models import Masterpiece, Buyer
from .forms import MasterpieceModelForm


# Create your views here.
class MasterpieceCreateView(CreateView):
    model = Masterpiece
    form_class = MasterpieceModelForm
    template_name = 'masterpiece/masterpieces.html'


class MasterpieceListView(ListView):
    model = Masterpiece
    template_name = 'masterpiece/masterpieces.html'


class BuyerListView(ListView):
    models = Buyer
    template_name = 'buyer/buyer.html'

    def get_queryset(self):
        resp = requests.get('https://bit.ly/2nkSGF1').content
        resp = json.loads(resp)
        data = resp['data']
        for i in data:
            name = i[0] + i[1]
            gender = None
            if i[0] == 'jade':
                gender = 'man'
            elif i[0] == 'jozz':
                gender = 'woman'
            if not Buyer.objects.filter(name=name).exists():

                Buyer(
                    name=i[0] + i[1],
                    position=i[2],
                    nationality=i[3],
                    property=i[5],
                    gender=gender
                ).save()

        queryset = Buyer.objects.all()
        return queryset
