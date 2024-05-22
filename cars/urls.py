from django.urls import  path
from . import views
app_name = 'car'
urlpatterns = [
    # Главная страница с выводом всех автомобилей
    path('car_list/',views.car_list, name='car_list'),
    path("detail/<int:id>/",views.detail, name="detail"),
    path("compare/<int:id>/",views.compare_cars, name="compare"),
    path("createreview/<int:id>/",views.createreview,name="createreview"),
    path("deletereview/<int:id>/",views.deletereview,name="deletereview"),
    path("updatetereview/<int:id>/",views.updatereview,name="updatereview"),
    path("order/<int:id>/",views.createorder,name="order"),
    path("deleteorder/<int:id>/",views.deleteorder,name="deleteorder")
]