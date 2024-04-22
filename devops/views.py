# Create your views here.

from django.shortcuts import render, redirect
from .forms import PostItForm
from .models import PostIt

def postit_list(request):
    postits = PostIt.objects.all()
    form = PostItForm()

    if request.method == 'POST':
        form = PostItForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postit_list')

    return render(request, 'postit_list.html', {'postits': postits, 'form': form})
