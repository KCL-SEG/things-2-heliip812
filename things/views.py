from django.shortcuts import render
from .forms import ThingForm

def home(request):

    if request.method == 'POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            thing = form.save()
    else:
        form = ThingForm()
    return render(request, 'home.html', {'form': form})
