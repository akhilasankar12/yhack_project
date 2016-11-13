from django.shortcuts import render
from django.http import HttpResponse
from foodbud.models import User

def index(request):
    return render(request,"index.html")

def initialInfo(request):
	if request.method == 'GET':
		return render(request,"initial-info.html")
	elif request.method == 'POST':
		formDict = {}
		formDict['budget'] = request.POST.get('budget','')
		formDict['days'] = request.POST.get('days','')
		formDict['gender'] = request.POST.get('gender','')
		formDict['age'] = request.POST.get('age','')
		formDict['vegetarian'] = request.POST.get('vegetarian','')
		#mealPlan = generate_meal_plan(formDict)
		return render(request,"meal-plan.html",formDict)

