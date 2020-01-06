from rest_framework import serializers
from .models import BlogList

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogList
        fields=('id','title','description','date_created','blog_owner')
        read_only_fields=('date_created',)