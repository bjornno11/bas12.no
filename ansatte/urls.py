from django.urls import path
from . import views

app_name = "ansatte"

urlpatterns = [
    path('', views.index, name='index'),
    path('registrer/', views.registrer, name='registrer'),
    path('roller/', views.rolle_liste, name='rolle_liste'),
    path('roller/ny/', views.rolle_ny, name='rolle_ny'),
    path('roller/<int:id>/endre/', views.rolle_endre, name='rolle_endre'),
    path('roller/<int:id>/slette/', views.rolle_slette, name='rolle_slette'),
]
