"""
URL configuration for myforum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import path


#urlpatterns = [
 #   path('admin/', admin.site.urls),
#]

from django.urls import path
#from .views import forum
from forum.views import ThreadListView, ThreadDetailView, CreateThreadView, CreatePostView

urlpatterns = [
    path('', ThreadListView.as_view(), name='thread_list'),
    path('thread/<int:pk>/', ThreadDetailView.as_view(), name='thread_detail'),
    path('thread/create/', CreateThreadView.as_view(), name='create_thread'),
    path('thread/<int:pk>/post/', CreatePostView.as_view(), name='create_post'),
]

