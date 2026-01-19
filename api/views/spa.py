from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

@login_required
def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, "api/spa/index.html", {})
