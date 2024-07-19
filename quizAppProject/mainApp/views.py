from django.shortcuts import render
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    msg=None
    form=forms.RegisterUser
    if request.method=='POST':
        form=forms.RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            msg='Registered'
    return render(request, 'registration/register.html', {'form':form, 'msg':msg})


def all_categories(request):
    catData=models.Qcategory.objects.all()
    return render(request, 'all-category.html', {'data': catData})


@login_required
def cat_questions(request, cat_id):
    category=models.Qcategory.objects.get(id=cat_id)
    question=models.Question.objects.filter(category=category).order_by('id').first()
    return render(request, 'cat-questions.html', {'question':question, 'category': category})

@login_required
def submit_answer(request,cat_id,quest_id):
    if request.method=='POST':
        category=models.Qcategory.objects.get(id=cat_id)
        question=models.Question.objects.filter(category=category, id__gt=quest_id).exclude(id=quest_id).order_by('id').first()
        if 'skip' in request.POST:
            quest=models.Question.objects.get(id=quest_id)
            user=request.user
            answer='Question Skipped'
            models.SubAnswer.objects.create(user=user, question=quest, right_choice=answer)
            if question:
                return render(request, 'cat-questions.html', {'question':question, 'category': category})
        else:
            quest=models.Question.objects.get(id=quest_id)
            user=request.user
            answer=request.POST['answer']
            models.SubAnswer.objects.create(user=user, question=quest, right_choice=answer)
                
        if question:
            return render(request, 'cat-questions.html', {'question':question, 'category': category})
        else:
            result= models.SubAnswer.objects.filter(user=request.user)
            skipped_count=models.SubAnswer.objects.filter(user=request.user, right_choice='Question Skipped').count()
            attempted_count=models.SubAnswer.objects.filter(user=request.user).exclude(right_choice='Question Skipped').count()
            rightAnswers=0
            percentage=0
            for row in result:
                if row.question.right_option == row.right_choice:
                    rightAnswers+=1
            percentage=(rightAnswers*100)/attempted_count
            return render(request, 'result.html', {'result':result, 'total_skipped':skipped_count, 'total_attempted': attempted_count, 'rightAnswer_count': rightAnswers, 'percentage':percentage})
        
    else:
        return HttpResponse('Method not allowed!')