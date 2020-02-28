from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from beer.models import Beer, Brewery, Vote
from beer.forms import VoteForm

# Create your views here.
class BeerList(ListView):
    model = Beer

class BeerDetail(DetailView):
    # model = Beer
    queryset = Beer.objects.calculate_vote()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        print(ctx)
        if self.request.user.is_authenticated:
            print(self.object)
            vote = Vote.objects.get_vote_or_unsaved_blank_vote(
                beer=self.object,
                user=self.request.user
            )
            if vote.id:
                vote_form_url = reverse(
                    'beer:UpdateVote',
                    kwargs={
                        'beer_id': vote.beer.id,
                        'pk': vote.id})
            else:
                vote_form_url = (
                    reverse(
                        'beer:CreateVote',
                        kwargs={
                            'beer_id': self.object.id}
                    )
                )
            vote_form = VoteForm(instance=vote)
            ctx['vote_form'] = vote_form
            ctx['vote_form_url'] = vote_form_url
        print(ctx)
        return ctx
        

class BreweryList(ListView):
    model = Brewery

class BreweryDetail(DetailView):
    queryset = Brewery.objects.all_with_prefetch_beers()

class CreateVote(LoginRequiredMixin, CreateView):
    form_class = VoteForm

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user.id
        initial['beer'] = self.kwargs['beer_id']
        return initial
    
    def get_success_url(self):
        beer_id = self.object.beer.id
        return reverse(
            'beer:BeerDetail',
            kwargs={
                'pk': beer_id})

    def render_to_response(self, context, **response_kwargs):
        print(context)
        beer_id = context['object'].id
        beer_detail_url = reverse(
            'beer:BeerDetail',
            kwargs={'pk': beer_id})
        return redirect(
            to=beer_detail_url)

class UpdateVote(LoginRequiredMixin, UpdateView):
    form_class = VoteForm
    queryset = Vote.objects.all()

    def get_object(self, queryset=None):
        vote = super().get_object(queryset)
        user = self.request.user
        if vote.user != user:
            raise PermissionDenied(
                'cannot change another '
                'users vote'
        )
        return vote
    
    def get_success_url(self):
        beer_id = self.object.beer.id
        return reverse(
            'beer:BeerDetail',
            kwargs={'pk': beer_id})

    def render_to_response(self, context, **response_kwargs):
        beer_id = context['object'].id
        beer_detail_url = reverse(
            'beer:BeerDetail',
            kwargs={'pk': beer_id})
        return redirect(
            to=beer_detail_url)
