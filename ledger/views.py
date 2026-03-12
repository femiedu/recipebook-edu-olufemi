from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RecipeForm, RecipeImageForm
from .models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "ledger/recipe_list.html", {"recipes": recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "ledger/recipe_detail.html", {"recipe": recipe})


@login_required
def recipe_add(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return redirect("ledger:recipe-detail", pk=recipe.pk)
    else:
        form = RecipeForm()

    return render(request, "ledger/recipe_form.html", {"form": form})


@login_required
def recipe_image_add(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.recipe = recipe
            image.save()
            return redirect("ledger:recipe-detail", pk=recipe.pk)
    else:
        form = RecipeImageForm()

    return render(
        request,
        "ledger/recipeimage_form.html",
        {
            "form": form,
        },
    )