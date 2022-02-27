from django.urls import path

from music_app.main.views import show_index, show_album_details, show_album_edit, show_album_delete, \
    show_profile_details, show_profile_delete, show_album_create

urlpatterns = (
    path('', show_index, name='show index'),
    path('album/add/', show_album_create, name='show album create'),
    path('album/details/<int:pk>/', show_album_details, name='show album details'),
    path('album/edit/<int:pk>/', show_album_edit, name='show album edit'),
    path('album/delete/<int:pk>/', show_album_delete, name='show album delete'),
    path('profile/details/', show_profile_details, name='show profile details'),
    path('profile/delete/', show_profile_delete, name='show profile delete'),
)
