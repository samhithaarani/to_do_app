from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import todo_item
def viewtodo(request):
    #rendering all objects from database giver by user
    all_items=todo_item.objects.all()
    #displaying items in todo.html
    return render(request,'todo.html',{"items":all_items})
def addtodo(request):
    #taking input from user
    user_item=request.POST['content']
    #saving to our db
    adding=todo_item(content=user_item)
    adding.save()
    #redirect to view todo
    return HttpResponseRedirect('viewtodo')
def deltodo(request,todo_id):
    #getting element from id genarated in todo.html
    del_element=todo_item.objects.get(id=todo_id)
    #deleting del_element
    del_element.delete()
    #redirects to view todo
    return HttpResponseRedirect("viewtodo")




# Create your views here.
