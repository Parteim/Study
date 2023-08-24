from django.shortcuts import render
from .models import Course, CourseLevel, Topic, MaterialText, MaterialLink, MaterialImage


def index(requests):
    courses = Course.objects.get()
    return render(requests, 'courses/index.html', {'courses': courses})


def courses(requests, pk):
    courses = CourseLevel.objects.filter(course=pk)
    return render(requests, 'courses/course.html', {'courses': courses})


def topics(requests, pk):
    topics = Topic.objects.filter(course_level=pk)
    return render(requests, 'courses/topics.html', {'topics': topics})


def topic_instance(requests, pk):
    topic = Topic.objects.get(id=pk)
    return render(requests, 'courses/topic_instance.html', {'topic': topic})
