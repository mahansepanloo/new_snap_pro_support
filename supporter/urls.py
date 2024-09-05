from django.urls import path
from .views import *

urlpatterrns = [
    path('Q_and_A_list/', Q_and_A_list.as_view()),
    path('Q_and_A_create/', Q_and_A_.as_view()),
    path('Q_and_A_update/<int:pk>/', Q_and_A_update.as_view()),
    path('Q_and_A_delete/<int:pk>/', Q_and_A_delete.as_view()),
    path('Q_and_A_detail/<int:pk>/', Q_and_A_detail.as_view()),
]