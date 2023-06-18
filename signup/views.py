from django.shortcuts import render, redirect
from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # ذخیره اطلاعات کاربر در پایگاه داده
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup/signup.html', {'form': form})
