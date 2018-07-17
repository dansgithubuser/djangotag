from django.urls import path
from . import views

urlpatterns=[
	path('player_create', views.player_create, name='player_create'),
	path('player_move', views.player_move, name='player_move'),
	path('player_get_all', views.player_get_all, name='player_get_all'),
	path('player_arena', views.player_arena, name='player_arena'),
]
