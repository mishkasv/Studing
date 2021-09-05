from django import template

register = template.Library()


@register.filter(name='carid')
def take_picture_url_by_car_id(objects, car_id):
    object_ = objects.filter(car_id=int(car_id)).first()
    if object_:
        return object_.url
