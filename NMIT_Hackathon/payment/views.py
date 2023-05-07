from django.http import JsonResponse
from django.shortcuts import render, redirect
from student.models import StudentInfo
from .models import CardDetails

class View:
    def __init__(self) -> None:
        self.card_id = ""

    def set_card_id(self, request, id):
        self.card_id = id
        return JsonResponse({'card_id': self.card_id})
    
    def get_card_id(self, request):
        return JsonResponse({'card_id': self.card_id})

    def index(self, request):
        content = CardDetails.objects.all().values()
        return JsonResponse({'status':'successful', 'content': list(content)})
    
    def pay(self, request, amount):
        if (self.card_id != ""):
            customer = CardDetails.objects.get(card_id=self.card_id)
            if (customer.balance >= amount):
                customer.balance -= amount
                customer.save()
                return JsonResponse({'status': 'successful', 'amount': customer.balance})
            else:
                return JsonResponse({'status': 'unsuccessful', 'amount': customer.balance})
        else:
            return JsonResponse({'status': 'unsuccessful', 'content': 'card_id not set'})
    
    def add_money(self, request, amount):
        if (self.card_id != ""):
            customer = CardDetails.objects.get(card_id=self.card_id)
            customer.balance += amount
            customer.save()
            return JsonResponse({'status':'successful','amount': customer.balance})
        else:
            return JsonResponse({'status': 'unsuccessful', 'content': 'card_id not set'})
    
    def add_card(self, request):
        if not (CardDetails.objects.filter(card_id = self.card_id).exists()):
            if request.method == 'POST':
                card_no = self.card_id
                name = '314CS21056'
                print(card_no, name)

                customer = CardDetails(card_id=card_no, card_holder_name=name)
                customer.save()

                all_students = CardDetails.objects.all().values()
                print(all_students)

                return redirect('home')
            else:
                print()
                return render(request, 'card_details/add_card.html', {'card_id': self.card_id})
        else:   
            return redirect('home')


    # def add_card(self, request, name):
    #     if (self.card_id != ""):
    #         if not (CardDetails.objects.filter(card_id = self.card_id).exists()):
    #             customer = CardDetails(card_id=self.card_id, card_holder_name=name)
    #             customer.save()
    #             return JsonResponse({'details':list(CardDetails.objects.all().filter(card_id=self.card_id).values())})
    #         else:
    #             return JsonResponse({'status': 'unsuccessful', 'content': 'card_id already exists'})
    #     else:
    #         return JsonResponse({'status': 'unsuccessful', 'content': 'card_id not set'})
    
    def delete_card(self, request):
        if (self.card_id != ""):
            if (CardDetails.objects.filter(card_id = self.card_id).exists()):
                customer = CardDetails.objects.get(card_id=self.card_id)
                customer.delete()
                return JsonResponse({'status': 'successful'})
            else:
                return JsonResponse({'status': 'exists'})
        else:
            return JsonResponse({'status': 'unsuccessful', 'content': 'card_id not set'})