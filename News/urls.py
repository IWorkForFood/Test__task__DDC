# ruff: noqa: E501
from django.urls import path
from News.views import (
                        createNews,
                        updateNews,
                        authorsListNews,
                        deleteNews
                        )

urlpatterns = [
    path('authors_news/', authorsListNews, name="authors_news"),

    #path('home', , name='home')
    path('create_news/', createNews, name="create_news"),
    path('update_news/<int:pk>/', updateNews, name="update_news"),
    path('delete_news/<int:pk>/', deleteNews, name="delete_news"),
]

'''
    path('add-blog/', add_blog, name="add_blog"),
    path('blog-delete/<id>', blog_delete, name="blog_delete"),
    path('blog-update/<slug>/', blog_update, name="blog_update"),
'''