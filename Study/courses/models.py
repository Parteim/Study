from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return f'Course: {self.course_name}'


class CourseLevel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'Course: {self.title}'


class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    course_level = models.ForeignKey(CourseLevel, on_delete=models.CASCADE)

    def __str__(self):
        return f'Topic: {self.title} for course about {self.course_level.title}'


class Material(models.Model):
    title = models.CharField(max_length=100)

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return f'Material: {self.title} for topic  {self.topic.title} <{self.topic}>'


class MaterialText(models.Model):
    text = models.TextField()

    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return f'Text material {self.material.title} for topic: {self.material.topic.title}'


class MaterialLink(models.Model):
    link = models.CharField(max_length=255)

    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return f'Link material {self.material.title} for topic: {self.material.topic.title}'


class MaterialImage(models.Model):
    img = models.ImageField(upload_to='material_images')

    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    def get_upload_path(self, filename):
        return f'material_images/{self.material.title}/{self.material.topic.title}/{filename}'

    img.upload_to = get_upload_path

    def __str__(self):
        return f'Image for material: {self.material.title} for topic: {self.material.topic.title} ID:<{self.pk}>'
