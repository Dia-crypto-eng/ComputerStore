from rest_framework import serializers
from .models import Product,Category
from ComputerStore.SumplifySerializer import DynamicFieldsModelSerializer

class CategorySerializer(DynamicFieldsModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
        
        
class ProductSerializer(DynamicFieldsModelSerializer):
    
    class Meta:
        model = Product
        fields = "__all__"
        

class ProductPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'mark', 'category', 'specifications']
        read_only_fields = ('created', 'updated')
    
    def normalize_value(self, value):
        """تحويل النصوص إلى صيغة الحرف الأول كبير والباقي صغير"""
        return value.capitalize() if isinstance(value, str) else value
    
    def normalize_properties(self, properties):
        """تطبيع خصائص الفئة لجعل الحرف الأول كبيرًا والباقي صغيرًا"""
        return [self.normalize_value(prop) for prop in properties]
    
    def set_specifications(self, instance, values):
        if not isinstance(values, dict): raise ValueError("Values must be a dictionary")
        # الحصول على المفاتيح من proprities الخاصة بالفئة
        category_keys = set(self.normalize_properties(instance.category.proprities))
        # التأكد من أن كل مفتاح في proprities له قيمة مقابلة في القاموس
        instance.specifications = {key: values.get(key, "") for key in category_keys}
        instance.save()

    def create(self, validated_data):
        specifications = validated_data.pop('specifications', {})
        # البحث عن category ID
        category_id = validated_data.get('category')
        # إذا لم تكن الفئة موجودة، نقوم بإنشاء فئة جديدة
        if not category_id:
            category_name = self.normalize_value(validated_data.pop('name', ''))
            category_proprities = self.normalize_properties(specifications.keys())
            category, created = Category.objects.get_or_create(name=category_name,defaults={'proprities': category_proprities})
        else:
            # البحث عن الفئة الموجودة
            category = Category.objects.get(id=category_id)
        # إنشاء الكائن الجديد باستخدام الفئة المناسبة
        instance = Product.objects.create(category=category, **validated_data)
        # تطبيق set_specifications لتحديث field specifications
        self.set_specifications(instance, specifications)
        return instance

    def update(self, instance, validated_data):
        specifications = validated_data.pop('specifications', {})
        # الحصول على category ID من البيانات المعدلة
        category_id = validated_data.get('category')
        if not category_id:
            category_name = self.normalize_value(validated_data.pop('name', ''))
            category_proprities = self.normalize_properties(specifications.keys())
            category, updated = Category.objects.get_or_create(name=category_name,defaults={'proprities': category_proprities})
        else:
            # البحث عن الفئة الموجودة
            category = Category.objects.get(id=category_id)
        # تحديث الكائن الموجود بالفئة الجديدة
        instance.category = category
        instance = super(ProductPostSerializer, self).update(instance, validated_data)
        # تطبيق set_specifications لتحديث field specifications
        self.set_specifications(instance, specifications)
        return instance

    def to_representation(self, instance):
        representation = super(ProductPostSerializer, self).to_representation(instance)
        # تطبيع اسم الفئة
        if 'category' in representation:
            representation['category'] = {
                'name': self.normalize_value(instance.category.name),
                'proprities': self.normalize_properties(instance.category.proprities)
            }
        return representation






               
# class ProductPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Product
#         fields=['name','mark', 'category','specifications']
#         read_only_fields = ('created','updated')
        
#     def to_representation(self, instance):
#         self.fields['category'] =  CategorySerializer()
#         return super(ProductPostSerializer, self).to_representation(instance)
    
#     def set_specifications(self, instance, values):
#         if not isinstance(values, dict):
#             raise ValueError("Values must be a dictionary")

#         # الحصول على المفاتيح من proprities الخاصة بالفئة
#         category_keys = instance.category.proprities

#         # التأكد من أن كل مفتاح في proprities له قيمة مقابلة في القاموس
#         instance.specifications = {key: values.get(key, "") for key in category_keys}
#         instance.save()

#     def create(self, validated_data):
#         # فصل specifications من البيانات المعدلة
#         specifications = validated_data.pop('specifications', {})
#         # إنشاء الكائن الجديد
#         instance = super(ProductPostSerializer, self).create(validated_data)
#         # تطبيق set_specifications لتحديث field specifications
#         self.set_specifications(instance, specifications)
#         return instance

#     def update(self, instance, validated_data):
#         # فصل specifications من البيانات المعدلة
#         specifications = validated_data.pop('specifications', {})
#         # تحديث الكائن الموجود
#         instance = super(ProductPostSerializer, self).update(instance, validated_data)
#         # تطبيق set_specifications لتحديث field specifications
#         self.set_specifications(instance, specifications)
#         return instance
    


                
        
    

     