from django.urls import path
from . import views
from markdown_view.views import StaffMarkdownView
urlpatterns = [
    path('', views.home, name='home'),
    path('education/', views.educational, name='educational'),
    path('launcher/', views.launcher, name='launcher'),
]
