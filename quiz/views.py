from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Question, Choice

def index(request):
    question_text = Question.objects.all
    return render(request, 'quiz/index.html', {'questions': question_text})

def add_question(request):
    q = Question(question_text = request.POST['question_input'])
    q.save()
    q.choice_set.create(choice_text = request.POST['name_choice1'], answer = request.POST['choice1'], votes = 0)
    q.choice_set.create(choice_text = request.POST['name_choice2'], answer = request.POST['choice2'], votes = 0)
    question_text = Question.objects.all
    return redirect('/')

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/results.html', {'question': question})

def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question answer form.
        return render(request, 'quiz/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('quiz:results', args=(question.id,)))
