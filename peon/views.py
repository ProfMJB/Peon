from django.shortcuts import render

# Create your views here.

def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        lat = request.POST['startLat']
        lng = request.POST['startLong']
        lifetime = request.POST['lifetime']
        return render(request, 'peon/add.html',
                      context={'name':name,
                               'lat':lat,
                               'long':lng,
                               'lifetime':lifetime})
    else:
        return render(request,'peon/add.html')