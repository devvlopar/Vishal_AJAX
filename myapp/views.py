from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.
def index(request):
    u_list = User.objects.all()
    return render(request, 'index.html', {'users': u_list})


def create_data(request):
    User.objects.create(
    
        first_name = request.POST['f_name'], #f_name : d1 object jo bananya uski key hai
        last_name = request.POST['l_name'],
        email = request.POST['email'],
        mobile = request.POST['mobile']
    )
    all_u = list(User.objects.values())
    print(all_u)
    return JsonResponse({'alldata': all_u})
    
    
    