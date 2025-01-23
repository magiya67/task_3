from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import MyModel
from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


def main(request):
    created_id = request.GET.get('created_id')
    contents = MyModel.objects.all()
    content_list = [str(field1) for field1 in contents]
    response = f"""<form method='POST' action='/contents/'>
                            <input type='text' name='field1'>
                            <button type='submit'>Post</button>
                        </form>
                        <form method='GET' action='/contents/'>
                            <input type='number' name='id'>
                            <button type='submit'>Get</button>
                        </form>"""
    if created_id:
        response += f"<p>New record created with ID: {created_id}</p>"
    return HttpResponse(response)

@csrf_exempt
def contents(request):
    if request.method == 'POST':
        field1 = request.POST.get("field1")
        new_record = MyModel.objects.create(content=field1)
        created_id = new_record.id
        return HttpResponseRedirect(f'/?created_id={created_id}')
    if request.method == 'GET':
        try:
            content_id = request.GET.get("id")
            field1 = MyModel.objects.get(id=content_id)
            return HttpResponse(field1)
        except MyModel.DoesNotExist:
            return HttpResponse("Content not found")