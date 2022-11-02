from django.urls import path
from store import views


urlpatterns = [
    path('<str:prod_type>/', views.StoreListView.as_view(), name='all_products'),
]