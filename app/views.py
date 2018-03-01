from django.shortcuts import render_to_response
from django.middleware.csrf import get_token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
# Create your views here.

class GroupList(APIView):
    _template='index.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        groups=Group.objects.all()
        serializer=GroupSerialize(groups, many=True)
        return Response({'groups':groups}, template_name='index.html')

    def post(self, request):
        data=request.POST
        group=Group.objects.create(name=data['name'],
                                   description=data['description'],
                                   icon=request.FILES['icon'],
                                   group_id=2)
        groups = Group.objects.all()
        serializer = GroupSerialize(groups, many=True)
        return Response({'groups':groups}, template_name='index.html')

@api_view(['GET'])
def form(request):
    cs=get_token(request)
    return render_to_response('form.html', locals())

@api_view(['GET'])
def form_(request, group):
    cs=get_token(request)
    group=group
    return render_to_response('element_form.html', locals())

class ElementList(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    def get(self,request, group_id):
        group=Group.objects.filter(id=group_id)
        elements=list(Element.objects.filter(moderator=True, group_id=group_id))

        return Response(locals(), template_name='page.html')

    def post(self,request, group_id):
        data = request.POST
        element = Element.objects.create(name=data['name'],
                                     description=data['description'],
                                     icon=request.FILES['icon'],
                                     group_id=group_id)

        group = Group.objects.filter(id=group_id)
        elements = list(Element.objects.filter(moderator=True, group_id=group_id))
        return Response({'group': group,'elements':elements}, template_name='page.html')

