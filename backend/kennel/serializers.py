from .models import Dog, DogColor, DogSize, DogMedia, Litter
from rest_framework import serializers


class DogMediaSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    thumb_url = serializers.SerializerMethodField()
    medium_url = serializers.SerializerMethodField()
    large_url = serializers.SerializerMethodField()
    webp_url = serializers.SerializerMethodField()

    class Meta:
        model = DogMedia
        fields = ['id', 'url', 'thumb_url', 'medium_url', 'large_url', 'webp_url', 'media_type', 'is_cover', 'order']

    def _get_variant_url(self, obj, attr):
        if obj.media_type != DogMedia.MediaType.IMAGE or not obj.file:
            return None
        request = self.context.get('request')
        url = getattr(obj, attr).url
        return request.build_absolute_uri(url) if request else url

    def get_url(self, obj):
        return self._get_variant_url(obj, 'file') if obj.file else None

    def get_thumb_url(self, obj):
        return self._get_variant_url(obj, 'thumb')

    def get_medium_url(self, obj):
        return self._get_variant_url(obj, 'medium')

    def get_large_url(self, obj):
        return self._get_variant_url(obj, 'large')

    def get_webp_url(self, obj):
        return self._get_variant_url(obj, 'webp')


class DogSizeSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source='id')
    label = serializers.CharField(source='name')

    class Meta:
        model = DogSize
        fields = ('value', 'label')


class DogColorSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source='id')
    label = serializers.CharField(source='name')

    class Meta:
        model = DogColor
        fields = ('value', 'label')


class DogShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['name', 'slug']


class LitterShortSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    mother = DogShortSerializer(read_only=True)
    father = DogShortSerializer(read_only=True)

    def get_name(self, obj):
        return f'{obj.mother.name} x {obj.father.name}'

    class Meta:
        model = Litter
        fields = ['name', 'slug', 'mother', 'father']


class DogListSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()
    cover = serializers.SerializerMethodField()

    def get_gender(self, obj):
        return {'value': obj.gender, 'label': obj.get_gender_display()}

    def get_cover(self, obj):
        cover_media = obj.cover_media[0] if obj.cover_media else None
        if cover_media:
            return DogMediaSerializer(cover_media, context=self.context).data
        return None

    class Meta:
        model = Dog
        fields = ['slug', 'name', 'gender', 'birth_date', 'cover']


class LitterListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    mother = DogShortSerializer(read_only=True)
    father = DogShortSerializer(read_only=True)
    puppies_count = serializers.SerializerMethodField()
    photo_url = serializers.SerializerMethodField()
    medium_url = serializers.SerializerMethodField()

    def _get_variant_url(self, obj, attr):
        request = self.context.get('request')
        url = getattr(obj, attr).url
        return request.build_absolute_uri(url) if request else url

    def get_photo_url(self, obj):
        return self._get_variant_url(obj, 'photo') if obj.photo else None

    def get_medium_url(self, obj):
        return self._get_variant_url(obj, 'medium')

    def get_name(self, obj):
        return f'{obj.mother.name} x {obj.father.name}'

    def get_puppies_count(self, obj):
        return getattr(obj, 'puppies_count_db', obj.puppies.count())

    class Meta:
        model = Litter
        fields = ['id', 'slug', 'name', 'birth_date', 'mother', 'father', 'puppies_count', 'photo_url', 'medium_url']


class LitterDetailSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    mother = DogShortSerializer(read_only=True)
    father = DogShortSerializer(read_only=True)
    puppies = serializers.SerializerMethodField()
    puppies_count = serializers.SerializerMethodField()
    males_count = serializers.SerializerMethodField()
    females_count = serializers.SerializerMethodField()
    photo_url = serializers.SerializerMethodField()
    medium_url = serializers.SerializerMethodField()


    def _get_variant_url(self, obj, attr):
        request = self.context.get('request')
        url = getattr(obj, attr).url
        return request.build_absolute_uri(url) if request else url

    def get_photo_url(self, obj):
        return self._get_variant_url(obj, 'photo') if obj.photo else None

    def get_medium_url(self, obj):
        return self._get_variant_url(obj, 'medium')

    def get_name(self, obj):
        return f'{obj.mother.name} x {obj.father.name}'

    def get_puppies(self, obj):
        return DogListSerializer(obj.puppies.all(), many=True, context=self.context).data

    def get_puppies_count(self, obj):
        return obj.puppies_count_db

    def get_males_count(self, obj):
        return obj.males_count_db

    def get_females_count(self, obj):
        return obj.females_count_db

    class Meta:
        model = Litter
        fields = '__all__'


class DogDetailSerializer(serializers.ModelSerializer):
    color = DogColorSerializer(read_only=True)
    size = DogSizeSerializer(read_only=True)
    role = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()
    litter = serializers.SerializerMethodField()
    cover = serializers.SerializerMethodField()
    media = DogMediaSerializer(many=True, read_only=True)

    def get_cover(self, obj):
        cover_media = obj.media.filter(is_cover=True).first()
        if cover_media:
            return DogMediaSerializer(cover_media, context=self.context).data
        return None

    def get_litter(self, obj):
        if obj.litter:
            return LitterShortSerializer(obj.litter).data
        return None

    def get_role(self, obj):
        return {'value': obj.role, 'label': obj.get_role_display()}

    def get_status(self, obj):
        return {'value': obj.status, 'label': obj.get_status_display()}

    def get_gender(self, obj):
        return {'value': obj.gender, 'label': obj.get_gender_display()}

    class Meta:
        model = Dog
        fields = [
            'id', 'slug', 'name', 'description', 'cover', 'birth_date',
            'gender', 'status', 'role', 'size', 'color', 'litter', 'media'
        ]