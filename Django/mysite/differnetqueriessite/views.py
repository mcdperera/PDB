from django.http import HttpResponse
from differnetqueriessite import models

from django.template import loader

# Display the records in table using a stroed procedure
def callUserCountProc(request):
    rows_list = models.call_UserCount()
    template = loader.get_template('getData.html')
    titles = ["User Type", "Count"]
    context = {'type': models.tablename, 'rows_list': rows_list, 'message': models.errormsg, 'titles': titles}
    return HttpResponse(template.render(context, request))


# Display the records in table using a stroed procedure
def callEmployeeDetailsProc(request):
    rows_list = models.call_EmployeeDetails()
    template = loader.get_template('getData.html')
    titles = ["First name", "Last name" , "Email"]
    context = {'type': models.tablename, 'rows_list': rows_list, 'message': models.errormsg, 'titles': titles}
    return HttpResponse(template.render(context, request))


# Display the records in table using a View
def getCurrentDayOrders(request):
    rows_list = models.get_CurrentDayOrder()
    template = loader.get_template('getData.html')
    titles = ["Product Id", "Product Number"]
    context = {'type': models.tablename, 'rows_list': rows_list, 'message': models.errormsg, 'titles': titles}
    return HttpResponse(template.render(context, request))

# Display the records in table using a  Function
def getNumberOfProducts(request):
    rows_list = models.get_NumberofProducts()
    template = loader.get_template('getData.html')
    titles = ["Number of products" ]
    context = {'type': models.tablename, 'rows_list': rows_list, 'message': models.errormsg, 'titles': titles}
    return HttpResponse(template.render(context, request))


# Display the records in table using a stroed procedure of suppliers
def callSupplierDetailsProc(request):
    rows_list = models.call_SupplierDetails()
    template = loader.get_template('getData.html')
    titles = ["First name", "Last name" , "Email" , "Address" ,  "Ratings" , "NumberofProducts" , "CommisionRate" ]
    context = {'type': models.tablename, 'rows_list': rows_list, 'message': models.errormsg, 'titles': titles}
    return HttpResponse(template.render(context, request))

# Display the records in table using a stroed procedure of suppliers
def callProductDetailsProc(request):
    rows_list = models.call_ProductDetails()
    template = loader.get_template('getData.html')
    titles = ["Products", "Product Type"]
    context = {'type': models.tablename, 'rows_list': rows_list, 'message': models.errormsg, 'titles': titles}
    return HttpResponse(template.render(context, request))

def callBuyingPatternProc(request):
    rows_list = models.call_BuyingPattern()
    template = loader.get_template('getData.html')
    titles = ["LastName","FirstName","OrderDate","NumberofProducts","TotalPrice"]
    context = {'type': models.tablename, 'rows_list': rows_list, 'message': models.errormsg, 'titles': titles}
    return HttpResponse(template.render(context, request))
