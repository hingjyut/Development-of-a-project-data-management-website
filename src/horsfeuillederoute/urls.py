from django.urls import path
from .views import (HorsFeuilleDeRouteListView,
                    HorsFeuilleDeRouteDetailView,
                    HorsFeuilleDeRouteCreateView,
                    HorsFeuilleDeRouteUpdateView,
                    HorsFeuilleDeRouteDeleteView,
                    )

app_name = 'horsfeuillederoute'
urlpatterns = [
    path('home', HorsFeuilleDeRouteListView.as_view(), name = 'horsfeuillederoute-list'),
    path('create/', HorsFeuilleDeRouteCreateView.as_view(), name='horsfeuillederoute-create'),
    path('<int:id>', HorsFeuilleDeRouteDetailView.as_view(), name = 'horsfeuillederoute-detail'),
    path('<int:id>/update/', HorsFeuilleDeRouteUpdateView.as_view(), name = 'horsfeuillederoute-update'),
    path('<int:id>/delete/', HorsFeuilleDeRouteDeleteView.as_view(), name = 'horsfeuillederoute-delete'),
    ]
