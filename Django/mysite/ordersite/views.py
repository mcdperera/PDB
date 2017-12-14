from django.http import HttpResponse
from ordersite import models
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.template import loader
from .forms import OrderReportForm

# Creating the table
def createTable(request):
    message = models.create_table()
    template = loader.get_template('template.html')
    context = {'table': models.tablename, 'url': models.url, 'message': message}
    return HttpResponse(template.render(context, request))


# Insert some records to the table.
def insertTable(request):
    message = models.insert_table()
    template = loader.get_template('template.html')
    context = {'table': models.tablename, 'url': models.url, 'message': message}
    return HttpResponse(template.render(context, request))


# Display the records in table.
def selectTable(request):
    rows_list = models.select_table()
    template = loader.get_template('getData.html')
    titles = ["OrderId","OrderNumber","CustomerId","TotalPrice","OrderDate "]
    context = {'type': models.tablename, 'rows_list': rows_list, 'message': models.errormsg, 'titles': titles}
    return HttpResponse(template.render(context, request))


# Delete the records in the table
def deleterecords(request):
    message = models.delete_records_table()
    template = loader.get_template('template.html')
    context = {'table': models.tablename, 'url': models.url, 'message': message}
    return HttpResponse(template.render(context, request))


# Delete the table
def deleteTable(request):
    message = models.drop_table()
    template = loader.get_template('template.html')
    context = {'table': models.tablename, 'url': models.url, 'message': message}
    return HttpResponse(template.render(context, request))

def newreport(request):
    form = OrderReportForm()
    return render(request, 'neworderreport.html', {'form': form})

# When user submit the form with data this methos triggered and if there is any thing wrong
# it redirect to error page
def setnewReport(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = OrderReportForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            ordernumber = form.cleaned_data['ordernumber']

            rows_list = models.selectOrdersByNumber(ordernumber)

            # redirect to a new URL:
            template = loader.get_template('getData.html')
            titles = ["Order Number", "Product Couont"]
            context = {'type': models.tablename, 'rows_list': rows_list, 'message': models.errormsg, 'titles': titles}
            return HttpResponse(template.render(context, request))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = OrderReportForm()

    return render(request, 'error.html', {'form': form  })