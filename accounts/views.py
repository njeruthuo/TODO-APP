from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_page(request):
    page = 'login'

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('mytodo:index')
        else:
            messages.error(request, "Username OR password does not exist!")

    context = {'page': page}
    return render(request, 'accounts/login-register.html', context)


def logout_page(request):
    logout(request)
    return redirect('mytodo:index')


def register_page(request):
    page = 'register'

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('mytodo:index')
        else:
            messages.error(request, "An error occured during registration. Try again later!")

    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'accounts/login-register.html', context)


def forgot_password(request):
    pass


def user_profile(request, pk):
    user = User.objects.get(id=pk)
    # blogs = user.blogs_set.all()
    context = {
        'user': user,
        # 'blogs':blogs,
    }
    return render(request, 'accounts/profile.html', context)

# def home(request):
# return render(request, 'accounts/home.html')


# def index(request):
#     return render(request, 'accounts/index.html')
