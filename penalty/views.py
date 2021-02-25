from django.shortcuts import render
from .forms import addfine
from .models import violation
from .models import vehicleinfo
from django.core.mail import send_mail
import random
# Create your views here.
def addvehicle(request):
    if request.method== "POST" :
        imf = addfine(request.POST)
        if imf.is_valid():
            imf.save()
            imf = addfine()
    else:
        imf = addfine()
    return render(request,'enroll/addvehicles.html',{'form':imf})

def viewvehicles(request):
    if request.method== "GET" :
        vio = violation.objects.all()
    else:
        vio = violation.objects.all()
    return render(request,'enroll/viewvehicles.html',{'vio':vio})

def search(request):
    if request.method == "GET":
        v1 = violation.objects.all()
        v2 = vehicleinfo.objects.all()
        s = request.GET['search']
        make=""
        colour=""
        owner=""
        for ob in v2:
            if (ob.registration_number == s):
                make=ob.make
                colour=ob.colour
                owner=ob.owner
            else:
                continue

    else:
        v1 = violation.objects.all()
    return render(request, 'enroll/search.html', {'v1': v1,'s':s,'v2':v2,'make':make,'colour':colour,'owner':owner})

def signalwise(request):
    if request.method== "GET" :
        vehicle_list1 = []
        vehicle_list2 = []
        vehicle_list3 = []
        vehicle_numbers=[]
        vehicle_string1=""
        vehicle_string2 = ""
        vehicle_string3 = ""

        v1 = violation.objects.all()
        v2 = vehicleinfo.objects.all()

        for var in v2:
            vehicle_numbers.append(var.registration_number)
        for i in range(0, 5):
            rnum1 = random.randint(0, 19)
            vehicle_list1.append(vehicle_numbers[rnum1])
            if violation.objects.filter(vehicle_number=vehicle_numbers[rnum1]):
                vehicle_string1 = vehicle_string1 + "\n" + str(vehicle_numbers[rnum1])

            rnum2 = random.randint(20, 34)
            vehicle_list2.append(vehicle_numbers[rnum2])
            if violation.objects.filter(vehicle_number=vehicle_numbers[rnum2]):
                vehicle_string2 = vehicle_string2 + "\n" + str(vehicle_numbers[rnum2])

            rnum3 = random.randint(35, 49)
            vehicle_list3.append(vehicle_numbers[rnum3])
            if violation.objects.filter(vehicle_number=vehicle_numbers[rnum3]):
                vehicle_string3 = vehicle_string3 + "\n" + str(vehicle_numbers[rnum3])




        send_mail(
            'Signal 1 -- vehicles with violation',
            vehicle_string1,
            'saipraneeth596@gmail.com',
            ['saipraneeth596@gmail.com'],
            fail_silently=False,
        )
        send_mail(
            'Signal 2 -- vehicles with violation',
            vehicle_string2,
            'saipraneeth596@gmail.com',
            ['saipraneeth596@gmail.com'],
            fail_silently=False,
        )
        send_mail(
            'Signal 3 -- vehicles with violation',
            vehicle_string3,
            'saipraneeth596@gmail.com',
            ['saipraneeth596@gmail.com'],
            fail_silently=False,
        )

        if (request.GET['signal']=="Signal 1"):
            return render(request, 'enroll/signal1.html', {'vehicle_list1': vehicle_list1,'v1':v1,'v2':v2})
        elif (request.GET['signal']=="Signal 2"):
            return render(request, 'enroll/signal2.html', {'vehicle_list2': vehicle_list2,'v1':v1,'v2':v2})
        else:
            return render(request, 'enroll/signal3.html', {'vehicle_list3': vehicle_list3, 'v1': v1, 'v2': v2})

    else:
        v1 = violation.objects.all()


