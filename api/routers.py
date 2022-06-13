from rest_framework import routers
from .views import CategoryApiView, PostApiView
routers = routers.DefaultRouter()

routers.register(r'category', CategoryApiView)
routers.register(r'posts', PostApiView)
