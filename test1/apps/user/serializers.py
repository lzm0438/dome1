from rest_framework import serializers

from apps.user.models import Student, Teacher, Book


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    # def test(self):
    #
    #
    #
    # def test2(self):


class TeacherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
