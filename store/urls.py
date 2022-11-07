from django.urls import path
from store import views

urlpatterns = [
    path('<str:gender>', views.StoreClothesListView.as_view(), name='all_products'),
    path('<str:gender>/<str:prod_type>', views.StoreClothesListView.as_view(), name='filtered_products')
]
