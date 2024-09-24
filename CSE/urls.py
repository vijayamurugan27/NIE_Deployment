
from django.urls import path
from CSE import views
from CSE.views import StuList, Forms, StudentDetail, StudentUpdate, StudentDelete

app_name = 'CSE'

urlpatterns = [
    path('index', views.index, name='home'),
    path('index', views.index, name='index'),
    path('products', views.products, name='products'),
    path('service', views.service, name='service'),
    path('contacts', views.contacts, name='contacts'),
    path('basic', views.basic, name='basic'),

    # CBV
    path('', StuList.as_view(), name='list'),
    path('forms', Forms.as_view(), name='forms'),
    path('<pk>/detail', StudentDetail.as_view(), name='detail'),
    path('<pk>/update', StudentUpdate.as_view(), name='update'),
    path('<pk>/delete', StudentDelete.as_view(), name='delete'),

    # FBV
    path('student', views.student, name='student'),  # Only keep one
    path('form', views.form, name='form'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),

    ###GET and POST

    path('nie',views.nie, name = 'nie'),
    path('add', views.add, name = 'add'),
    path('add1', views.add1, name = 'add1'),

    # login, logout, user registration
    path('register', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login'),
    path('logout', views.logoutuser, name = 'logout'),

]
