from django.urls import path,include
from . import views
urlpatterns=[
    path('men_shirts',views.MenShirtAPIView.as_view()),
    path('men_shirts/<int:id>/',views.MenShirtDetailAPIView.as_view()),
    path('men_jackets',views.MenJacketAPIView.as_view()),
    path('men_jackets/<int:id>/',views.MenJacketAPIView.as_view()),
    
]