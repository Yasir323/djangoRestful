from rest_framework import serializers
from .models import Toy


# class ToySerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=150)
#     description = serializers.CharField(max_length=500)
#     release_date = serializers.DateTimeField()
#     toy_category = serializers.CharField(max_length=150)
#     was_included_in_home = serializers.BooleanField(required=False)
#
#     def create(self, validated_data: dict) -> Toy:
#         return Toy.objects.create(**validated_data)
#
#     def update(self, instance: Toy, validated_data: dict) -> Toy:
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.release_date = validated_data.get('release_date', instance.release_date)
#         instance.toy_category = validated_data.get('toy_category', instance.toy_category)
#         instance.was_included_in_home = validated_data.get('was_included_in_home', instance.was_included_in_home)
#         instance.save()
#         return instance


class ToySerializer(serializers.ModelSerializer):

    class Meta:
        model = Toy
        fields = (
            'id',
            'name',
            'description',
            'toy_category',
            'release_date',
            'was_included_in_home'
        )
