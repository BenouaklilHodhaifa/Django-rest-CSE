from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Project, Task

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'role')
    
    def create(self, validated_data):      
        role = validated_data.pop('role', None)
        if not role:
            raise serializers.ValidationError("role field is required.")
        
        validated_data['username'] = validated_data['email']
        user = User.objects.create_user(role=role, **validated_data)
        return user
        

class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    assigned_to = UserSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)
    project_id = serializers.IntegerField(write_only=True)
    assigned_to_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Task
        fields = '__all__'