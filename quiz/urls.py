from django.urls import path
from . import views

app_name = 'quiz'
urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    path('add_question', views.add_question, name='add_question'),
    # ex: /5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /5/vote/
    path('<int:question_id>/answer/', views.answer, name='answer'),
]
