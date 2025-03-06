from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from fileflow.models import Employee, Friend, Partner, Person,Position

from .forms import PersonForm, FriendForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Position, Employee
from .models import Partner
from .models import PersonDetails



def home(request):
    return redirect('login')

def about(request):
    return render(request, 'about.html')

# def login(request):
    # return render(request, 'login.html')

def team(request):
    return render(request, 'team.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def services(request):
    return render(request, 'services.html')



def index(request):
    context = {'title': 'Bosh sahifa', 'greeting': 'Assalomu alaykum!'}
    return render(request, 'login.html')

@login_required
def protected_view(request):
    persons=Person.objects.all()
    employees=Employee.objects.all()
    partners=Partner.objects.all()
    friends=Friend.objects.all()
    context ={
        'employess':employees,
        'partners':partners,
        'friends':friends,
        'persons':persons,
        'user':request.user,
    }
    
    return render(request, 'protected_page.html', context)





# person model uchun
# Person uchun CRUD amallari

@login_required
def add_person(request):
    """Person qo'shish"""
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('person_list')  # Personlar ro'yxatiga qaytish
    else:
        form = PersonForm()
    return render(request, 'person_add.html', {'form': form})

@login_required
def update_person(request, pk):
    """Personni yangilash"""
    person = get_object_or_404(Person, pk=pk)  # Personni olish
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_list')  # Personlar ro'yxatiga qaytish
    else:
        form = PersonForm(instance=person)
    return render(request, 'person_update.html', {'form': form})

@login_required
def delete_person(request, pk):
    """Personni o'chirish"""
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')  # Personlar ro'yxatiga qaytish
    return render(request, 'person_delete.html', {'person': person})



@login_required
def person_list(request):
     # Qidiruv filtrlarining qiymatlari
    firstname_query = request.GET.get('firstname', '')
    lastname_query = request.GET.get('lastname', '')
    surename_query = request.GET.get('surename', '')
    is_published_query = request.GET.get('is_published', '')
    sendstatus_query = request.GET.get('sendstatus', '')

    # Personalarni olish
    people = Person.objects.all()

    # Filtrlash
    if firstname_query:
        people = people.filter(firstname__icontains=firstname_query)
    if lastname_query:
        people = people.filter(lastname__icontains=lastname_query)
    if surename_query:
        people = people.filter(surename__icontains=surename_query)
    if is_published_query:
        people = people.filter(is_published=is_published_query == 'true')
    if sendstatus_query:
        people = people.filter(sendstatus=sendstatus_query)

    context = {
        'people': people,
    }

    return render(request, 'person_list.html', context)


# Friend uchun CRUD amallari

# friend model uchun

@login_required
def add_friend(request):
    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            friend = form.save(commit=False)
            # friend.user = request.user  # Do'stni tizimga kirgan foydalanuvchi bilan bog'lash
            friend.save()
            return redirect('friend_list')  # Do'stlar ro'yxatiga qaytish
    else:
        form = FriendForm()
    return render(request, 'friend_add.html', {'form': form})

@login_required
def update_friend(request, pk):
    friend = get_object_or_404(Friend, pk=pk)  # Foydalanuvchiga tegishli bo'lgan do'stni olish
    if request.method == 'POST':
        form = FriendForm(request.POST, instance=friend)
        if form.is_valid():
            form.save()
            return redirect('friend_list')  # Do'stlar ro'yxatiga qaytish
    else:
        form = FriendForm(instance=friend)
    return render(request, 'friend_update.html', {'form': form})

@login_required
def delete_friend(request, pk):
    friend = get_object_or_404(Friend, pk=pk)  # Foydalanuvchiga tegishli bo'lgan do'stni olish
    if request.method == 'POST':
        friend.delete()
        return redirect('friend_list')  # Do'stlar ro'yxatiga qaytish
    return render(request, 'friend_delete.html', {'friend': friend})

@login_required
def friend_list(request):
    friends = Friend.objects.all()  # Foydalanuvchiga tegishli do'stlar ro'yxati
    return render(request, 'friend_list.html', {'friends': friends})


@login_required
def employee_list(request):
    employees=Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})        





# Position Views
class PositionListView(ListView):
    model = Position
    template_name = 'position_list.html'  # Shablon nomi
    context_object_name = 'positions'  # HTML dagi o‘zgaruvchi nomi

class PositionCreateView(CreateView):
    model = Position
    fields = ['title', 'level', 'department', 'description']
    template_name = 'position_form.html'
    success_url = reverse_lazy('position_list')

class PositionUpdateView(UpdateView):
    model = Position
    fields = ['title', 'level', 'department', 'description']
    template_name = 'position_form.html'
    success_url = reverse_lazy('position_list')

class PositionDeleteView(DeleteView):
    model = Position
    template_name = 'position_delete.html'
    success_url = reverse_lazy('position_list')

# Employee Views
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'

class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['firstname', 'lastname', 'surename', 'position', 'status']
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['firstname', 'lastname', 'surename', 'position', 'status']
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_delete.html'
    success_url = reverse_lazy('employee_list')





# Hamkorlar ro‘yxati
class PartnerListView(ListView):
    model = Partner
    template_name = 'partner_list.html'
    context_object_name = 'partners'

# Yangi hamkor qo‘shish
class PartnerCreateView(CreateView):
    model = Partner
    fields = ['firstname', 'lastname', 'surename', 'type', 'status', 'delete']
    template_name = 'partner_form.html'
    success_url = reverse_lazy('partner_list')

# Hamkorni tahrirlash
class PartnerUpdateView(UpdateView):
    model = Partner
    fields = ['firstname', 'lastname', 'surename', 'type', 'status', 'delete']
    template_name = 'partner_form.html'
    success_url = reverse_lazy('partner_list')

# Hamkorni o‘chirish
class PartnerDeleteView(DeleteView):
    model = Partner
    template_name = 'partner_delete.html'
    success_url = reverse_lazy('partner_list')




# Ro‘yxat sahifasi
class PersonDetailsListView(ListView):
    model = PersonDetails
    template_name = 'person_details_list.html'
    context_object_name = 'details'

# Qo‘shish sahifasi
class PersonDetailsCreateView(CreateView):
    model = PersonDetails
    fields = ['person', 'el1', 'el2']
    template_name = 'person_details_form.html'
    success_url = reverse_lazy('person-details-list')

# Tahrirlash sahifasi
class PersonDetailsUpdateView(UpdateView):
    model = PersonDetails
    fields = ['person', 'el1', 'el2']
    template_name = 'person_details_form.html'
    success_url = reverse_lazy('person-details-list')

# O‘chirish sahifasi
class PersonDetailsDeleteView(DeleteView):
    model = PersonDetails
    template_name = 'person_details_confirm_delete.html'
    success_url = reverse_lazy('person-details-list')

