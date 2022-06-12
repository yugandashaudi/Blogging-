from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin
from rest_framework.permissions import IsAuthenticated



class GetPracticalTherapyPostView(GenericAPIView,ListModelMixin):
    queryset = Post.objects.filter(post_type="PT")
    serializer_class = GetPostSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    

class CreatePracticalTherapyPostView(GenericAPIView,CreateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset=Post.objects.all() 
    serializer_class = CreatePostSerializer

    

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def perform_create(self,serializer):
        serializer.save(associated_user=self.request.user,post_type="PT")    


class RetrivePraticalTherapyPostView(GenericAPIView,RetrieveModelMixin):
    permission_classes = [IsAuthenticated] 
    queryset = Post.objects.filter(post_type="PT")   
    serializer_class = GetPostSerializer   

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class UpdatePraticalTherapyPostView(GenericAPIView,UpdateModelMixin):
    permission_classes = [IsAuthenticated]     
    queryset = Post.objects.filter(post_type="PT")
    serializer_class = CreatePostSerializer

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)


class DestroyPraticalTherapyPostView(GenericAPIView,DestroyModelMixin):
    permission_classes = [IsAuthenticated]       
    queryset = Post.objects.filter(post_type="PT")
    serializer_classes = GetPostSerializer
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
class ListRadioTherapyPostView(GenericAPIView,ListModelMixin,CreateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.filter(post_type='RT')
    def get_serializer_class(self):
        if self.request.method == ("GET" or "POST"):
            print('it is working fine')
            return GetPostSerializer
        return CreatePostSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)  

    def create(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)     


class ActionRadioTherapyPostView(GenericAPIView,
RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.filter(post_type='RT')
    def get_serializer_class(self):
        if self.request.method == "GET" or "POST" or "DELETE":
            print('it is working fine')
            return GetPostSerializer
        return CreatePostSerializer

    

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)

    def update(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

    

class ListActionEmergencyTherapyView(GenericAPIView,ListModelMixin,CreateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.filter(post_type='ET')
    def get_serializer_class(self):
        if self.request.method == "GET" or "POST":
            return GetPostSerializer

        return CreatePostSerializer  

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)  

    def create(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)     

class ParticularActionEmergingTherapay(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    permission_classes = [IsAuthenticated] 
    queryset = Post.objects.filter(post_type="ET") 
    def get_serializer_class(self):
        if self.request.method == "GET" or "POST":
            return GetPostSerializer

        return CreatePostSerializer  
    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)

    def update(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    






class ListDiagonisticImagingTherapyView(GenericAPIView,ListModelMixin,CreateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.filter(post_type="DI")
    def get_serializer_class(self):
        if self.request.method == "GET" or "POST":
            return GetPostSerializer

        return CreatePostSerializer  

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)  

    def create(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)     

class  ActionDiagonisticImagingTherapyView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    permission_classes = [IsAuthenticated] 
    queryset = Post.objects.filter(post_type="DI") 
    def get_serializer_class(self):
        if self.request.method == "GET" or "POST":
            return GetPostSerializer

        return CreatePostSerializer  
    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)

    def update(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
class ListNuclearMedicineTherapyView(GenericAPIView,ListModelMixin,CreateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.filter(post_type="DI")
    def get_serializer_class(self):
        if self.request.method == "GET" or "POST":
            return GetPostSerializer

        return CreatePostSerializer  

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)  

    def create(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)     

class  ActionNuclearMedicineTherapyView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    permission_classes = [IsAuthenticated] 
    queryset = Post.objects.filter(post_type="DI") 
    def get_serializer_class(self):
        if self.request.method == "GET" or "POST":
            return GetPostSerializer

        return CreatePostSerializer  
    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)

    def update(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)    


    
    