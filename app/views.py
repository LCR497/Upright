from django.shortcuts import render, redirect
from .forms import FeedbackForm

def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.save()
            return redirect('index')
    else:
        form = FeedbackForm()
    return render(request, 'index.html', {'form': form})
