from django.shortcuts import render,redirect
from .models import TodoList, Category
from django.contrib import messages
from .forms import UserRegisterForm

def index(request): #the index view
    if request.user.is_authenticated == True:
        todos = TodoList.objects.filter(user=request.user) #quering all todos with the object manager
        categories = Category.objects.all() #getting all categories with object manager
        if request.method == "POST": #checking if the request method is a POST
            if "taskAdd" in request.POST: #checking if there is a request to add a todo
                print(dict(request.POST))
                title = request.POST["description"] #title
                date = str(request.POST["date"]) #date
                category = request.POST["category_select"] #category
                content = title + " -- " + date + " " + category #content
                Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category), user=request.user)
                Todo.save() #saving the todo
                return redirect("/") #reloading the page
            if "taskDelete" in request.POST: #checking if there is a request to delete a todo
                print(request.POST)
                print(request.POST['checkedbox'])
                print(request.POST.get('checkedbox'))
                checkedlist = request.POST.getlist('checkedbox') #checked todos to be deleted
                for todo_id in checkedlist:
                    todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
                    todo.delete() #deleting todo
        # print(dict(request.POST))
        print(request.user)
        return render(request, "index.html", {"todos": todos, "categories":categories})
    else:
        return redirect("register")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})