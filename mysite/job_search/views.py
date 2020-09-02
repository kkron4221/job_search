from django.shortcuts import render


def index(request):
    test = "hogehoge"
    return render(request, 'job_search/index.html', {'test':test})