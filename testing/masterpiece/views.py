from django.views.generic import CreateView, ListView
from .models import Masterpiece
from .forms import MasterpieceModelForm


# Create your views here.
class MasterpieceCreateView(CreateView):
    model = Masterpiece
    form_class = MasterpieceModelForm
    template_name = 'masterpiece/masterpieces.html'


class MasterpieceListView(ListView):
    model = Masterpiece
    template_name = 'masterpiece/masterpieces.html'
