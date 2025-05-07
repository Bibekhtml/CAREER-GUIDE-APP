from django.shortcuts import render
from .models import Test

def test_list(request):
    tests = Test.objects.all()
    return render(request, 'tests/index.html', {'tests': tests})

def test_detail(request, test_id):
    test = Test.objects.get(id=test_id)
    return render(request, 'tests/detail.html', {'test': test})