from django.db import models
from django.db.models.aggregates import Sum
import django.contrib.auth
from django.core.exceptions import ObjectDoesNotExist

class BeerManager(models.Manager):
    def calculate_vote(self):
        qs = self.get_queryset()
        qs = qs.annotate(score=Sum('vote__value'))
        return qs

class Beer(models.Model):
    title = models.CharField(max_length=140)

    og = models.FloatField(null=True, blank=True)
    abv = models.FloatField(null=True, blank=True)
    ibu = models.FloatField(null=True, blank=True)

    hops = models.ManyToManyField(to='Hop', related_name='used_hops', blank=True)

    brewery = models.ForeignKey(to='Brewery', on_delete=models.SET_NULL, related_name='brewered', null=True, blank=True)
    style = models.ForeignKey(to='Style', on_delete=models.SET_NULL, null=True, blank=True)

    objects = BeerManager()

    class Meta:
        ordering = ('title', )

    def __str__(self):
        return '{}'.format(self.title)

class Style(models.Model):
    short_title = models.CharField(max_length=40, null=True, blank=True)
    title = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.short_title)

class BreweryManager(models.Manager):
    def all_with_prefetch_beers(self):
        qs = self.get_queryset()
        return qs.prefetch_related(
            'brewered')


class Brewery(models.Model):
    name = models.CharField(max_length=140, verbose_name='Brewery\'s name')

    objects = BreweryManager()

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return '{}'.format(self.name)


class Hop(models.Model):
    name = models.CharField(max_length=50)

    description = models.TextField(blank=True)
    alpha_min = models.FloatField(null=True, blank=True)
    alpha_max = models.FloatField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)


class VoteManager(models.Manager):

    def get_vote_or_unsaved_blank_vote(self, beer, user):
        try:
            return Vote.objects.get(
                beer=beer,
                user=user)
        except ObjectDoesNotExist:
            return Vote(
                beer=beer,
                user=user)


class Vote(models.Model):
    UP = 1
    DOWN = -1
    VALUE_CHOICES = (
        (UP, '👍'),
        (DOWN, '👎'),
    )

    value = models.SmallIntegerField(choices = VALUE_CHOICES)

    user = models.ForeignKey(
        django.contrib.auth.get_user_model(),
        on_delete = models.CASCADE
    )

    beer = models.ForeignKey(
        Beer,
        on_delete = models.CASCADE
    )

    voted_on = models.DateTimeField(
        auto_now = True
    )

    objects = VoteManager()

    class Meta:
        unique_together = ('user', 'beer')

