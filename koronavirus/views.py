from django.shortcuts import render
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from koronavirus.models import Stat, Nakazeni, Naockovani
from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse
from koronavirus.forms import StatModelForm


def index(request):

    num_stat = Stat.objects.all().count()
    stat = Stat.objects.order_by('-nazev_statu')
    paginator = Paginator(stat, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'num_stat': num_stat,
        'stat': stat,
        'page_obj': page_obj
    }

    return render(
        request,
        'index.html',
        context=context,
    )


def graf(request):

    num_stat = Stat.objects.all().count()
    stat = Stat.objects.order_by('nazev_statu')

    context = {
        'num_stat': num_stat,
        'stat': stat
    }

    return render(
        request,
        'graf.html',
        context=context
    )


def staty(request):

    return render(
        request,
        'staty.html',
    )


class StatDetailView(DetailView):
    model = Stat

    context_object_name = 'stat_detail'   # your own name for the list as a template variable
    template_name = 'stat/detail.html'  # Specify your own template name/location


class StatCreateView(CreateView):
    model = Stat
    fields = ['nazev_statu', 'zkratka_statu', 'vlajka', 'forma_statu', 'pocet_obyvatel', 'rozloha', 'text']


class StatUpdateView(UpdateView):
    model = Stat
    # fields = '__all__'
    form_class = StatModelForm
    context_object_name = 'stat'
    template_name = 'stat/update.html'

    # success_url = f"/koronavirus/staty/{}/"

    def get_success_url(self):
        return self.request.path[:-7]


class StatDeleteView(DeleteView):
    model = Stat
    success_url = reverse_lazy('stat_detail')
