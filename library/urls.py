from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='user_login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('logout_page/', views.logout_page, name='logout_page'),
    path('create_book/', views.create_book, name='create_book'),
    path('update_book/<int:pk>/', views.update_book, name='update_book'),
    path('delete_post/<int:pk>/', views.DeletePost.as_view(), name='delete_book'),
]
