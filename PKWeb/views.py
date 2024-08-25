from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect


from django.contrib.auth import authenticate , login , logout,update_session_auth_hash

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView
from django.views import View
# Create your views here.



class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'protected_page.html'
    login_url = '/login/'  # Redirects to this URL if not logged in
    redirect_field_name = 'next'  # Redirects back to the original URL after login



class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home | PKWeb'
        context['message'] = 'Welcome to the Home Page!'
        return context
    
class DashboardPageView(LoginRequiredMixin,TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home | PKWeb'
        context['message'] = 'Welcome to the Home Page!'
        return context

class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)  # This logs the user out
        return redirect('/')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login | PKWeb'
        return context
    def form_invalid(self, form):
        # Add an error message to the messages framework
        messages.error(self.request, "Invalid username or password. Please try again.")
        return super().form_invalid(form)
    
    
    