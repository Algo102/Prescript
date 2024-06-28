from .forms import CategoryForm, ReceiptForm, RecipeSearchForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Receipt

import logging

logger = logging.getLogger(__name__)


def main(request):
    recent_receipts = Receipt.objects.all().order_by('-id')[:5]
    logger.info('Main page accessed')
    return render(request, "drink/main.html", {'recent_receipts': recent_receipts})


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            logger.info('new category created')
            return redirect('main')
    else:
        form = CategoryForm()
    return render(request, 'drink/create_category.html', {'form': form})


def add_receipt(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST, request.FILES)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.author = request.user
            receipt.save()
            logger.info(f'Added receipt by {receipt.author}')
            return redirect('main')
    else:
        form = ReceiptForm()
    return render(request, 'drink/add_receipt.html', {'form': form})


def receipt_detail(request, receipt_id):
    receipt = get_object_or_404(Receipt, pk=receipt_id)
    return render(request, 'drink/receipt_detail.html', {'receipt': receipt})


def all_receipt(request):
    recipes = Receipt.objects.all()
    return render(request, "drink/all_receipt.html", {'recipes': recipes})


def get_receipt(request):
    if request.method == 'GET':
        form = RecipeSearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            recipes = (Receipt.objects.filter(name__icontains=search_query) | Receipt.objects.filter(
                description__icontains=search_query))
            return render(request, 'drink/recipe_search_results.html',
                          {'recipes': recipes, 'search_query': search_query})
    else:
        form = RecipeSearchForm()
    return render(request, "drink/get_receipt.html", {'form': form})


def modify_receipt(request, receipt_id):
    receipt = get_object_or_404(Receipt, pk=receipt_id)
    if request.method == 'POST':
        form = ReceiptForm(request.POST, request.FILES, instance=receipt)
        if form.is_valid():
            form.save()
            logger.info('receipt updated successfully')
            return redirect('receipt_detail', receipt_id=receipt.id)
    else:
        form = ReceiptForm(instance=receipt)
    return render(request, "drink/add_receipt.html", {'form': form})
