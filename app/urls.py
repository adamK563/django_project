# app/urls.py
from django.urls import path
from .views import FormView, QuestionerView, AnswersView, ClearDataView, SignUpView, CustomLoginView, CustomLogoutView, ProtectedView, HomeView

urlpatterns = [
    path('form/', FormView.as_view(), name='form_data_view'),
    path('questioner/', QuestionerView.as_view(), name='questioner_view'),
    path('answers/', AnswersView.as_view(), name='answers_view'),
    path('clear-data/', ClearDataView.as_view(), name='clear_data_view'),  
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout', kwargs={'next_page': '/home/'}),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('home/', HomeView.as_view(), name='home' )
]
