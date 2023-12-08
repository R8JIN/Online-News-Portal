from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import CategorySerializer
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from django.template import loader
from .forms import EditorForm, CommentForm, UpdateForm
from .models import NewsPost, Category, Comment
from django.contrib.auth.decorators import login_required
from .models import Bookmark
from django.contrib import messages
# from Comments.forms import UserComment
# from Comments.forms import CommentForm


def view(request):
    post = NewsPost.objects.all().order_by('category', '-date')
    category = Category.objects.all()
    slide = NewsPost.objects.filter(category__title="Sports").order_by('-date')[0]
    subslide = NewsPost.objects.filter(category__title="Local").order_by('-date')[0:1]
    # slide = NewsPost.objects.filter(category=Category.objects.get(title="Sports")).order_by('-date')[0]
    # categorys = {'category': NewsPost.objects.filter(category=category)
    #              for category in Category.objects.all()}
    content = {
        'post': post, 'category': category, 'slide': slide, 'sub': subslide
    }
    return render(request, 'home.html', content)
    # return render(request, 'home.html', categorys)


def view_article(request, id):
    post = NewsPost.objects.get(id=id)

    category = Category.objects.all()
    post_cat = NewsPost.objects.filter(category__title=post.category)
    form = CommentForm()
    if request.user.is_authenticated:
        author = Comment(user=request.user, post_id=id)
        form = CommentForm()
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=author)
            if form.is_valid():
                form.save()
                return redirect('/')
    return render(request, 'news_detail.html', {'post_cat': post_cat, 'post': post, 'category': category, 'form': form})


def category_view(request, cat):
    post = NewsPost.objects.filter(category_id=cat)
    return render(request, 'category.html', {'post': post})


@login_required
def add_article(request):
    author = NewsPost(author=request.user)
    form = EditorForm()
    if request.method == 'POST':
        form = EditorForm(request.POST, request.FILES, instance=author)

        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'index.html', context)


@login_required
def add_bookmark(request, pid):
    bm_post = Bookmark.objects.filter(user=request.user).filter(post_id=pid)
    if not bm_post:
        bm_post = Bookmark(user=request.user, post=NewsPost.objects.get(id=pid))
        print(bm_post)
        bm_post.save()
        messages.info(request, 'Item bookmarked')
    else:
        messages.info(request, 'Item already bookmarked')
    return redirect('/')


def remove_bookmark(request, pid):
    bm_post = Bookmark(user=request.user, post=NewsPost.objects.get(id=pid))
    bm_post.delete()
    messages.info(request, 'Item removed from bookmark')

@login_required
def view_bookmark(request):
    post = Bookmark.objects.filter(user=request.user)
    return render(request, 'bookmark.html', {'post': post})


def view_profile(request):
    post = NewsPost.objects.filter(author=request.user)
    bm = Bookmark.objects.filter(user=request.user)
    content = {'post': post, 'bm' : bm}
    return render(request, 'user/profile.html', content)


def update(request, id):
    post = NewsPost.objects.get(id=id)

    if request.method == "POST":
        form = UpdateForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
    else:
        form = UpdateForm(instance=post)
    context = {
        'post': post,
        'form': form,

    }
    return render(request, 'user/edit.html', context)


def delete_post(request, id):
    if request.user:
        post = NewsPost.objects.get(id=id)
        print(post)
        post.delete()
    return redirect('/profile')

# def add_comment(request):
#     author = UserComment(user=request.user)
#     form = CommentForm
#     if request.method == 'POST':
#         form = CommentForm(request.POST, instance=author)
#
#         if form.is_valid():
#             form.save()
#
#     context = {'form': form}
#     return render(request, 'comment_div.html', context)
#
# @csrf_exempt
# def catergory_create(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = CategorySerializer(data=python_data)

#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'New Category Added'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type ='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')

# def category_view(request):

#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         cat = Category.objects.get(id=id)

#         serializer = CategorySerializer(cat)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')
    

from django.utils.decorators import method_decorator
from django.views import View

@api_view(['GET', 'POST', 'PUT','PATCH', 'DELETE'])
def CategoryAPI(request):
    if request.method == 'GET':
        id = request.data.get('id')

        if id is not None:
            cat = Category.objects.get(id=id)
            serializer = CategorySerializer(cat)
            return Response(serializer.data)
        cat = Category.objects.all()
        serializer = CategorySerializer(cat, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Added'}
            return Response(res)
        return Response(serializer.errors)
    
    if request.method == 'PUT':
        id = request.data.get('id')
        # print(request.data)
        # print(id)
        cate = Category.objects.get(id=id)
        # print(cat)
        serializer = CategorySerializer(cate, data=request.data, 
                                        partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated'})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        id = request.data.get('id')
        cat = Category.objects.get(id=id)
        cat.delete()
        return Response({'msg': 'Data Deleted'})

@method_decorator(csrf_exempt, name='dispatch')
class category_api(View):

    def get(self, request, *args, **kwargs):    
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        cat = Category.objects.get(id=id)

        serializer = CategorySerializer(cat)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    
    def post(self, request, *args, **kwargs):    
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = CategorySerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'New Category Added'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type ='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        cat = Category.objects.get(id=python_data.get('id'))
        serializer = CategorySerializer(cat, data=python_data, partial=True )
        if serializer.is_valid():
            serializer.save()
            # if serializer.
            # serializer.save()
            res = {'msg': 'Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        res = {'msg': 'Not Updated'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
    
    def delete(self, request, *args, **kwargs):
       
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        title = python_data.get('title')
        print(title)
        cat = Category.objects.get(title=title)
        
        cat.delete()
        res = {'msg': 'Category Deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')


# @api_view(['POST']) #request.data #request.method #request.query_params
# def category_create(request):
#     pass

# @api_view(['GET', 'POST'])
# def hello_world(request):
    # if request.method == 'GET':
    #     return Response({'msg': 'This is get request'})
    # if request.method == "POST":
    #     print(request.data)
        # return Response({'msg': 'This is post request', 'data': request.data})