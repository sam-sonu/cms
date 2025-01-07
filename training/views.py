# training/views.py
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import TrainingPluginModel
from django.shortcuts import get_object_or_404, render


def training_list(request):
    trainings = TrainingPluginModel.objects.all()
    paginator = Paginator(trainings, 10)  # Show 10 trainings per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'training/training_list.html', {'page_obj': page_obj})

def training_detail(request, id):
    training = get_object_or_404(Training, id=id)
    return render(request, 'training/training_detail.html', {'training': training})

def check_feedback(request, id):
    training = get_object_or_404(Training, id=id)
    # Implement feedback logic here
    return render(request, 'training/check_feedback.html', {'training': training})

def mark_action(request, id, action):
    training = get_object_or_404(Training, id=id)
    if action in ['done', 'rejected', 'postponed']:
        # Implement action logic here
        pass
    return redirect('training_list')