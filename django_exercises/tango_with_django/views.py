from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from tango_with_django.models import Page, User
from logging import debug

# Create your views here.
def index(request):
	return render(request, "rango/index.html",{"page_title":"Rango Exercises"})


def signup(request):
	pass


def login(request):
	if request.method == "POST":
		if request.POST["email"]:
			u = User.objects.filter(email=request.POST["email"], password=request.POST["password"])
			if u:
				request.session["uid"] = u[0].uid
				request.session["email"] = u[0].email
				return HttpResponseRedirect(reverse("twd:user_profile"))
			else:
				return render(request, "rango/login.html", {"error_message": "Account doesn't exist or wrong password."})
		else:
			return render(request, "rango/login.html", {"error_message": "Please ener."})

	elif request.method == "GET":
		return render(request, "rango/login.html",{"page_title": "Login Page"})
	else:
		return HttpResponseRedirect(reverse("twd:login", {"error_msg":"Invalid request."}))


def profile(request):
	uid = request.session.get("uid")
	pages = Page.objects.filter(uid=uid)
	return render(request, "rango/pages/profile.html",{"page_title": "Profile Page", "pages": pages})
	

def create(request):
	if request.method == "POST":

		return render(request, "rango/pages/create.html", {"page_title", "POST CP"})
	elif request.method == "GET":
		return render(request, "rango/pages/create.html",{"page_title", "Create Page"})
	else:
		return HttpResponseRedirect(reverse("twd:login", {"error_msg":"Invalid request."}))



def track_url(request):
	if request.method == "GET":
			if request.GET["pid"]:
				p = Page.objects.get(pid=request.GET["pid"])
				pid = request.GET["pid"]
				if p :
					p.count += 1
					p.save()
					return HttpResponseRedirect(reverse("twd:page_detail")+"?pid=" + str(pid))
	else:
		return HttpResponse("Invalid request.")

				
def page_detail(request):
	pid = request.GET["pid"]
	p = Page.objects.get(pid=pid)
	return render(request, "rango/pages/page_detail.html", 
		{"page_title":p.title, "page_count": p.count})

	
