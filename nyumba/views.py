from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import Agents, About, CommentForm, Comment, Photo, Video, Slide


# Create your views here.

class home(ListView):
	model = Slide
	template_name ="nyumba/index1.html"

class contact(View):
	def get(self, *args, **kwargs):
		form = CommentForm()
		context = {
			'form': form
		}
		return render(self.request, "nyumba/contact.html", context)

	def post(self, *args, **kwargs):
		form = CommentForm(self.request.POST)
		if form.is_valid():
			jina = form.cleaned_data.get('jina')
			phone = form.cleaned_data.get('phone')
			maoni = form.cleaned_data.get('maoni')

			try:
				conta = Comment()
				conta.jina = jina
				conta.phone = phone
				conta.maoni = maoni
				conta.save()

				messages.info(self.request, "Thank you to contact us we shall contact you very soon on your number")
				return redirect("/")

			except ObjectDoesNotExist:
				messages.info(self.request, "")
				return redirect("/")


class video(ListView):
	model = Video
	paginate_by = 20
	template_name ="nyumba/video.html"


class photo(ListView):
	model = Photo
	paginate_by = 20
	template_name ="nyumba/photo.html"


class member(ListView):
	model = Agents
	template_name ="nyumba/agents.html"


class about(ListView):
	model = About
	paginate_by = 20
	template_name ="nyumba/about.html"

