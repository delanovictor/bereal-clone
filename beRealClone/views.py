from rest_framework import viewsets
from beRealClone.models import *
from beRealClone.serializer import *
from rest_framework.decorators import action

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        queryset = Post.objects.all()

        user_id = self.request.query_params.get('user')
        
        if user_id is not None:
            queryset = queryset.filter(user=user_id)
            
        return queryset

