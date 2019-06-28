from django.contrib import admin
from django.urls import path

from .views import (
                    direction_delete_view,

                    direction_update_view,
                    direction_create_view,
                    direction_list_view,
                    direction_detail_view,
                    )

app_name = "directions"
urlpatterns=[
    path('', direction_list_view, name='direction-list'),
    path('create/', direction_create_view, name = 'direction_list'),
    path('<int:id>/', direction_detail_view, name='product-detail'),
    path('<int:id>/delete', direction_delete_view, name='direction-delete'),
    path('<int:id>/update', direction_update_view, name='direction-update'),
]
