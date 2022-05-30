from django.forms import BooleanField, ModelForm

from .models import Comment


class MessageForm(ModelForm):

    privacy = BooleanField(required=True)

    class Meta:
        model = Comment
        fields = [
            "name",
            "email",
            "phone",
            "text",
            "course",
        ]


class CourseBuyForm(ModelForm):

    privacy = BooleanField(required=True)

    class Meta:
        model = Comment
        fields = [
            "name",
            "email",
            "phone",
            "text",
            "category",
            "course",
        ]
