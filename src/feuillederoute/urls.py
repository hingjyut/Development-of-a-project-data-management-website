from django.urls import path
from .views import (FeuilleDeRouteListView,
                    FeuilleDeRouteDetailView,
                    FeuilleDeRouteCreateView,
                    FeuilleDeRouteUpdateView,
                    FeuilleDeRouteDeleteView,
                    TryFeuilleDeRouteListView,
                    homeindex_view,
                    )

app_name = 'feuillederoute'

urlpatterns = [
    path('home', FeuilleDeRouteListView.as_view(), name = 'feuillederoute-list'),
    path('create/', FeuilleDeRouteCreateView.as_view(), name='feuillederoute-create'),
    path('<int:id>', FeuilleDeRouteDetailView.as_view(), name = 'feuillederoute-detail'),
    # path('', TryFeuilleDeRouteListView.as_view(), name = 'feuillederoute-list'),
    path('home', TryFeuilleDeRouteListView.as_view(), name = 'tryfeuillederoute-list'),
    path('<int:id>/update/', FeuilleDeRouteUpdateView.as_view(), name = 'feuillederoute-update'),
    path('<int:id>/delete/', FeuilleDeRouteDeleteView.as_view(), name = 'feuillederoute-delete'),
    path('homeindex', homeindex_view, name='homeindex'),
    ]
