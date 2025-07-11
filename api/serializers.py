from book.models import Category,Book,Authors
from rest_framework import serializers
from rest_framework.validators import ValidationError
class BookSerzializersClass(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self,data):
        title = data.get('title',None)
        price = data.get('price',None)
        # pages = data.get('pages',None)

        if not title.isalpha():
            data = {
                'status':False,
                'message':'Only Letters should be used!'
            }
            raise ValidationError(data)
        if Book.objects.filter(title = title).exists():
            data = {
                'status':False,
                'message':'This book already exists'
            }
            raise ValidationError(data)
        if price>2000000 or price < 0:
            data = {
                'status':False,
                'message':'The price is mistaken'
            }
            raise ValidationError(data)
        # if pages>5000 or pages<10:
        #     data = {
        #         'status':False,
        #         'message':'This amount of pages can not be given'
        #     }
        #     raise ValidationError(data)

    def validate_pages(self,data):
        if data>5000 or data<10:
            context = {
                'status':False,
                'message':'This amount of pages can not be given'
            }
            raise ValidationError(context)

class CategorySerzializersClass(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class AuthorSerzializersClass(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'