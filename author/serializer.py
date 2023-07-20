from rest_framework import serializers


from .models import AuthorModel

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = '__all__'

