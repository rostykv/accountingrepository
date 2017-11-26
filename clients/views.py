from django.shortcuts import render
def company_list(request):
    return render(request, 'clients/company_list.html', {})
