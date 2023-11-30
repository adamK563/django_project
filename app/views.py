# app/views.py
from django.shortcuts import render, redirect
from django.views import View
from .forms import FormDataForm
from .models import FormData

class FormDataView(View):
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
