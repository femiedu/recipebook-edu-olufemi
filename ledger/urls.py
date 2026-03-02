from django.urls import path
from . import views

app_name = "ledger"

urlpatterns = [
    path("recipes/list/", views.recipe_list, name="recipe-list"),
    path("recipes/<int:pk>/", views.recipe_detail, name="recipe-detail"),
]