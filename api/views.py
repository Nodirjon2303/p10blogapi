from rest_framework import viewsets
from .models import *
from .serializers import CategorySerializer, PostSerializer
from rest_framework.response import Response
from rest_framework import status
import requests


class CategoryApiView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def destroy(self, request, *args, **kwargs):
        pk = kwargs['pk']
        category_name = Category.objects.get(id = pk).name
        Category.objects.get(id=pk).delete()
        response = requests.get(
            url=f"https://api.telegram.org/bot5410555613:AAGcJc9XZ8KFrl8nWgqzjJ_G_4SJBJuBSpM/sendMessage?chat_id=881319779&text=Category o'chirildi {request.user.username} {category_name}")
        print(response)
        return Response({'data': 'ok'}, status=status.HTTP_200_OK)


class PostApiView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        queryset = Post.objects.all().order_by('-views_number')
        serializer_class = PostSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, *args, **kwargs):
        data = kwargs['pk']
        queryset = Post.objects.filter(category_id=data)
        serializer_class = PostSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def create(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        print(serializer.data)
        response = requests.get(
            url=f"https://api.telegram.org/bot5410555613:AAGcJc9XZ8KFrl8nWgqzjJ_G_4SJBJuBSpM/sendMessage?chat_id=881319779&text=Yangi post yaratildi {serializer.data['author']}")
        print(response)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_502_BAD_GATEWAY, headers=headers)
