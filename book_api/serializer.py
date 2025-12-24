from rest_framework import serializers
from book_api.models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    page_number = serializers.IntegerField()
    publish_data = serializers.DateField()
    stock = serializers.IntegerField()

    def create(seşf, validated_data):
        return Book.objects.create(**validated_data)