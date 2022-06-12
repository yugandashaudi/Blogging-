from django.urls import path
from .views import *

urlpatterns=[
    path('',GetPracticalTherapyPostView.as_view(),name='getpraticaltherapy'),
    path('create_pratical/',CreatePracticalTherapyPostView.as_view(),name='createpraticaltherapy'),
    path('update_pratical/<int:pk>/',UpdatePraticalTherapyPostView.as_view(),name='update_pratical'),
    path('retrive_pratical/<int:pk>/',RetrivePraticalTherapyPostView.as_view(),name='retrive_pratical'),
    path('delete_pratical/<int:pk>/',DestroyPraticalTherapyPostView.as_view(),name='delete_pratical'),
    path('listaction_radio/',ListRadioTherapyPostView.as_view(),name='listaction_radion'),
    path('action_radio/<int:pk>/',ActionRadioTherapyPostView.as_view(),name='action_radio'),
    path('listaction_emerging/',ListActionEmergencyTherapyView.as_view(),name='listaction_emerging'),
    path('particularaction_emerging/<int:pk>/',ParticularActionEmergingTherapay.as_view(),name='particularaction_emerging'),
    path('listaction_diagonistic/',ListDiagonisticImagingTherapyView.as_view(),name='listaction_diagonistic'),
    path('particularaction_diagonistic/<int:pk>/',ActionDiagonisticImagingTherapyView.as_view(),name='particularaction_diagonistic'),
    path('listaction_nuclear/',ListNuclearMedicineTherapyView.as_view(),name='listaction_diagonistic'),
    path('particularaction_nuclear/<int:pk>/',ActionNuclearMedicineTherapyView.as_view(),name='particularaction_diagonistic'),
    
]
    
