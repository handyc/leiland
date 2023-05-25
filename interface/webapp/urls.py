from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('search/', views.search, name = 'search'),
    path('testsearch/', views.testsearch, name = 'testsearch'),
    path('about/', views.about, name = 'about'),
    path('cmdi/', views.cmdi, name = 'cmdi'),
    path('results/', views.results, name = 'results'),
    path('testresults/', views.testresults, name = 'testresults'),
    path('dataset/<int:dataset_id>', views.dataset, name = 'dataset'),
    #path('create/', views.create, name = 'create'),
    #path('edit/', views.edit, name = 'edit'),
    #path('fragment/', views.fragment, name = 'fragment'),
]
