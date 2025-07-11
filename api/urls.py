from django.urls import path
# for importing books 
from .views import BooksApiView,BookDetailView,BookCreateApiView,BookDestroyApiView,BookUpdateApiView
# for importing categories
# from .views import CategoryApiView,CategoryDetailApiView,CategoryCreateApiView,CategoryDestroyApiView,CategoryUpdateApiView
# for importing authors
# from .views import AuthorsApiView,AuthorsDetailApiView,AuthorsCreateApiView,AuthorsDestroyApiView,AuthorsUpdateApiView

# These imports for the swagger/frontend programmers!
# ===============================================================
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# ================================================================


urlpatterns = [
    # These pahts for the swagger/frontend programmers!
    # ===============================================================
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # ===============================================================



    # These are for books urls
    path('',BooksApiView.as_view()),
    path('<int:pk>/',BookDetailView.as_view()),
    path('create/',BookCreateApiView.as_view()),
    path('delete/<int:pk>/',BookDestroyApiView.as_view()),
    path('<int:pk>/update/',BookUpdateApiView.as_view()),



    # # These are for categories urls
    # path('category_list/',CategoryApiView.as_view()),
    # path('category_detail/<int:pk>/',CategoryDetailApiView.as_view()),
    # path('category_create/',CategoryCreateApiView.as_view()),
    # path('category_delete/<int:pk>/',CategoryDestroyApiView.as_view()),
    # path('category_update/<int:pk>/',CategoryUpdateApiView.as_view()),



    # # These are for author urlsd
    # path('authors_list/',AuthorsApiView.as_view()),
    # path('authors_detail/<int:pk>/',AuthorsDetailApiView.as_view()),
    # path('authors_create/',AuthorsCreateApiView.as_view()),
    # path('authors_delete/<int:pk>/',AuthorsDestroyApiView.as_view()),
    # path('authors_update/<int:pk>/',AuthorsUpdateApiView.as_view())
]   