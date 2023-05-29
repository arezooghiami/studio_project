from django.urls import path
from . import views

app_name='product'

urlpatterns = [
    path('',views.product,name='product'),
    path('product/',views.all_product,name='all_product'),
    path('category/<slug>/<int:id>/',views.all_product,name='category'),
    path('detail/<int:id>/',views.product_detail,name='detail')
 ]
