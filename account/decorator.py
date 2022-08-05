from django.shortcuts import render

def check_authenticate(myfun):
    def inner(request):
        if request.user.is_authenticated:
            return render(request,'account/home.html')

        else:
            return myfun(request)
    return inner
