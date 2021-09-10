from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/assinar/
    path('assinar/', views.assinar, name='assinar'),

    # ex: /polls/assinar/
    path('assinar/form/', views.assinarForm, name='assinarForm'),

    # ex: /polls/autenticar/
    path('autenticar/', views.autenticar, name='autenticar'),

    # ex: /polls/autenticar/form/
    path('autenticar/form/', views.autenticarForm, name='autenticarForm'),

    # ex: /polls/chaves/
    path('chaves/', views.chaves, name='chaves'),

    # ex: /polls/chaves/form
    path('chaves/form/', views.chavesForm, name='chavesForm'),

    # ex: /polls/
    path('', views.index, name='index')
]