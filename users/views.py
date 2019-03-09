from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

class BaseView(View):
    pass


class LoginView(BaseView):
    def get(self, request):
        return render(request, 'pages/login.html')

    def post(self, request):
        # Login user
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('books:index')
        else:
            context = {'username': username, 'password': password}
            messages.error(request, 'Invalid username or password.')
            # return redirect('users:login')
            return render(request, 'pages/login.html', context)


class RegisterView(BaseView):
    def get(self, request):
        return render(request, 'pages/register.html')

    def post(self, request):

        # Getting form values

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check if passwords match !
        if password1 == password2:
            # Check if user already exists !
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('users:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                else:
                    # Looks Good !!
                    user = User.objects.create_user(username=username, password=password1, email=email,
                                                    first_name=first_name, last_name=last_name)
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in.')
                    # return redirect('/')
                    user.save()
                    messages.success(request, 'You are now registerd and can log in.')
                    return redirect('users:login')
        else:
            messages.error(request, 'Passwords don\'t match')
            return redirect('users:register')
