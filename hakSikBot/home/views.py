from django.template.response import TemplateResponse
import functions

def home_page(request):
    context = {}
    context['menu'] = functions.get_menu()

    return TemplateResponse(request, 'index.html', context)
