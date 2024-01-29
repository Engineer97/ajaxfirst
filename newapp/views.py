from django.shortcuts import render
from django.views import View

# Create your views here.

from .models import Todo

from .models import datetime

from django.http import JsonResponse

import json


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

def todoToDictionary(todo:Todo) -> dict:
        result = {
                "id":todo.id,
                "userid":todo.userid,
                "title":todo.title,
                "done":todo.done,
                "regdate":todo.regdate,
                "moddate":todo.moddate,
        }

@method_decorator(csrf_exempt, name='dispatch')

class TodoView(View):
        def post(self, request):
                request = json.loads(request.body)
                userid = request["userid"]
                title = request["title"]
                

                todo = Todo()
                todo.userid = userid
                todo.title = title

                todo.save()

                todos = Todo.objects.filter(userid = userid)

                return JsonResponse({"list":list(todos.values())})
        
        def get(self, request):
                userid = request.GET["userid"]
                todos = Todo.objects.filter(userid=userid)
                return JsonResponse({"list":list(todos.values())})


