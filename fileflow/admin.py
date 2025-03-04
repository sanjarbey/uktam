from django.contrib import admin
from .models import Friend, Partner, Position, Employee, Person,PersonDetails

# Register Friend model
@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'surename', 'type', 'status')
    search_fields = ('firstname', 'lastname', 'surename', 'type')
    list_filter = ('status',)

# Register Partner model
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'surename', 'type', 'status')
    search_fields = ('firstname', 'lastname', 'surename', 'type')
    list_filter = ('status',)

# Register Position model
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'department', 'created_at', 'updated_at')
    search_fields = ('title', 'level', 'department')
    list_filter = ('level', 'department')
    ordering = ('title',)

# Register Employee model
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'surename', 'position', 'status')
    search_fields = ('firstname', 'lastname', 'surename', 'position__title')
    list_filter = ('status', 'position')
    autocomplete_fields = ('position',)





# Register Person model
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'surename', 'type', 'send', 'sendstatus', 'created_at', 'updated_at', 'is_published')
    search_fields = ('firstname', 'lastname', 'surename', 'type')
    list_filter = ('send', 'sendstatus', 'is_published')
    autocomplete_fields = ( 'friend', 'partner')
    list_editable = ('is_published',)
    # inlines = [PersonDetailsInline]  # PersonDetails ni Person sahifasiga qo‘shish


# # PersonDetailsni Person sahifasida ko‘rsatish
# class PersonDetailsInline(admin.TabularInline):  
#     model = PersonDetails
#     extra = 1  # Qo‘shimcha bo‘sh joy ajratish

# # PersonDetails uchun admin ro‘yxatga olish
# @admin.register(PersonDetails)
# class PersonDetailsAdmin(admin.ModelAdmin):
#     list_display = ('person', 'el1', 'el2', 'created_at', 'updated_at')
#     list_filter = ('created_at', 'updated_at')


# from .models import PersonDetails

@admin.register(PersonDetails)
class PersonDetailsAdmin(admin.ModelAdmin):
    list_display = ('person', 'el1', 'el2', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('person__firstname', 'person__lastname')