from django.urls import path
from .views import profile, home, createMatkul, viewMatkul,viewMatkulDetail, deleteView
#url for app
urlpatterns = [
    path('story-3/', profile, name='profile'),
    path('', home, name='home'),
    path('create-matkul/', createMatkul, name="create_matkul"),
    path('view-matkul/', viewMatkul, name="view_matkul"),
    path('view-matkul/<int:id>', viewMatkulDetail, name="detail_matkul"),
    path('view-matkul/<int:id>/delete', deleteView, name="delete_matkul"),
]