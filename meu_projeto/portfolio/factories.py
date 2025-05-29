import meu_projeto.portfolio.factories as factories
from faker import Factory as FakerFactory

from django.contrib.auth.models import User
from django.utils.timezone import now

from portfolio.models import Post

faker = FakerFactory.create()


class UserFactory(factories.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factories.Faker("safe_email")
    username = factories.LazyAttribute(lambda x: faker.name())

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop("password", None)
        user = super(UserFactory, cls), prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user
    

    class Postfactory(factories.django.DjangoModelFactory):
        title = factories.LazyAttribute(lambda x: faker.sentence())
        created_on = factories.LazyAttribute(lambda x: faker.now())
        author = factoty.SubFactory(UserFactory)
        status = 0

        class Meta:
            model = Post