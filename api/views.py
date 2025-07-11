from django.shortcuts import render,get_object_or_404
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView

# Create your views here.
from book.models import Category,Book,Authors
from .serializers import BookSerzializersClass,AuthorSerzializersClass,CategorySerzializersClass


from rest_framework.views import APIView,Response







# class BooksApiView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerzializersClass

class BooksApiView(APIView):
    def get(self,request):
        books = Book.objects.all()
        serialazer_data = BookSerzializersClass(books,many = True).data
        data = {
            'status':'Ok',
            'books':serialazer_data
        }
        return Response(data)


# class BookDetailView(RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerzializersClass

class BookDetailView(APIView):
    def get(self,request,pk):
        book = Book.objects.get(id = pk)
        serializer_data = BookSerzializersClass(book).data
        data = {
            'status':'detail is gotten',
            'book':serializer_data
        }
        return Response(data)

class BookCreateApiView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerzializersClass

class BookDestroyApiView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerzializersClass

# class BookUpdateApiView(UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerzializersClass

class BookUpdateApiView(APIView):
    def put(self,request,pk):
        books = Book.objects.all()
        book = get_object_or_404(books,id = pk)
        data = request.data 
        serialaizer_data = BookSerzializersClass(instance = book,data = data,partial = True).data
        if serialaizer_data.is_valid(raise_exception = True):
            book_saved = serialaizer_data.save()
            data = {
                'status':True,
                'message':f'The book is updated to {book_saved}'
            }
        return Response(data)

# =====================================================



# This is for Authors class!
# class AuthorsApiView(ListAPIView):
#     queryset = Authors.objects.all()
#     serializer_class = AuthorSerzializersClass

# class AuthorsDetailApiView(RetrieveAPIView):
#     queryset = Authors.objects.all()
#     serializer_class = AuthorSerzializersClass

# class AuthorsCreateApiView(CreateAPIView):
#     queryset = Authors.objects.all()
#     serializer_class = AuthorSerzializersClass

# class AuthorsDestroyApiView(DestroyAPIView):
#     queryset = Authors.objects.all()
#     serializer_class = AuthorSerzializersClass

# class AuthorsUpdateApiView(UpdateAPIView):
#     queryset = Authors.objects.all()
#     serializer_class = AuthorSerzializersClass

# # =====================================================


# # This is for Category Class!
# class CategoryApiView(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerzializersClass

# class CategoryDetailApiView(RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerzializersClass

# class CategoryCreateApiView(CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerzializersClass

# class CategoryDestroyApiView(DestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerzializersClass

# class CategoryUpdateApiView(UpdateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerzializersClass