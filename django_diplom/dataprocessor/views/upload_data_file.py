from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class FileDataView(View):
    def get(self, request):
        return render(request, "get_file_data.html", context={'header': '11111', 'message': '2222'})

    def post(self, request):
        return HttpResponse(status=201)
