from rest_framework import serializers
from django.contrib.auth.models import User
from apps.books.models import Pregunta, Respuesta, Libro, Capitulo, Pagina


class UserSerializer(serializers.ModelSerializer):
    # posts = serializers.HyperlinkedIdentityField(
    #     'posts', view_name='userpost-list', lookup_field='username'
    # )

    class Meta:
        model = User
        # fields = ('id', 'username', 'first_name', 'last_name', 'posts', )
        fields = ('id', 'username', 'first_name', 'last_name', )


class PreguntaSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(
            PreguntaSerializer, self).get_validation_exclusions(*args, **kwargs)
        return exclusions + ['author']

    class Meta:
        model = Pregunta


class RespuestaSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(
            RespuestaSerializer, self
        ).get_validation_exclusions(*args, **kwargs)
        return exclusions + ['author']

    class Meta:
        model = Respuesta


class LibroSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(
            LibroSerializer, self
        ).get_validation_exclusions(*args, **kwargs)
        return exclusions + ['author']

    class Meta:
        model = Libro


class CapituloSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(
            CapituloSerializer, self
        ).get_validation_exclusions(*args, **kwargs)
        return exclusions + ['author']

    class Meta:
        model = Capitulo


class PaginaSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(
            PaginaSerializer, self
        ).get_validation_exclusions(*args, **kwargs)
        return exclusions + ['author']

    class Meta:
        model = Pagina
