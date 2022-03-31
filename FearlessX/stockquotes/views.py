from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages



def home(request):
    import requests
    import json
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Has Been Added! "))
            return redirect('home')
    else: 
        ticker = Stock.objects.all()
        output = []
        for ticker_item in ticker:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_f403a9ed9f1e4d37a462018ae2bb8f91")
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as err:
                api = "Error"
        return render(request, 'home.html', {'ticker' : ticker, 'output' : output})


def search(request):
    import requests
    import json
    import webbrowser

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_f403a9ed9f1e4d37a462018ae2bb8f91")

        try:
            api = json.loads(api_request.content)
        except Exception as err:
            api = "Error"
        return render(request, 'search.html', {'api' : api})

    else:
        return render(request, 'search.html', {'ticker': " "})


def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id) #Symbol Id Number In Database
    item.delete()
    messages.success(request, ("Stock Has Been Deleted!"))
    return redirect('home')
