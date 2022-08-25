import imp
from django.urls import path
from .views import get_all_party_results, getPollByLGA, getPolls, get_pu_result

urlpatterns = [
    path('', get_pu_result, name='pu_result'),
    path('polls/', getPolls, name='polls'),
    path('poll_lga/<int:id>', getPollByLGA, name='poll_lga'),
    path('party_results', get_all_party_results, name='party_results')
]
