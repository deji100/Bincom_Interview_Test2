from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from .models import *

# Create your views here.

def get_pu_result(request):
    results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=13)
    return render(request, 'pu_result.html', {'results': results})

def getPolls(request):
    polling_units = PollingUnit.objects.filter(polling_unit_id__gt=0)
    return render(request, 'polls.html', {'polls': polling_units})

def getPollByLGA(request, id):
    lga_polls = PollingUnit.objects.filter(lga_id=id)
    return render(request, 'lga_polls.html', {'polls': lga_polls})

def get_all_party_results(request):
    parties = Party.objects.all()
    context = {}
    for party in parties:
        context[party] = AnnouncedPuResults.objects.filter(party_abbreviation=party).aggregate(Sum('party_score'))
    return render(request, 'all_party_results.html', {'context': context})




