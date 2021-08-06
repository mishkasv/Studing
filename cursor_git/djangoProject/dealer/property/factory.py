from . import models
import factory, faker, faker_vehicle


class PropertyFacrory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Property

    category = factory.Sequence(lambda n: "Category #%s" % n)
    name = faker_vehicle.VehicleProvider.vehicle_object()['Category']

    @factory.post_generation
    def carproperty(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for car in extracted:
                self.carproperty.add(car)
