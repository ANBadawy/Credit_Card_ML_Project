from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.predict_credit_approval, name='predict_credit_approval'),
]
