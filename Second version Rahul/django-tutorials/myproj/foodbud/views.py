from django.shortcuts import render
from django.http import HttpResponse
from foodbud.models import Meals
# Create your views here.
price_item= {}
calories_item = {}
def index(request):
    return render(request,"index.html")

def signup(request):
    return render(request,"signup.html")

def demo(request):
    list_of_objs = Meals.objects.all()
    for meal in list_of_objs:
        if meal.category == 'veg':
            price_item.update({meal.item_name:meal.price})
            calories_item.update({meal.item_name:meal.calories})
    set_of_food_combos = []
    for value in make_food_combos(price_item,price_item.keys(),20,25,0):
        if len(set_of_food_combos) <=1000:
            if value not in set_of_food_combos and len(value)>=3:
                set_of_food_combos.append(value)
        else:
            break
    calories_fit_combos=[]
    for value in set_of_food_combos:
        if(valid_calories(value,calories_item)):
            calories_fit_combos.append(value)
    return render(request,"demo.html",{'list_of_content':calories_fit_combos})


def calorie_fitness(gender,age,calorie):
    if gender=='M':
        if (age in range(14,19) and calorie>=3200) or (age in range(18,24) and calorie>=3400) or \
                (age in range(23,31) and calorie>=3300) or (age in range(30,36) and calorie>=3000):
                return True
        else:
            return False
    if gender=='F':
        if (age in range(14,19) and calorie>=2400) or (age in range(18,24) and calorie>=2600) or \
                (age in range(23,31) and calorie>=2700) or (age in range(30,36) and calorie>=2200):
                return True
        else:
            return False


def valid_calories(list_of_items,calories_item):
    calori = 0
    for item in list_of_items:
        calori+=calories_item[item]
    return calorie_fitness('M',25,calori)

def make_food_combos(food_dict,key_list,lower_bound,upper_bound,sum):
    if upper_bound == 0:
        return
    if lower_bound <= sum <= upper_bound:
        yield[]
    if sum > upper_bound or not key_list:
        return
    for solution in make_food_combos(food_dict,key_list[1:], lower_bound, upper_bound,sum + food_dict[key_list[0]]):
        yield [key_list[0]] + solution
    for solution in make_food_combos(food_dict,key_list[1:], lower_bound, upper_bound,sum):
        yield solution

def login(request):
	return render(request,"login.html")

# def login(request):
#     return render(request,"demo.html")
