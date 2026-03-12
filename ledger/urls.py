from django.urls import path
from . import views

app_name = "ledger"

urlpatterns = [
    path("recipes/list/", views.recipe_list, name="recipe-list"),
    path("recipes/add/", views.recipe_add, name="recipe-add"),
    path("recipes/<int:pk>/", views.recipe_detail, name="recipe-detail"),
    path("recipes/<int:pk>/add_image/", views.recipe_image_add, name="recipe-image-add"),
]