from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Fornecedor
from django.contrib import messages
from .forms import FornecedorForm
from django.views.generic import CreateView, ListView
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
class add_fornecedor(CreateView):
    model = Fornecedor
    template_name = 'fornecedor_form.html'
    form_class = FornecedorForm


class FornecedorUpdate(CreateView):
    model = Fornecedor
    template_name = 'fornecedor_form.html'
    form_class = FornecedorForm


class FornecedoresList(ListView):
    model = Fornecedor
    template_name = 'fornecedores_list.html'
    paginate_by = 10


@login_required
def fornecedor_delete(request, pk):
    fornecedor = Fornecedor.objects.get(pk=pk)
    fornecedor.delete()
    messages.success(request, 'Fornecedor deletado com sucesso.')
    return HttpResponseRedirect(reverse('fornecedores:fornecedores_list'))


@login_required
def fornecedor_detail(request, pk):
    template_name = 'fornecedores_detail.html'
    obj = Fornecedor.objects.get(pk=pk)
    search = request.GET.get('search')
    if search:
        obj = obj.filter(fornecedor__icontains=search)
    context = {'object': obj}
    return render(request, template_name, context)
