
from django.urls import path
from . import views

urlpatterns = [
    path('text/' , views.text , name="home"),
    path('add/' , views.Add , name="add"),
    path('' , views.show , name='show'),
    path('delete/<int:id>', views.delete, name="delete"),
    path('edit/<int:id>' , views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    path('search/' , views.search , name="search")

]
