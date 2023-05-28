from django.contrib import admin

from .models import *

class AttractionImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ('id',)
    extra = 1

class HotelImageInline(admin.TabularInline):
    model = HotelImage
    readonly_fields = ('id',)
    extra = 1

class OperatorImageInline(admin.TabularInline):
    model = OperatorImage
    readonly_fields = ('id',)
    extra = 1

class OperatorServiceInline(admin.TabularInline):
    model = OperatorPackage
    readonly_fields = ('id',)
    extra = 1

class AttractionFeeInline(admin.TabularInline):
    model = AttractionFee
    readonly_fields = ('id',)
    extra = 1


class RoomInline(admin.TabularInline):
    model = Room
    readonly_fields = ('id',)
    extra = 1


@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'type','image']
    inlines = [AttractionImageInline, AttractionFeeInline]

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'attraction','image']
    inlines = [HotelImageInline, RoomInline]


@admin.register(TourOperator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ['name', 'attraction', 'phone_number','email']
    inlines = [OperatorImageInline, OperatorServiceInline]

admin.site.register(Type)
admin.site.register(Location)

admin.site.register(InterestingFacts)
