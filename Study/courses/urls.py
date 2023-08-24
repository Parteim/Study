from django.urls import path

from .views import index, courses, topics, topic_instance

urlpatterns = [
    path('', index, name='home'),
    path('course/<int:pk>', courses, name='course'),
    path('topics/<int:pk>', topics, name='topics'),
    path('topic_instance/<int:pk>', topic_instance, name='topic_instance'),
]
