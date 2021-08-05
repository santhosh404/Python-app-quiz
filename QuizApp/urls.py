from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('basic', views.basic, name='basic'),
    path('datatypes', views.datatypes, name='datatypes'),
    path('operators', views.operators, name='operators'),
    path('conditionalstatements', views.con_statements, name='Cstatements'),
    path('loops', views.loops, name='loops'),
    path('functions', views.function, name='function'),
    path('eh', views.exceptHandle, name='exceptHandle')
]
