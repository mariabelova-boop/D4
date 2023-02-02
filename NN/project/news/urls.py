from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostFilter, PostDetail,PostCreate,PostUpdate,PostDelete


urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>', PostDetail.as_view()),
   path('search/', PostFilter.as_view(), name = 'post_search'),
   path('create/', PostCreate.as_view(), name = 'post_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name = 'post_update'),
   path('<int:pk>/delete/',PostDelete.as_view(), name = 'post_delete'),
]