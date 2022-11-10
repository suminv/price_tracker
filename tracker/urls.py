from django.contrib import admin
from django.urls import path
from links.views import home_view, LinkDeleteView, update_prices

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home-view'),
    path('detele/<pk>/', LinkDeleteView.as_view(), name='delete'),
    path('update/', update_prices, name='update-prices'),

]
