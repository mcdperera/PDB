from django.http import HttpResponse
from orderdetailsite import models

from django.template import loader

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
    titles = [" OrderDetailId","OrderId","ProductSupplierId ","Quantity ","UnitPrice"]
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