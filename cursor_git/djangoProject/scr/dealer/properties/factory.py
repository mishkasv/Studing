from . import models
import factory.fuzzy
from faker_vehicle.vehicle_dict import vehicles

vehicle_category = [v['Category'] for v in vehicles]


class PropertyFacrory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Property

    category = factory.Sequence(lambda n: "Category #%s" % n)
    name = factory.fuzzy.FuzzyChoice(vehicle_category)

    @factory.post_generation
    def carproperty(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for car in extracted:
                self.carproperty.add(car)
