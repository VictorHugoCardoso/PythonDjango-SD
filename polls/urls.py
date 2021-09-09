from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/assinar/
    path('assinar/', views.assinar, name='assinar'),
    
    # ex: /polls/autenticar/
    path('autenticar/', views.autenticar, name='autenticar'),

    # ex: /polls/chaves/
    path('chaves/', views.chaves, name='chaves'),

    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]