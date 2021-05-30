from django.urls import path

from .views import date, welwel, show_stock, add_company, add_stock_day

urlpatterns = [
    path('stock/<symbol>', show_stock, name='details'),
    path('welwel', welwel),
    path('date', date),
    path('addcompany', add_company),
    path('addstockday', add_stock_day),

]