from .models import Item, Category
from rest_framework import serializers
from datetime import date


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    @staticmethod
    def check_for_special_chars(value):
        special_chars = '!@#$%^&*'
        for char in special_chars:
            if char in value: raise serializers.ValidationError('no special chars allowed')

    def validate_name(self, value):
        if len(value) < 5: raise  serializers.ValidationError('Name must be at least 5 chars')
        self.check_for_special_chars(value)
        return value

    def validate_description(self, value):
        if len(value.split()) < 2:  raise serializers.ValidationError('description must be at least 2 words')
        self.check_for_special_chars(value)
        return value

    def validate_width(self, value):
        if value and value < 0: raise serializers.ValidationError('value must be positive')
        return value
    def validate_height(self, value):
        if value and value < 0: raise serializers.ValidationError('value must be positive')
        return value
    def validate_weight (self, value):
        if value and value < 0: raise serializers.ValidationError('value must be positive')
        return value

    def validate_expiration_date(self, value):
        if value < date.today(): raise serializers.ValidationError('expiration_date should not be from past')
        return value

    def validate(self, data):
        words_that_need_expiration_date = ['food','drink','beverage',
                                            'snack','fruit','vegetable'
                                        ]
        category = data.get('category')
        expiration_date = data.get('expiration_date')
        for word_that_need_expiration_date in words_that_need_expiration_date:
            if word_that_need_expiration_date.lower() in category.name.lower() and not expiration_date:
                raise serializers.ValidationError('expiration_date necessary for food and drinks')
        return data






