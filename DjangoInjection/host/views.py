from django.shortcuts import render

# Create your views here.
from host.forms import HostCheckForm
from os import popen

def index(request):
    output = None
    if request.method == 'POST':
        form = HostCheckForm(request.POST)
        if form.is_valid():
            cmd = 'ping -c 3' + form.cleaned_data['ip']
            output = popen(cmd, 'r').read()
    else:
        form = HostCheckForm()
    return render(request, 'host/index.html', {'form': form, 'output': output})
