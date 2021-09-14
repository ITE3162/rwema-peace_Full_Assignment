from django.urls import path
from .views import *

urlpatterns = [
    path('register', register, name="register"),
    path('login', login, name="login"),
    path('logout', logout, name='logout'),
    path('dashboard', dashboard, name="dashboard"),
    path('create', createblog, name="create"),
    path('blogs', blogs, name="blogs"),
    path('editblog/<int:id>', postedit, name='editpost'),
]
