from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from .models import TotalClasses
from student.models import StudentInfo
from payment.models import CardDetails

# def add_class(request):
#     data = TotalClasses.objects.get(dept='CSE', sem='1')
#     print(data.total_classes)
#     return render(request, 'attendence/add_class.html')

def add_class(request):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'staff':
            if request.method == 'POST':
                dept = request.POST.get('dept')
                sem = request.POST.get('sem')

                prev_total_classes = TotalClasses.objects.get(dept=dept, sem=sem)
                total_classes = prev_total_classes.total_classes + 1
                TotalClasses.objects.filter(dept=dept, sem=sem).update(total_classes=total_classes)
            
                return redirect(reverse('home'))
            else:
                return render(request, 'attend/add_class.html')
        else:
            return redirect('home')
    else:
        return redirect('index')
    
def attend(request, key, card_id):
    if key == 11223344:
        if CardDetails.objects.filter(card_id=card_id).exists():
            card_holder = CardDetails.objects.get(card_id=card_id).card_holder_name

            student = StudentInfo.objects.get(std_reg_no = card_holder)
            attend = student.std_class_attended + 1
            StudentInfo.objects.filter(std_reg_no = card_holder).update(std_class_attended = attend)

            return JsonResponse({'status': 'successful', 'card_id': card_id})
        else:
            return JsonResponse({'status': 'unsuccessful', 'card_id': card_id})
        
def add_clas1s(request):
    a = TotalClasses.objects.get(dept='CSE', sem='1')
    print(a.total_classes)

    return render(request, 'attend/add_class.html')