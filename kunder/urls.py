from django.urls import path
from . import views

app_name = "kunder"

urlpatterns = [
    path('', views.kunde_liste, name='kunde_liste'),
    path('ny/', views.kunde_ny, name='kunde_ny'),
    path('<int:id>/endre/', views.kunde_endre, name='kunde_endre'),
    path('<int:id>/slette/', views.kunde_slette, name='kunde_slette'),
]
