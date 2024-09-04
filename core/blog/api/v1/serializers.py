from rest_framework import serializers
from blog.models import Post, Category
from django.urls import reverse
from accounts.models import Profile


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
    absolute_url = serializers.SerializerMethodField()
    #category = serializers.SlugRelatedField(many=False, slug_field='name', read_only=False, queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ['id','author', 'title', 'content', 'category', 'image',
                       'snippet', 'status', 'relative_url',
                       'absolute_url', 'created_date', 'published_date']
        read_only_fields = ['author']

    
    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('blog:api-v1:post-detail',
                                                   kwargs={'pk':obj.pk}))
    
    
    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context['kwargs'].get('pk'):
            # detail page
            rep.pop('snippet')
            rep.pop('relative_url')
            rep.pop('absolute_url')

        else:
            rep.pop('content')

        rep['category'] = CategorySerializer(instance.category, context={'request':request}).data
        return rep
    

    def create(self, validated_data):
        user_id = self.context.get('request').user.id
        validated_data['author'] = Profile.objects.get(user__id = user_id)
        return super().create(validated_data)
