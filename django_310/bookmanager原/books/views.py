from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        'name': '马上双十一'
    }
    return render(request, 'book/index.html', context=context)
def test(request):
    context = {
        'name': '马上双十一'
    }
    return render(request, 'book/test.html', context=context)