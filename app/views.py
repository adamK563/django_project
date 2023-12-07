from django.shortcuts import render, redirect
from django.views import View
from .forms import FormDataForm, SignUpForm
from .models import FormData
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginView(View):
    template_name = 'registration/login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                return redirect('questioner_view')
            else:
                pass
        return render(request, self.template_name, {'form': form})

@method_decorator(login_required, name='dispatch')
class ProtectedView(View):
    template_name = 'registration/protected_view.html'

    def get(self, request):
        return render(request, self.template_name)

class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class SignUpView(View):
    template_name = 'registration/signup.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, self.template_name, {'form': form})

class HomeView(View):
    template_name = 'apppractice/home.html'
    def get(self, request):
        return render(request, self.template_name)

class ClearDataView(View):
    def get(self, request):
        FormData.objects.all().delete()
        return redirect('form_data_view')

class FormView(View):
    template_name = 'apppractice/form_template.html'

    def get(self, request):
        form = FormDataForm()
        data_list = FormData.objects.all()
        return render(request, self.template_name, {'form': form, 'data_list': data_list})

    def post(self, request):
        form = FormDataForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            selected_answer = request.POST.get(f'answer{instance.id}')
            instance.selected_answer = selected_answer
            instance.save()
            return redirect('form_data_view')
        data_list = FormData.objects.all()
        return render(request, self.template_name, {'form': form, 'data_list': data_list})


class QuestionerView(View):
    template_name = 'apppractice/questioner_template.html'

    def get(self, request):
        form = FormDataForm()  
        data_list = FormData.objects.all()
        return render(request, self.template_name, {'form': form, 'data_list': data_list})

    def post(self, request):
        form = FormDataForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.answer = request.POST.get('answer')
            instance.save()
            return redirect('answers_view')  
        data_list = FormData.objects.all()
        return render(request, self.template_name, {'form': form, 'data_list': data_list})

class AnswersView(View):
    template_name = 'apppractice/answers_template.html'

    def get(self, request):
        data_list = FormData.objects.all()
        return render(request, self.template_name, {'data_list': data_list})
