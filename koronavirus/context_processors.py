from koronavirus.models import Stat


def stat(request):
    return {'genres': Stat.objects.all()}
