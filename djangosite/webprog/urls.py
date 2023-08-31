from django.urls import path
from . import views

app_name = 'webprog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post, name='post'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path('dashboard/', views.dashboard, name='dashboard')
]
