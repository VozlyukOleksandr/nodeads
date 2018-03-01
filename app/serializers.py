from rest_framework import serializers
from .models import Group, Element



class GroupSerialize(serializers.ModelSerializer):

    class Meta:
        model=Group
        fields='__all__'


class ElementSerialize(serializers.ModelSerializer):

    class Meta:
        model=Element
        fields=('name','description','icon','group_id','create_time')
