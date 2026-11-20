from django.shortcuts import render, redirect, get_object_or_404
from .models import RegistroMetrica
from .forms import RegistroMetricaForm


def listar(request):
    registros = RegistroMetrica.objects.all().order_by('-fecha')
    return render(request, 'monitoreo/listar.html', {
        'registros': registros
    })


def crear(request):
    if request.method == 'POST':
        form = RegistroMetricaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = RegistroMetricaForm()

    return render(request, 'monitoreo/formulario.html', {
        'form': form
    })


def editar(request, id):
    registro = get_object_or_404(RegistroMetrica, id=id)

    if request.method == 'POST':
        form = RegistroMetricaForm(request.POST, instance=registro)

        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = RegistroMetricaForm(instance=registro)

    return render(request, 'monitoreo/formulario.html', {
        'form': form
    })


def eliminar(request, id):
    registro = get_object_or_404(RegistroMetrica, id=id)

    if request.method == 'POST':
        registro.delete()
        return redirect('listar')

    return render(request, 'monitoreo/eliminar.html', {
        'registro': registro
    })
