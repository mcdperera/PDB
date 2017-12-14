from django.http import HttpResponse
from usertitlesite import models

from django.template import loader

# Display the records in table using a stroed procedure
def createTable(request):
    message = models.call_CreateTable()
    template = loader.get_template('template.html')
    context = {'table': models.tablename, 'url': models.url, 'message': message}
    return HttpResponse(template.render(context, request))

# Add column to an existing table.
def addColumnToTable(request):
    message = models.call_AddColumnToExistingTable()
    template = loader.get_template('template.html')
    context = {'table': models.tablename, 'url': models.url, 'message': message}
    return HttpResponse(template.render(context, request))

# drop column in an existing table.
def dropColumnInTable(request):
    message = models.drop_ColumnInExistingTable()
    template = loader.get_template('template.html')
    context = {'table': models.tablename, 'url': models.url, 'message': message}
    return HttpResponse(template.render(context, request))

# drop table.
def deleteTable(request):
    message = models.delete_ExistingTable()
    template = loader.get_template('template.html')
    context = {'table': models.tablename, 'url': models.url, 'message': message}
    return HttpResponse(template.render(context, request))

# Insert values to the newly created table columns.
def insertDataToTable(request):
    message = models.insert_table()
    template = loader.get_template('template.html')
    context = {'table': models.tablename, 'url': models.url, 'message': message}
    return HttpResponse(template.render(context, request))

# Display the records in table.
def selectTable(request):
    rows_list = models.select_table()
    template = loader.get_template('getData.html')
    titles = ["User Title Id","User Title","Description"]
    context = {'type': models.tablename, 'rows_list': rows_list, 'message': models.errormsg, 'titles': titles}
    return HttpResponse(template.render(context, request))