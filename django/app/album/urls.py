# urls.py
from django.urls import path
from . import views
app_name = 'album'
urlpatterns = [
    path("", views.index, name="index"),
    path('album_list/', views.album_list, name='album_list'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('add_album/', views.add_album, name='add_album'),
    path('add_photo/', views.add_photo, name='add_photo'),
    path('albums/<int:pk>/delete/', views.delete_album, name='delete_album'),  # 添加删除相册的URL配置
]
