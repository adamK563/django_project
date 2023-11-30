# app/views.py
from django.shortcuts import render, redirect
from django.views import View
from .forms import FormDataForm
from .models import FormData

class ClearDataView(View):
    def get(self, request):
        # Clear all data
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
        form = FormDataForm()  # Create a form instance
        data_list = FormData.objects.all()
        return render(request, self.template_name, {'form': form, 'data_list': data_list})

    def post(self, request):
        form = FormDataForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            selected_answer = request.POST.get(f'answer{instance.id}')
            instance.selected_answer = selected_answer
            instance.save()
            return redirect('answers_view')  # Redirect to the answers page
        data_list = FormData.objects.all()
        return render(request, self.template_name, {'form': form, 'data_list': data_list})


class AnswersView(View):
    template_name = 'apppractice/answers_template.html'

    def get(self, request):
        data_list = FormData.objects.all()
        return render(request, self.template_name, {'data_list': data_list})
