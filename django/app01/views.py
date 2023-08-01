from django.shortcuts import render, redirect

# Create your views here.
from app01.models import Picture


def main(request):
    pictures = Picture.objects.all()

    return render(request, 'main.html', {'result': pictures})
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        images = request.FILES.getlist("image")
        for image in images:
            picture = Picture()
            picture.img = image
            picture.save()

        return redirect('/')