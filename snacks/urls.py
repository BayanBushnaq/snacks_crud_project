from django.urls import path
from .views import SnackListView,SnackDetailView,SnackCreateView,SnackUpdateView , SnackDeleteView
urlpatterns =[
    path('',SnackListView.as_view(), name='snack_listview'),
    path('<int:pk>/',SnackDetailView.as_view(), name='Snack_DetailView'),
    path('create/',SnackCreateView.as_view(),name = 'Snack_CreateView'),
    path('update/<int:pk>',SnackUpdateView.as_view(),name='Snack_UpdateView'),
    path('delete/<int:pk>', SnackDeleteView.as_view(),name='Snack_DeleteView' )
]