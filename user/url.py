from django.urls import path
from user.views import *

urlpatterns = [
    path('login/', login_view),
    path('register/', register_view)

]
