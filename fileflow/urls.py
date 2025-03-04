# from django.urls import path
# from . import views  # views.py dan funksiyalarni import qilish

# urlpatterns = [
#     path('', views.home, name='home'),  # Asosiy sahifa (localhost:8000/)
#     
    
   
# ]

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import (
    PositionListView, PositionCreateView, PositionUpdateView, PositionDeleteView,
    EmployeeListView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView
)

from .views import (
    PartnerListView, PartnerCreateView, PartnerUpdateView, PartnerDeleteView
)


from .views import (
    PersonDetailsListView, 
    PersonDetailsCreateView, 
    PersonDetailsUpdateView, 
    PersonDetailsDeleteView
)

urlpatterns = [
     # Login sahifasi
    path('login/', LoginView.as_view(template_name='login.html', next_page='protected'), name='login'),
    # Logout
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('', views.index, name='login'),
    path('login/', views.login, name='login'),  # localhost:8000/login/
    path('about/', views.about, name='about'),  # localhost:8000/about/
    path('team/', views.team, name='team'),  # localhost:8000/team/
    path('contact/', views.contact, name='contact'),  # localhost:8000/contact/
    path('services/', views.services, name='services'),  # localhost:8000/services/
]

urlpatterns += [
    path('protected/', views.protected_view, name='protected'),


    # Do'stlar uchun URL'lar
    path('friends/', views.friend_list, name='friend_list'),
    path('friends/add/', views.add_friend, name='add_friend'),
    path('friends/update/<int:pk>/', views.update_friend, name='update_friend'),
    path('friends/delete/<int:pk>/', views.delete_friend, name='delete_friend'),

    # Personlar uchun URL'lar
    path('persons/', views.person_list, name='person_list'),
    path('persons/add/', views.add_person, name='add_person'),
    path('persons/update/<int:pk>/', views.update_person, name='update_person'),
    path('persons/delete/<int:pk>/', views.delete_person, name='delete_person'),
]


urlpatterns += [
    # Position URLs
    path('position/', PositionListView.as_view(), name='position_list'),
    path('position/add/', PositionCreateView.as_view(), name='position_add'),
    path('position/<int:pk>/update/', PositionUpdateView.as_view(), name='position_update'),
    path('position/<int:pk>/delete/', PositionDeleteView.as_view(), name='position_delete'),

    # Employee URLs
    path('employee/', EmployeeListView.as_view(), name='employee_list'),
    path('employee/add/', EmployeeCreateView.as_view(), name='employee_add'),
    path('employee/<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
]





urlpatterns += [
    path('partner/', PartnerListView.as_view(), name='partner_list'),
    path('partner/add/', PartnerCreateView.as_view(), name='partner_add'),
    path('partner/<int:pk>/update/', PartnerUpdateView.as_view(), name='partner_update'),
    path('partner/<int:pk>/delete/', PartnerDeleteView.as_view(), name='partner_delete'),
]





urlpatterns += [
    path('person-details/', PersonDetailsListView.as_view(), name='person-details-list'),
    path('person-details/add/', PersonDetailsCreateView.as_view(), name='person-details-add'),
    path('person-details/<int:pk>/update/', PersonDetailsUpdateView.as_view(), name='person-details-update'),
    path('person-details/<int:pk>/delete/', PersonDetailsDeleteView.as_view(), name='person-details-delete'),
]



