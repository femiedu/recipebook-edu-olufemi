from django.shortcuts import render

# Create your views here.
RECIPES_LIST = [
    {"name": "Recipe 1", "link": "/recipe/1"},
    {"name": "Recipe 2", "link": "/recipe/2"},
]

RECIPE_1_DATA = {
    "name": "Recipe 1",
    "ingredients": [
        {"name": "tomato", "quantity": "3pcs"},
        {"name": "onion", "quantity": "1pc"},
        {"name": "pork", "quantity": "1kg"},
        {"name": "water", "quantity": "1L"},
        {"name": "sinigang mix", "quantity": "1 packet"},
    ],
}

RECIPE_2_DATA = {
    "name": "Recipe 2",
    "ingredients": [
        {"name": "garlic", "quantity": "1 head"},
        {"name": "onion", "quantity": "1pc"},
        {"name": "vinegar", "quantity": "1/2cup"},
        {"name": "water", "quantity": "1 cup"},
        {"name": "salt", "quantity": "1 tablespoon"},
        {"name": "whole black peppers", "quantity": "1 tablespoon"},
        {"name": "pork", "quantity": "1 kilo"},
    ],
}


def recipes_list(request):
    return render(
        request,
        "ledger/recipes_list.html",
        {"recipes": RECIPES_LIST},
    )


def recipe_1(request):
    return render(
        request,
        "ledger/recipe_detail.html",
        {"recipe": RECIPE_1_DATA},
    )


def recipe_2(request):
    return render(
        request,
        "ledger/recipe_detail.html",
        {"recipe": RECIPE_2_DATA},
    )