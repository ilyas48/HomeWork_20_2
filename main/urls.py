from django.urls import path

from main.apps import MainConfig
from main.views import CategoryListView, ProductListView, ProductCategoryListView, ProductCardListView, \
    ProductCreateView, ProductUpdateView, toggle_activity

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('<int:pk>/main/', ProductCategoryListView.as_view(), name='products_categories'),
    path('<str:name>/main/', ProductCardListView.as_view(), name='product_card'),
    path('create/', ProductCreateView.as_view(), name='create_products'),
    path('<int:pk>/main/update/', ProductUpdateView.as_view(), name='update_products'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),
]
