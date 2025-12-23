from rest_framework import serializers
from book_api.models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    page_number = serializers.IntegerField()
    publish_data = serializers.DateField()
    stock = serializers.IntegerField()