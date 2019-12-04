from django.shortcuts import render

def index(request):
    print(request.GET)
    return render(
        request,
        'Base.html', 
    )

