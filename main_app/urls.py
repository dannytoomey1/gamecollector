from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('games/', views.games_index, name='index'),
  path('games/<int:game_id>/', views.games_detail, name='detail'),
  path('games/create/', views.GameCreate.as_view(), name='games_create'),
  path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
  path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
  path('games/<int:game_id>/add_playtime/', views.add_playtime, name='add_playtime'),
  path('games/<int:game_id>/assoc_dev/<int:dev_id>/', views.assoc_dev, name='assoc_dev'),
  path('games/<int:game_id>/unassoc_dev/<int:dev_id>/', views.unassoc_dev, name='unassoc_dev'),
  path('devs/', views.DevList.as_view(), name='devs_index'),
  path('devs/<int:pk>/', views.DevDetail.as_view(), name='devs_detail'),
  path('devs/create/', views.DevCreate.as_view(), name='devs_create'),
  path('devs/<int:pk>/update/', views.DevUpdate.as_view(), name='devs_update'),
  path('devs/<int:pk>/delete/', views.DevDelete.as_view(), name='devs_delete'),
]