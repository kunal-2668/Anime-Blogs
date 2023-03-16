from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog,Contact,Profile_photo
from .forms import Addblog
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_control

# Create your views here.

def home(request):
    blog = Blog.objects.filter(status=True).order_by('?')
    userblog = Blog.objects.filter(Your_Name=request.user)
    return render (request, 'hometemp.html',{'blog':blog,'userblog':userblog})


def readmore(request,id):
    if request.user.is_authenticated:
        j = Blog.objects.get(id=id)
        return render (request, 'readmore.html',{'j':j})
    else:
        return redirect('login')


def search(request):
    searchinput = request.POST['search']
    if Blog.objects.filter(Title__contains = searchinput).exists():
        blog = Blog.objects.filter(Title__contains = searchinput)
        return render (request, 'hometemp.html',{'blog':blog})
    else:
        messages.info(request,"No Search Results")
        return redirect('home')


def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('main')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('main')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                return redirect('main')
        else:
            messages.info(request,'Try Matching Password')
            return redirect('home')
    else:
        return render(request,'index.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.method == "POST":
        username = request.POST['lusername']
        password = request.POST['lpassword']

        user = auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid username/password')
            return redirect('login')
    else:
        return render(request,'main.html')

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def logout(request):
#     request.session.flush()
#     if hasattr(request, 'user'):
#         from django.contrib.auth.models import AnonymousUser
#         request.user = AnonymousUser()
#         return redirect('login')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    auth.logout(request)
    return redirect('home')


@login_required(login_url='login')
def addblog(request):
    if request.method == "GET":
        form = Addblog()
        return render(request,'addblog.html',{'form':form})
    else:
        form = Addblog(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Your Blog will get Inspected by Admin, It will be Published Soon!")
            return redirect('home')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def main(request):
    return render (request, 'main.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        address = request.POST['address']
        data = Contact(name=name,email=email,number=number,address=address)
        data.save()

        return redirect("home")


def blogsingle(request,id):
    data = Blog.objects.get(id = id)
    return render(request,'create.html',{'j':data})


def pdfcreate(request,id):
    data = Blog.objects.get(id = id)
    template_path = 'create.html'
    context = {'j': data}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{data.Title}.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@login_required(login_url='adminlogin')
def Edit(request):
    blog = Blog.objects.all()
    return render(request,'admin_panel.html',{'blog':blog})


def edit_blog(request,id):
    if request.method == "GET":
        data = Blog.objects.get(id=id)
        form = Addblog(instance=data)
        return render(request,'addblog.html',{'form':form})
    else:
        data = Blog.objects.get(id=id)
        form = Addblog(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('Edit')


def delete_blog(request,id):
    data = Blog.objects.get(id=id)
    data.delete()
    return redirect('Edit')


def Contacts(request):
    contacts = Contact.objects.all()
    return render(request,'contacts.html',{'data':contacts})


def adminlogin(request):
    if request.method == "POST":
        username = request.POST['lusername']
        password = request.POST['lpassword']
        admin ="admin"
        user = auth.authenticate(username='admin',password=password)
        User.objects.filter(username='admin').exists()
        print(user)
        if username is admin:
            auth.login(request,user)
            return redirect('admin_panel')
        else:
            messages.info(request,'Invalid username/password')
            return redirect('home')
    else:
        return render(request,'admin_panellogin.html')


def signupform(request):
    if request.method == 'GET':
        form = UserCreationForm
        return render (request,'test.html',{'form':form})

    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        return redirect('signupform')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


def loginform(request):
    try:
        if request.method == 'GET':
            form = AuthenticationForm(request)
            return render (request,'test.html',{'form':form})

        else:
            form = AuthenticationForm(request ,data=request.POST or None)
            if form.is_valid():
                user = form.get_user()
                print(user)
                auth.login(request,user)
                return redirect('home')
            messages.info(request,'Invalid username/password')
            return redirect('loginform')

    except Exception as e:
        print(e)
        return HttpResponse(e)


def add_profile_photo(request):
    if request.user.is_authenticated:
        if Profile_photo.objects.filter(user_name__exact=request.user).exists():
            return redirect('Profile')
        elif request.method == "POST":
            user_name = request.user
            profile = request.FILES['profile']

            Profile_photo.objects.create(user_name=user_name,profile=profile)

            return redirect('Profile')
        else:
            return render(request,'add_profile_photo.html')
    else:
        return redirect('main')

def showprofile_photo(request):
    if request.user.is_authenticated:
        if Profile_photo.objects.filter(user_name__exact=request.user).exists():
            data = Profile_photo.objects.get(user_name__exact=request.user)
            blog = Blog.objects.filter(Your_Name__exact=request.user)
            return render(request,'Profile.html',{'data':data,'blog':blog})
        else:
            return redirect('addprofile')
    else:
        return redirect('main')


def update_profile(request,id):
    if Profile_photo.objects.filter(user_name__exact=request.user).exists():
            photo = Profile_photo.objects.get(id = id)
            if request.method == "POST":
                profile = request.FILES['profile']
                Profile_photo(id=id,user_name=photo.user_name,profile=profile).save()
                return redirect('Profile')
            else:
                return render(request,'add_profile_photo.html')

    else :
        return redirect('addprofile')
    


def filter(request,query):
    blog = Blog.objects.filter(status=True).order_by(query)
    return render (request, 'hometemp.html',{'blog':blog})