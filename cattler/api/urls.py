from django.urls import path
from .views import AnimalCreate, TroopCreate, CorralCreate, LotCreate, AnimalIngressView, getAnimals, getTroops

urlpatterns = [
    path('animals/', AnimalCreate.as_view(), name='animal-create'),
    path('animals/get', getAnimals.as_view(), name='animal-get'),
    path('troops/', TroopCreate.as_view(), name='troop-create'),
    path('troops/get', getTroops.as_view(), name='troops-get'),
    path('corrals/', CorralCreate.as_view(), name='corral-create'),
    path('lots/', LotCreate.as_view(), name='lots-create'),
    path('animals/income/', AnimalIngressView.as_view(), name='animal-income'),

]