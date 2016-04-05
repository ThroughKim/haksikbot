from django.template.response import TemplateResponse

def home_page(request):
    context = {}

    return TemplateResponse(request, 'index.html', context)
