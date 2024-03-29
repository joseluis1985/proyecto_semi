from django.shortcuts import render,render_to_response
from django.views.generic import TemplateView,CreateView,FormView
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
from django.forms import ModelForm
from django import forms

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import logout, login,authenticate
from django.contrib.auth.decorators import login_required
import  json
def logoutSystem(request):
	logout(request)
def loginView(request):
	if request.method=="POST":
		form=AuthenticationForm(request.POST)
		if form.is_valid:
			username=request.POST["username"]
			password=request.POST["password"]
			resultado=authenticate(username=username,password=password)
			if resultado:
				if resultado.is_active:
					login(request,resultado)
					return HttpResponseRedirect("/usuarios/logeado/")
				else:
					return render_to_response("usuario/no_activo.html",{},RequestContext(request))
			else:
				return render_to_response("usuario/usuarioincorrecto.html",{},RequestContext(request))
	form=AuthenticationForm()
	return render_to_response("usuario/login.html",{"form":form},RequestContext(request))
def logeado(request):
	return render_to_response("usuario/logeado.html",{},RequestContext(request))
def principal(request):
	return render_to_response("usuario/principal.html",{},RequestContext(request))
def nuevo_usuario(request):
	print "principal"
	if request.method=="POST":
		datos=UserCreationForm(request.POST)
		if(datos.is_valid()):
			datos.save()
			return HttpResponseRedirect("/usuarios/exito/")
	form=UserCreationForm()
	return render_to_response("usuario/nuevo.html",{"form":form},RequestContext(request))
def exito_registro(request):
	return render_to_response("usuario/registro_exito.html",{},RequestContext(request))
class formulario(ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	password1=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=usuario
class PaginaPrincipal(FormView):
	template_name="usuario/index.html"
	form_class=formulario
