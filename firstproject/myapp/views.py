from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from datetime import datetime

def hello1(request):
    now = datetime.now()


    food1 = {'name':'蝦仁滑蛋','price':180,'comment':'好吃','is spicy':False}
    food2 = {'name':'蒜泥白肉','price':160,'comment':'人氣推薦','is spicy':True}
    food3 = {'name':'貴妃醉雞','price':200,'comment':'主廚推薦','is spicy':False}
    foods = [food1,food2,food3]
    return render(request ,"menu.html" ,locals())