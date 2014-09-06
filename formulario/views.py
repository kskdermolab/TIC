from django.shortcuts import render
from django.http import HttpResponse
from django.forms import ModelForm

from formulario import models


class FormForm(ModelForm):
    class Meta:
        model = models.Form


def index(request):
    #return HttpResponse("Hello, world. You're at the poll index.")
    form = models.Denuncia(Nombre='Juan')
    form.save()
    form = FormForm()
    context = {'form': form}
    return render(request, 'formulario/index.html', context)

