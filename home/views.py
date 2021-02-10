from django.shortcuts import render, redirect, reverse

def index(request):
    if request.user.is_authenticated:
        user = request.user
        context={'user': user }
        return render(request, 'home.html', context)
    else: 
        return redirect(reverse('account_login'))

def upload_new_image(request):
    print("HELLLLLO")
    print(request.POST)