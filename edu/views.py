from django.views.generic import View
from django.shortcuts import get_object_or_404, render, redirect

class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
    
class TagStudy(View):
    template_name = 'tag_study.html'

    def get(self, request):
        return render(request, self.template_name)
    
class NewContent(View):
    template_name = 'upload_form.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, reguest):
        param = reguest.POST.get('content','')
        print(f"param:{param}")
        return redirect('edu:tag_study')