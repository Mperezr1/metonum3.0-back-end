from django.shortcuts import render

from .forms import EcuacionesNoLinealesForms
from .models import EcuacionesNoLineales

# Create your views here.


def EcuacionesNoLinealesView(request):
    form = EcuacionesNoLinealesForms(request.POST or None)
    if form.is_valid():
        form_data = (form.clean())
        funcion = (form_data.get("funcion"))
        valorInicial = (form_data.get("valorInicial"))
        delta = (form_data.get("delta"))
        iter = (form_data.get("iter"))
        obj = EcuacionesNoLineales.objects.create(funcion=form_data.get("funcion"), valorInicial=form_data.get("valorInicial"),
                                                  delta=form_data.get("delta"),  iter=form_data.get("iter"))
    context = {
        "form": form
    }
    return render(request, "ecuacionesNoLineales.html", context)
