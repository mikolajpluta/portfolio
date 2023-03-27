from django.urls import path
from hotels.views import (
    HotelListView,
    HotelCreateView,
    HotelUpdateView,
    LoginAPIView
)

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('hotels/', HotelListView.as_view(), name='hotel-list'),
    path('hotels/admin/', HotelCreateView.as_view()),
    path('hotels/owner/<int:pk>/', HotelUpdateView.as_view()),
]