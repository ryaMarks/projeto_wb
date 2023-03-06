import csv
import io
from datetime import datetime
from django.contrib import messages
from ..produto.actions.export_xlsx import export_xlsx
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView
from .models import Produto
from .forms import ProdutoForm
# Create your views here.


@login_required
def produto_list(request):
    template_name = 'produto_list.html'
    objects = Produto.objects.all()
    context = {'object_list': objects}
    return render(request, template_name, context)


class ProdutoList(ListView):
    model = Produto
    template_name = 'produto_list.html'
    paginate_by = 10


@login_required
def produto_detail(request, pk):
    template_name = 'produto_detail.html'
    obj = Produto.objects.get(pk=pk)
    obj.preco_venda = obj.preco_compra + obj.preco_compra * (obj.lucro/100)
    context = {'object': obj}
    return render(request, template_name, context)


class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm


class ProdutoUpdate(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm


@login_required
def produto_delete(request, pk):
    produto = Produto.objects.get(pk=pk)
    produto.delete()
    messages.success(request, 'Produto deletado com sucesso.')
    return HttpResponseRedirect(reverse('produto:produto_list'))


@login_required
def delete_all(request):
    if request.method == 'POST':
        for produto in Produto.objects.all():
            if str(produto.pk) in request.POST:  # verifica se name-input foi enviado na requisição
                if request.POST[str(produto.pk)] == 'on':
                    produto.delete()
    return HttpResponseRedirect(reverse('produto:produto_list'))




@login_required
def produto_json(request, pk):
    # retorna o produto, ID e estoque
    produto = Produto.objects.filter(pk=pk)
    data = [item.to_dict_json() for item in produto]
    return JsonResponse({'data': data})


def save_data(data):
    aux = []
    for item in data:
        codigo = item.get('codigo')
        produto = item.get('produto')
        medida = item.get('medida')
        preco = item.get('preco')
        estoque = item.get('quantidade')
        obj = Produto(
            codigo=codigo,
            produto=produto,
            medida=medida,
            preco=preco,
            estoque=estoque,
        )
        aux.append(obj)
    print(aux)
    Produto.objects.bulk_create(aux)


@login_required
def import_csv(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        # Lendo arquivo InMemoryUploadedFile
        file = myfile.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(file))
        # Gerando uma list comprehension
        data = [line for line in reader]
        save_data(data)
        return HttpResponseRedirect(reverse('produto:produto_list'))

    template_name = 'produto_import.html'
    return render(request, template_name)


@login_required
def exportar_produtos_xlsx(request):
    MDATA = datetime.now().strftime('%Y-%m-%d')
    model = 'Produto'
    filename = 'produtos_exportados.xlsx'
    _filename = filename.split('.')
    filename_final = f'{_filename[0]}_{MDATA}.{_filename[1]}'
    queryset = Produto.objects.all().values_list(
        'codigo',
        'produto',
        'preco',
        'fabricante',
        'estoque',
    )
    columns = ('Codigo', 'Produto', 'Preço', 'Fabricante', 'Estoque')
    response = export_xlsx(model, filename_final, queryset, columns)
    return response
