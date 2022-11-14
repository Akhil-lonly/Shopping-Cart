from . import views
from django.urls import path

#
app_name='ecommerceapp'

urlpatterns = [
    path('',views.AllProdCat,name='AllProdCat'),
    path("<slug:c_slug>/",views.AllProdCat,name='product_by_category'),
    path("<slug:c_slug>/<slug:p_slug>/",views.ProDetail,name='ProDetail'),
]