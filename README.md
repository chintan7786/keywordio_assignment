# keywordio_assignment

## Created A Library management website

Steps followed by me in sequence.

### Step 1:
Connected it to MySQL data base in settings.py file.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'keywordio',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'YOUR_PASSWORD',
    }
}
```

Created one user defined model **Book** and Used predefine **User** model in it.

Book:

|Cols     |
|---------|
|book_name|
|author   |

Used following columns from User model:

|Cols       |
|---------  |
|username   |
|password   |
|first_name |
|group      |


### Step 2:
Created two groups **Admin** and **Student** and wrote following code in _decorators.py_ file

```
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not allowed to use  this page')
        return wrapper_func
    return decorator
```


### Step 3:
Created Login and Regiteration pages.


### Step 4:
Created FrontEnd with bootstrap and html and added following task in Backend _views.py_ file
- For Admin
    - Create book entry from index.html page
    - View all book entries in index.html
    - Can Update and Delete each book entry
- For Student
    - Can view all the books entry in index.html page
