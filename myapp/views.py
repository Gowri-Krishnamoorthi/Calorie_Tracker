from django.shortcuts import redirect, render
from .models import Food , Consume
# Create your views here.

def index(request):
    
    if request.method == 'POST':
       food_consumed = request.POST['food_consumed'] #namefood
       consumed = Food.objects.get(name=food_consumed)  #food object
       user = request.user

       consume = Consume(user=user, food_consumed=consumed)
       consume.save()

       foods = Food.objects.all()

    
    # Fetch consumed foods for the current user
    consumed_foods = Consume.objects.filter(user=request.user)
    foods = Food.objects.all()

    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_foods': consumed_foods})

def delete_consume(request , id):
   consumed_food = Consume.objects.get(id=id);

   if request.method == 'POST':
      consumed_food.delete()
      return redirect('/')
   
   return render(request, 'myapp/delete.html' , )
