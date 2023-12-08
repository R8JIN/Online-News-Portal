from django.urls import path
from News import views


urlpatterns = [
    path('', views.view, name='home'),
    path('add/', views.add_article, name='add'),
    path('post/<id>', views.view_article, name='article'),
    path('category/<cat>', views.category_view, name='category'),
    path('bookmark/<pid>', views.add_bookmark, name='bookmark'),
    path('bookmark_list', views.view_bookmark, name='view_bm'),
    path('profile', views.view_profile, name='profile'),
    path('delete/<int:id>', views.delete_post, name='delete'),
    path('edit/<int:id>',views.update,name='edit'),
    path('cat_view/', views.category_view),
    path('categ/', views.CategoryAPI),
    # path('cat_create/', views.catergory_create),
    path('cat_api/', views.category_api.as_view()),
    # path('hello_world/', views.hello_world )
]

