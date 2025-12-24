from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def books(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])    
def book(request, id):
    book = Book.objects.get(pk=id)
    if request.method == "GET":
        try:
            
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except:
            return Response({"error":"Eşleşen bir kayıt bulunamadı."}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        seralizer = BookSerializer(book,data = request.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data)
        else:
            return Response(seralizer.errors)
        
    if request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)