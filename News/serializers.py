from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    
    # title = serializers.CharField(read_only=True)
    class Meta:
        model = Category
        fields='__all__'
        # read_only = ['caption']
        # extra_kwargs ={'title':{'read_only':True}}
    # def validate_title(self, value):
    #    pass
    # def create(self, validated_data):
    #     return Category.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.caption = validated_data.get('caption', instance.title)