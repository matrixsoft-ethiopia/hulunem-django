from django.shortcuts import render
from .models import question, comment,claim

# Create your views here.
def questions_view(request, **kwarg):
    Questions = question()
    message = ""
    if request.method == 'POST':
        Questions.user = request.user
        Questions.detail_text = request.POST.get('detail_text')
        Questions.save()
        message = "√ ጥያቄዎን በተሳካ ሁኔታ ልከዋል። እናመሰግናለን!"
    context = {
        'message' : message,
    }
    return render(request, 'questions.html', context)

def comments_view(request, **kwarg):
    Comments = comment()
    message = ""
    if request.method == 'POST':
        Comments.user = request.user
        Comments.detail_text = request.POST.get('detail_text')
        Comments.save()
        message = "√ አስተያየትዎን በተሳካ ሁኔታ ልከዋል። ስለ አስተያየትዎ እናመሰግናለን!"
    context = {
        'message' : message,
    }
    return render(request, 'comments.html', context)

def claims_view(request, **kwarg):
    Claims = claim()
    message = ""
    if request.method == 'POST':
        Claims.user = request.user
        Claims.detail_text = request.POST.get('detail_text')
        Claims.save()
        message = "√ ቅሬታዎን በተሳካ ሁኔታ ልከዋል። እናመሰግናለን!"
    context = {
        'message' : message,
    }
    return render(request, 'claims.html', context)