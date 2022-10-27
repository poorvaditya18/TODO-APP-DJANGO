from django.shortcuts import render,redirect
from .models import *
# Create your views here.

# Home
def home(request):
    context={}
    if request.method == "POST":
        todo = request.POST.get('todo')
        Todo.objects.create(todo_name = todo)
        # redirect to the todo page itself
        return redirect('/')

    context['todos'] = Todo.objects.all()
    return render(request,'home.html',context)


def update_todo(request):
    id = request.GET.get('id')
    try:
        todo_obj = Todo.objects.get(id=id)
        todo_obj.is_completed = not todo_obj.is_completed
        todo_obj.save()
    except Exception as e:
        print(e)
    return redirect('/') 




def delete_todo(request,id):
    try:
        todo_obj = Todo.objects.get(id=id).delete()
    except Exception as e:
        print(e)
    return redirect('/')    
