
from django.urls import path,include
from .views import Login,Register,BookLists,AddBook,BookDelete,BookUpdate
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/',Login.as_view(), name = 'login'),
    path('register/',Register.as_view(), name = 'register'),
    path('books/',BookLists.as_view(),name = 'books'),
    path('add_book/',AddBook.as_view(),name = 'add_book'),
    path('delete/<int:pk>/',BookDelete.as_view(), name = 'delete'),
    path('logout/',LogoutView.as_view(next_page = 'login'), name = 'logout'),
    path('update<int:pk>/',BookUpdate.as_view(), name = 'update'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
