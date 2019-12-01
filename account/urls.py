from .views import log_in, log_out, signup
from django.urls import path

app_name = 'account'
urlpatterns = [
    path('', log_in, name='main'),
    path('logout/', log_out, name='logout'),
    path('signup/', signup, name='signup')
]
