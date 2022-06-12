from rest_framework import serializers

from Blogging.models import Post 

class GetPostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields = '__all__'

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =['heading','description','image','video','comments']