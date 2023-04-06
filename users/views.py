from django.contrib import auth, messages
from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.urls import reverse
from products.models import Basket
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем вы успешно зарегестрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    # baskets = Basket.objects.filter(user=request.user)
    # total_summ = sum(basket.summ() for basket in baskets)
    # total_quantity = sum(basket.quantity for basket in baskets)
    # total_summ = 0
    # total_quantity = 0
    # for basket in baskets:
    #     total_summ += basket.summ()
    #     total_quantity += basket.quantity
    context = {
        'title': 'Store - Профиль',
        'form': form,
        'baskets': Basket.objects.all(),
        # 'total_summ': total_summ,
        # 'total_quantity': total_quantity,
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
