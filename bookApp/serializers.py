from rest_framework import serializers
from .models import Book

def name_length(value):
        if len(value) < 5:
            raise serializers.ValidationError("Name is too short")
        else:
            return value

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(validators = [name_length])
    author = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=5, decimal_places=2)



    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
    

    # FIELD LEVEL VALIDATION
    # def validate_title(self, value):
    #     if len(value) < 5:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value
        

    #OBJECT LEVEL VALIDATION
    def validate(self, data):
        if data['title'] == data['author']:
            raise serializers.ValidationError('title and author cannot be same')
        else:
            return data