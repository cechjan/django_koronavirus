from django.shortcuts import render
from django.views.generic import ListView, DetailView
from koronavirus.models import Stat, Nakazeni, Naockovani
from django.core.paginator import Paginator


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

