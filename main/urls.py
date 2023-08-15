from django.urls import path

from main.apps import MainConfig
from main.views import CategoryListView, ProductListView, ProductCategoryListView, ProductCardListView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('<int:pk>/main/', ProductCategoryListView.as_view(), name='products_categories'),
    path('<str:name>/main/', ProductCardListView.as_view(), name='product_card')

]
