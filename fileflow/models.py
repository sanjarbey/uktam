from django.db import models
from django.contrib.auth.models import User  # Django ichki foydalanuvchi modeli

# Create your models here.

class Friend(models.Model):
    firstname = models.CharField(max_length=200)  # Ismi
    lastname = models.CharField(max_length=200)  # Familiyasi
    surename = models.CharField(max_length=200)  # Otasini ishmi
    type = models.CharField(max_length=200)  # Turi
    status = models.CharField(max_length=45, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    delete = models.CharField(max_length=45, choices=[('delete', 'Delete'), ('ondelete', 'Ondelete')], default='delete')
    created_at = models.DateTimeField(auto_now_add=True)   # Yaratilgan vaqt
    updated_at = models.DateTimeField(auto_now=True)       # Yangilangan vaqt
    
    def __str__(self):
        return self.firstname  # Admin panelda sarlavha ko'rsatiladi


class Partner(models.Model):
    firstname = models.CharField(max_length=200)  # Ismi
    lastname = models.CharField(max_length=200)  # Familiyasi
    surename = models.CharField(max_length=200)  # Otasini ishmi
    type = models.CharField(max_length=200)  # Turi
    status = models.CharField(max_length=45, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    delete = models.CharField(max_length=45, choices=[('delete', 'Delete'), ('ondelete', 'Ondelete')], default='delete')
    created_at = models.DateTimeField(auto_now_add=True)   # Yaratilgan vaqt
    updated_at = models.DateTimeField(auto_now=True)       # Yangilangan vaqt
    
    def __str__(self):
        return self.firstname  # Admin panelda sarlavha ko'rsatiladi




class Position(models.Model):
    POSITION_LEVEL_CHOICES = [
        ('JR', 'Junior'),         # Boshlang‘ich daraja
        ('MD', 'Mid-level'),      # O‘rta daraja
        ('SR', 'Senior'),         # Katta mutaxassis
        ('LD', 'Lead'),           # Jamoa yetakchisi
        ('EX', 'Executive'),      # Rahbariyat darajasi
    ]

    title = models.CharField(max_length=100)  # Pozitsiya nomi
    level = models.CharField(
        max_length=2,
        choices=POSITION_LEVEL_CHOICES,       # Tanlash uchun darajalar
        default='JR'                          # Standart daraja
    )
    department = models.CharField(max_length=100)  # Bo'lim nomi (Masalan, IT, HR)
    description = models.TextField(blank=True, null=True)  # Pozitsiya haqida batafsil ma'lumot
    created_at = models.DateTimeField(auto_now_add=True)   # Yaratilgan vaqt
    updated_at = models.DateTimeField(auto_now=True)       # Yangilangan vaqt
    status = models.CharField(max_length=45, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    delete = models.CharField(max_length=45, choices=[('delete', 'Delete'), ('ondelete', 'Ondelete')], default='delete')

    def __str__(self):
        return f"{self.title} ({self.get_level_display()})"
    

class Employee(models.Model):
    firstname = models.CharField(max_length=200)  # Ismi
    lastname = models.CharField(max_length=200)  # Familiyasi
    surename = models.CharField(max_length=200)  # Otasini ishmi
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    status = models.CharField(max_length=45, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    delete = models.CharField(max_length=45, choices=[('delete', 'Delete'), ('ondelete', 'Ondelete')], default='delete')
    created_at = models.DateTimeField(auto_now_add=True)   # Yaratilgan vaqt
    updated_at = models.DateTimeField(auto_now=True)       # Yangilangan vaqt
    def __str__(self):
        return self.firstname  # Admin panelda sarlavha ko'rsatiladi
    



class Person(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'Yangi'),          # Hujjat yangi yaratilgan
        ('IN_REVIEW', 'Ko‘rib chiqilmoqda'), # Hujjat ko‘rib chiqilayotgan holatda
        ('APPROVED', 'Tasdiqlangan'),  # Hujjat tasdiqlangan
        ('REJECTED', 'Rad etilgan'),   # Hujjat rad etilgan
    ]

    firstname = models.CharField(max_length=200)  # Ismi
    lastname = models.CharField(max_length=200)  # Familiyasi
    surename = models.CharField(max_length=200)  # Otasini ishmi
    brithday=models.DateField(null=True, blank=True) # tugulgan sanasi
    type = models.CharField(max_length=200)  # Turi
    send =  models.CharField(
        max_length=20,                       # Maksimal uzunlik
        choices=STATUS_CHOICES,              # Tanlovlar
        default='NEW'                        # Standart qiymat
    )
    senddata = models.DateTimeField(auto_now_add=True)  # Yaratilgan sana vaqti
    sendstatus= models.CharField(
        max_length=20,                       # Maksimal uzunlik
        choices=STATUS_CHOICES,              # Tanlovlar
        default='NEW'                        # Standart qiymat
    )

    employee = models.ManyToManyField(Employee, related_name='Employees') 
    friend = models.ManyToManyField(Friend, related_name='Friend') 
    partner = models.ManyToManyField(Partner, related_name='Partner') 
    created_at = models.DateTimeField(auto_now_add=True)  # Yaratilgan sana vaqti
    updated_at = models.DateTimeField(auto_now=True)  # So'nggi tahrirlangan sana vaqti
    is_published = models.CharField(max_length=45, choices=[('publish', 'Published'), ('draf', 'Draf')], default='publish')  # Nashr etilganligi

    document = models.FileField(upload_to='documents/', null=True, blank=True)  # Fayl qo'shish
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # Rasm qo'shish
    status = models.CharField(max_length=45, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    delete = models.CharField(max_length=45, choices=[('delete', 'Delete'), ('ondelete', 'Ondelete')], default='delete')

   
    def __str__(self):
        return self.firstname  # Admin panelda sarlavha ko'rsatiladi
    
class PersonDetails(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='details')  # Many-to-One bog‘lanish
    el1 = models.DecimalField(max_digits=20, decimal_places=4)  
    el2 = models.DecimalField(max_digits=20, decimal_places=4)  
    created_at = models.DateTimeField(auto_now_add=True)  # Qo‘shilgan vaqti
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"{self.person.firstname} - el1: {self.el1}, el2: {self.el2}"