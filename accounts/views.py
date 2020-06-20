from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect
from .forms import loginForm, registerForm, UpdateProfileForm
from django.http import HttpResponse
from shop.models import shops
from django.contrib.auth.models import User
# email
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# Create your views here.


def login_view(request):
    form = loginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
            # A backend authenticated the credentials
        elif not user:
            # No backend authenticated the credentials
            context['message'] = "ያስገቡት ኢሜይል ወይም የይለፍ ቃል የተሳሳተ ነው "
            context['form'] = loginForm()
        elif not user.is_active:
            context['message'] = "የኢሜይል አድራሻዎን አላረጋገጡም። ወደ ኢሜይል አድራሻዎ በመሄድ ያረጋግጡ  "
            context['form'] = loginForm()

    return render(request, "login.html", context)


def logout_view(request):
    logout(request)
    return redirect("/profile/login/")


def register_view(request):
    form = registerForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        firstName = form.cleaned_data.get('firstName')
        lastName = form.cleaned_data.get('lastName')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(email, email, password)
        new_user.first_name = firstName
        new_user.last_name = lastName
        new_user.is_active = False
        new_user.save()
        to_email = form.cleaned_data.get('email')
        send_mail(
            'Subject here',
            'Here is the message.',
            'matrixsoftethiopia@example.com',
            [to_email],
            fail_silently=False,
        )
        return HttpResponse('We have sent you an email, please confirm your email address to complete registration')
    else:
        form = registerForm()
    return render(request, "register.html", context)


def base_layout_view(request):
    return render(request, "base_layout.html")


def user_page_view(request):
    return render(request, "user-page.html")


def get_user_order(request):
    order = orders.objects.filter(user=request.user)
    if order.exists():
        return order[0]
    return 0


def order_given(request, **kwargs):
    existing_order = get_user_order(request)
    shop = shops.objects.get(owner=request.user)
    context = {
        'order': existing_order,
        'shop': shop
    }
    return render(request, 'order-given.html', context)


def order_received(request, **kwargs):
    existing_order = orders.objects.all()
    filtered_shop = shops.objects.get(owner=request.user)
    context = {
        'order2': existing_order,
        'shop': filtered_shop
    }
    return render(request, 'order-received.html', context)


def update_profile(request):
    update_user = User.objects.get(username=request.user.username)
    message = ""
    if request.method == 'POST':
        update_user.first_name = request.POST.get('firstname')
        update_user.last_name = request.POST.get('lastname')
        update_user.save()
        message = "√ በተሳካ ሁኔታ ቀይረዋል"
    context = {
        'firstname': update_user.first_name,
        'lastname': update_user.last_name,
        'message': message
    }
    return render(request, 'edit-user.html', context)
