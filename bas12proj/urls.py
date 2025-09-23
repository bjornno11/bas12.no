from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("system/", include(("system.urls", "system"), namespace="system")),
    path("master/", include(("master.urls", "master"), namespace="master")),
    path("ordre/", include(("ordre.urls", "ordre"), namespace="ordre")),
    path("innkjop/", include(("innkjop.urls", "innkjop"), namespace="innkjop")),
    path("reskontro/", include(("reskontro.urls", "reskontro"), namespace="reskontro")),
    path("lager/", include(("lager.urls", "lager"), namespace="lager")),
    path("regnskap/", include(("regnskap.urls", "regnskap"), namespace="regnskap")),
    path("lonn/", include(("lonn.urls", "lonn"), namespace="lonn")),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    
    # Faste data
    path("ansatte/", include(("ansatte.urls", "ansatte"), namespace="ansatte")),
    path("kunder/", include(("kunder.urls", "kunder"), namespace="kunder")),
    
    # Startside
    path("", include("portal.urls", namespace="portal")),
]
