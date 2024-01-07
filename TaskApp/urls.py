import TaskApp.views as views
from django.urls import path
urlpatterns = [   
    path('toppost/', views.topPost, name = 'topPost'),
    path('searchcomment/', views.searchComment, name = 'searchComment')
]  