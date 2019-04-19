# Django Todolist App
This is an example Django app, it's availible to create todolist for authorization user

You can view a working version of this app
[here](https://tododjango.herokuapp.com).

## Features

-Django 2.0+

## Building

clone repository to your directory
```powershell
git clone https://github.com/Rokfordchez/todolist.git
```
It is best to use the python `virtualenv` tool to build locally:

windows
```powershell
cd ../
virtualenv -p python .
source/activate.ps1
pip install django
cd [your directory]
python manage.py runserver
```
After installation, you not need to change settings.py, all variables use BASE_DIR
Then visit `http://localhost:8000` to view the app.

## Application Code
API model of Todolist
```python
class TodoList(models.Model): #Todolist able name that inherits models.Model
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=250) # a varchar
    content = models.TextField(blank=True) # a text field
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # a foreignkey
    checkbox = models.BooleanField(default=False)
    class Meta:
        ordering = ["-created"] #ordering by the created field
    def __str__(self):
        return self.title #name to be shown when called
```

in views.py

Create Todo task:
```python
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
 ```
 
Delete todo task/tasks
```python
if "taskDelete" in request.POST: #checking if there is a request to delete a todo
    checkedlist = request.POST.getlist('checkedbox') #checked todos to be deleted
    for todo_id in checkedlist:
        todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
        todo.delete() #deleting todo
 ```
 
 Save to Todolist.checkbox value of todo without reload all page, usage ajax request
 
 in index.html
```javascript
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
<script type="text/javascript">
$(document).ready(function() {
    $('.taskCheckbox').click(function (event){
    var catid;
    catid = $(this);
    $.ajax(
    {
        type:"GET",
        url: "check/",
        data:{
                 'todo_id': catid.attr('id')
        },
     })
    });
console.log( "ready!" );
    });
```

in views.py
```python
def check(request):
    print('check')
    if request.method == 'GET':
        checked = request.GET['todo_id']
        l = TodoList.objects.get(pk=checked)  # getting the checked
        if l.checkbox == True:
            l.checkbox = False
        else:
            l.checkbox = True
        l.save()  # saving it to store in database
    # no return, goal to save value of checkbox, on page checked return with css
    pass
```

## Contacts
telegram @originalov
