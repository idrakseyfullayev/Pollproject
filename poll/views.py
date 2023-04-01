from django.shortcuts import render, HttpResponse, redirect, get_list_or_404
from django.views import generic
from poll.models import QuestionModel, ChoiceModel, PollModel
from account.models import Account
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

class IndexView(generic.View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            questions = QuestionModel.objects.all()
            
            context = {
                "questions": questions,
            }
            return render(request, "index.html", context)
            
        return render(request, "index.html")
    
    
    def post(self, request, *args, **kwargs):
        question_ids = []
        answer_ids = []
        print(request.POST)

        for i in request.POST:
            if i.startswith('question'):
                question_ids.append(request.POST[i])
            elif i.startswith('answer'):
                answer_ids.append(request.POST[i])

        print(question_ids, answer_ids)


        for i in range(len(answer_ids)):
            # question = QuestionModel.objects.get(id=question_ids[i])
            # print(question)
            answer = ChoiceModel.objects.get(id=answer_ids[i])
            question = answer.question
            print(answer)
            print(question)

        
            if request.user.is_authenticated:
                PollModel.objects.create(user = request.user, question = question, answer = answer)
                user = User.objects.get(username = request.user.username)
                account_user = Account.objects.get(user = user)

                if answer.is_true == True:
                    account_user.cor_uns_number += 1
                    account_user.save()
                else:
                    account_user.uncur_uns_number += 1
                    account_user.save()  
            
        return redirect("poll:index")
    

