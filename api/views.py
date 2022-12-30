from django.http import HttpResponse
from django.shortcuts import render
from api.serializers import AdSerializer, BreakSerializer, CategorySeializer, CommentForNoticeSerializer, DialogSerializer, FavoriteSerializer, LessonSerializer, MarketSerializer, NoticeSerializer, ProductSerializer, TextSerializer, UserSerializer, WordSerializer
from rest_framework.response import Response
from base.models import Left_Ad
from rest_framework.decorators import api_view

from breaktime.models import Content
from lesson.models import Dialog, Text, Word
from markets.models import Category, Market, Product
from notices.models import Comment_for_Notice, Notice
from setting.models import Favorites, Lesson
from users.models import User

# Create your views here.


@api_view(('GET',))
def adsApi(request):
    data = Left_Ad.objects.all().order_by('?')
    serializer = AdSerializer(data, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def breakApi(request):
    data = Content.objects.all()
    serializer = BreakSerializer(data, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def wordApi(request):
    data = Word.objects.all()
    serializer = WordSerializer(data, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def dialogApi(request):
    data = Dialog.objects.all()
    serializer = DialogSerializer(data, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def textApi(request):
    data = Text.objects.all()
    serializer = TextSerializer(data, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def categoryApi(request):
    data = Category.objects.all()
    serializer = CategorySeializer(data, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def marketApi(request):
    data = Market.objects.all()
    serializer = MarketSerializer(data, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def productApi(request):
    data = Product.objects.all()
    serializer = ProductSerializer(data, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def noticeApi(request):
    data = Notice.objects.all()
    serializer = NoticeSerializer(data, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def commentForNoticeApi(request):
    data = Comment_for_Notice.objects.all()
    serializer = CommentForNoticeSerializer(data, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def lessonApi(request):
    data = Lesson.objects.all()
    serializer = LessonSerializer(data, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def favoriteApi(request):
    data = Favorites.objects.all()
    serializer = FavoriteSerializer(data, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def userApi(request):
    data = User.objects.all()
    serializer = UserSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['POST',])
def add_word(request):
    # print(request.POST)
    lesson = Lesson.objects.get(name=request.POST.get('lesson_name'))
    print(request.POST.get('another_lang'))
    data = {'another_lang': request.POST.get('another_lang'), 'turkmen': request.POST.get('turkmen'), 'description': request.POST.get('description'), 'additional1': request.POST.get(
        'additional1'), 'additional2': request.POST.get('additional2'), 'additional3': request.POST.get('additional3'), 'lesson': lesson, 'audio_another': request.FILES.get('audio_another'), 'audio_turkmen': request.FILES.get('audio_turkmen')}
    # print(data)
    # print(request.FILES)
    serializer = Word(**data)
    serializer.save()
    print(serializer)
    # serializer.is_valid(raise_exception=True)
    # serializer.save()
    return HttpResponse('ok')


@api_view(['POST',])
def add_dialog(request):
    # print(request.POST)
    lesson = Lesson.objects.get(name=request.POST.get('lesson_name'))
    print(request.POST.get('another_question_lang'))
    data = {'question_another': request.POST.get('question_another'), 'answer_another': request.POST.get('answer_another'), 'question_turkmen': request.POST.get('question_turkmen'), 'answer_turkmen': request.POST.get('answer_turkmen'), 'description': request.POST.get('description'), 'additional1': request.POST.get('additional1'), 'additional2': request.POST.get(
        'additional2'), 'wrong_text': request.POST.get('wrong_text'), 'lesson': lesson, 'audio_question_another': request.FILES.get('audio_question_another'), 'audio_answer_another': request.FILES.get('audio_answer_another'), 'audio_question_turkmen': request.FILES.get('audio_question_turkmen'), 'audio_answer_turkmen': request.FILES.get('audio_answer_turkmen')}
    # print(data)
    # print(request.FILES)
    serializer = Dialog(**data)
    serializer.save()
    print(serializer)
    # serializer.is_valid(raise_exception=True)
    # serializer.save()
    return HttpResponse('ok')
