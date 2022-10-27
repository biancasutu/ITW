from django.urls import path
from store import views


urlpatterns = [
    path('all', views.StoreListView.as_view(), name='all_products'),
]