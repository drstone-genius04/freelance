from django.shortcuts import render
from django.views import View

# Create your views here.
def aboutUs(request):
    return render(request, 'about.html')
def contactUs(request):
    return render(request, 'contact.html')
def services(request):
    return render(request, 'services.html')

class indexPage(View):
    template_name = 'index.html'
    def get(self, request):
        return render(request, self.template_name)
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["main"] = context['main'].filter(user=self.request.user) 
    #     return context

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super(mainPage, self).form_valid(form)