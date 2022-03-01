from rest_framework import serializers
from employee.models import Employeetable
class EmployeetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employeetable
        fields = ['id', 'firstname', 'lastname', 'fullname', 'age', 'city']


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return  Employeetable.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.fullname = validated_data.get('fullname', instance.fullname)
        instance.age = validated_data.get('age ', instance.age )
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
