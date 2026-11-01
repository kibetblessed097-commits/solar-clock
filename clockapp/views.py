from django.shortcuts import render


def clock(request):
    return render(request, "clockapp/clock.html")
