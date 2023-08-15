from django.views.generic import ListView

from main.models import Category, Product


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории'
    }


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Товары'
    }


class ProductCategoryListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        products_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'Товары из выбранной категории {products_item.name}'

        return context_data


class ProductCardListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_views += 1
        self.object.save()
        return self.object


