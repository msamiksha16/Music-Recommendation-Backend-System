from django.urls import path
from .views import UserProfileCreateView, UserProfileDetailView, UserCreateUpdateView, UserRetrieveView

urlpatterns = [
    path('', UserProfileCreateView.as_view(), name='create-user'),
    path('<int:id>/', UserProfileDetailView.as_view(), name='get-user'),
    path("", UserCreateUpdateView.as_view(), name="user-create-or-update"),      # POST /users/
    path("<int:id>/", UserRetrieveView.as_view(), name="user-retrieve"), 
     
   

]