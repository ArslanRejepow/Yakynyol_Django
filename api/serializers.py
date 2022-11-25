from rest_framework.serializers import ModelSerializer
from base.models import Left_Ad
from breaktime.models import Content
from lesson.models import Dialog, Text, Word
from markets.models import Category, Market, Product
from notices.models import Comment_for_Notice, Notice
from setting.models import Favorites, Lesson
from users.models import User

class AdSerializer(ModelSerializer):
    class Meta:
        model = Left_Ad
        fields = '__all__'

class BreakSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

class WordSerializer(ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'

class DialogSerializer(ModelSerializer):
    class Meta:
        model = Dialog
        fields = '__all__'

class TextSerializer(ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'

class CategorySeializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MarketSerializer(ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class NoticeSerializer(ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'

class CommentForNoticeSerializer(ModelSerializer):
    class Meta:
        model = Comment_for_Notice
        fields = '__all__'

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class FavoriteSerializer(ModelSerializer):
    class Meta:
        model = Favorites
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
