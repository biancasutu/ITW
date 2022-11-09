from django.urls import path
from store import views
from .views import get_filtered

urlpatterns = [
    path('<str:acc_name>', get_filtered, name='accessories_by_name'),
    path('create-accessories', views.AccessoriesCreateView.as_view(), name='create_accessories'),
    path('update-accessories', views.AccessoriesUpdateView.as_view(), name='update_accessories'),
    path('delete-accessories', views.AccessoriesDeleteView.as_view(), name='delete_accessories')
]
