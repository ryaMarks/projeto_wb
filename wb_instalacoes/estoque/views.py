from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, resolve_url
from django.views.generic import DetailView, ListView
from ..produto.models import Produto
from .forms import EstoqueForm, EstoqueClienteForm, EstoqueFornecedorForm,  EstoqueItensEntradaForm, EstoqueItensSaidaForm
from .models import (
    Estoque,
    EstoqueEntrada,
    EstoqueItens,
    EstoqueSaida
)
from django.template.loader import render_to_string
from weasyprint import HTML  # importa biblioteca do weasyprint para arquivos estaticos
import datetime
from decimal import Decimal


@login_required
def estoque_entrada_list(request):
    template_name = 'estoque_list.html'
    objects = EstoqueEntrada.objects.all()
    context = {
        'object_list': objects,
        'titulo': 'Entrada',
        'url_add': 'estoque:estoque_entrada_add'
    }
    return render(request, template_name, context)


class EstoqueEntradaList(ListView):
    model = EstoqueEntrada
    template_name = 'estoque_list.html'

    def get_context_data(self, **kwargs):
        context = super(EstoqueEntradaList, self).get_context_data(**kwargs)
        context['titulo'] = 'Entrada'
        context['url_add'] = 'estoque:estoque_entrada_add'
        return context


@login_required
def estoque_entrada_detail(request, pk):
    template_name = 'estoque_detail.html'
    obj = EstoqueEntrada.objects.get(pk=pk)
    context = {
        'object': obj,
        'url_list': 'estoque:estoque_entrada_list'
    }
    return render(request, template_name, context)


class EstoqueDetail(DetailView):
    model = Estoque
    template_name = 'estoque_detail.html'


def dar_baixa_estoque(form):
    # Pega os produtos a partir da instância do formulário (Estoque).
    produtos = form.estoques.all()
    for item in produtos:
        produto = Produto.objects.get(pk=item.produto.pk)
        produto.estoque = item.saldo
        produto.save()


def estoque_add(request, form_inline, template_name, movimento, url):
    estoque_form = Estoque()
    item_estoque_formset = inlineformset_factory(
        Estoque,
        EstoqueItens,
        form=form_inline,
        extra=0,
        can_delete=False,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        cliente = EstoqueClienteForm(request.POST, instance=estoque_form, prefix='main')
        fornecedor = EstoqueFornecedorForm(request.POST, instance=estoque_form, prefix='main')
        form = EstoqueForm(request.POST, instance=estoque_form, prefix='main')
        formset = item_estoque_formset(
            request.POST,
            instance=estoque_form,
            prefix='estoque'
        )
        if movimento == 'e':
            aux = fornecedor
        if movimento == 's':
            aux = cliente
        if form.is_valid() and formset.is_valid() and aux.is_valid():
            form = form.save(commit=False)
            form.funcionario = request.user
            form.movimento = movimento
            aux.save()
            form.save()
            formset.save()
            dar_baixa_estoque(form)
            return {'pk': form.pk}
    else:
        form = EstoqueForm(instance=estoque_form, prefix='main')
        formset = item_estoque_formset(instance=estoque_form, prefix='estoque')
        cliente = EstoqueClienteForm(instance=estoque_form, prefix='main')
        fornecedor = EstoqueFornecedorForm(instance=estoque_form, prefix='main')
        if movimento == 'e':
            context = {'form': form, 'formset': formset, 'fornecedor': fornecedor}
        if movimento == 's':
            context = {'form': form, 'formset': formset, 'cliente': cliente}
        return context


@login_required
def estoque_entrada_add(request):
    form_inline = EstoqueItensEntradaForm
    template_name = 'estoque_entrada_form.html'
    movimento = 'e'
    url = 'estoque:estoque_detail'
    context = estoque_add(request, form_inline, template_name, movimento, url)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)


def estoque_saida_list(request):
    template_name = 'estoque_list.html'
    objects = EstoqueSaida.objects.all()
    context = {
        'object_list': objects,
        'titulo': 'Saída',
        'url_add': 'estoque:estoque_saida_add'
    }
    return render(request, template_name, context)


class EstoqueSaidaList(ListView):
    model = EstoqueSaida
    template_name = 'estoque_list.html'

    def get_context_data(self, **kwargs):
        context = super(EstoqueSaidaList, self).get_context_data(**kwargs)
        context['titulo'] = 'Saída'
        context['url_add'] = 'estoque:estoque_saida_add'
        return context


def estoque_saida_detail(request, pk):
    template_name = 'estoque_detail.html'
    obj = EstoqueSaida.objects.get(pk=pk)
    context = {
        'object': obj,
        'url_list': 'estoque:estoque_saida_list'
    }
    return render(request, template_name, context)


@login_required
def estoque_saida_add(request):
    form_inline = EstoqueItensSaidaForm
    template_name = 'estoque_saida_form.html'
    movimento = 's'
    url = 'estoque:estoque_detail'
    context = estoque_add(request, form_inline, template_name, movimento, url)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)


@login_required
def pdf_generate(request, pk):  # recebe a solicitacao html e o nome do usuario
    lista = Estoque.objects.get(pk=pk)  # pega os dados do cliente com o nome e salva em 'lista'
    # coletando dados dos produtos
    produto = []
    for obj in lista.estoques.all():
        prod = []
        prod.append(obj.produto.produto)  # nome do produto
        prod.append(obj.quantidade)  # quantidade movimentada
        prod.append(obj.produto.preco)  # preço unitario do produto
        bruto = f'{Decimal(int(obj.quantidade) * float(obj.produto.preco)):,.2f}'
        prod.append(Decimal(bruto))  # preço bruto do produto
        prod.append(obj.produto.medida)
        produto.append(prod)




    # coletando outros dados
    outros = []
    total = 0
    for i in produto:
        total = total + i[3]
    outros.append(total)
    if lista.movimento == 'e':
        outros.append(lista.fornecedor)
    else:
        outros.append(lista.cliente)
    outros.append(lista.nf)
    outros.append(datetime.datetime.now())
    outros.append(lista.movimento)


    # cria ao html
    context = {  # variavel que carrega os dados para o html
        'produto': produto,  # passa os dados do cliente que serao enviados para o html
        'geral': outros,
    }
    html_string = render_to_string('pdf.html', context=context)  # prepara o template html
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    pdf = html.write_pdf()  # transforma html em pdf
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Orçamento - ' + str(lista.nf) + '.pdf"'
    return response
