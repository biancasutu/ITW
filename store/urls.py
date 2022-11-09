from django.urls import path
from store import views

urlpatterns = [
    path('<str:gender>', views.StoreClothesListView.as_view(), name='clothes'),
    path('<str:gender>/<str:prod_type>', views.StoreClothesListView.as_view(), name='filtered_products'),
    path('create-clothes', views.ClothesCreateView.as_view(), name='create_clothes')
]
