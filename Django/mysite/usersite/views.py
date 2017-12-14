from django.http import HttpResponse
from usersite import models
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.template import loader
from .forms import NameForm
from .forms import UserReportForm

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
    titles = ["UserId", "Firstname", "Lastname", "Email", "Username", "Password", "Address" , "User typeid"]
    context = {'type': models.tablename, 'rows_list': rows_list, 'message': models.errormsg , 'titles': titles}
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

# After sucessfully insert the data in to the table this method triggered.
def thanks(request):
    template = loader.get_template('thanks.html')
    context = {}
    return HttpResponse(template.render(context, request))

# When user request for insert the data this method trigged
def get_name(request):
    form = NameForm()
    return render(request, 'new.html', {'form': form})

# When user submit the form with data this methos triggered and if there is any thing wrong
# it redirect to error page
def setnew(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            lastname = form.cleaned_data['lastname']
            firstname = form.cleaned_data['firstname']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            address = form.cleaned_data['address']
            usertype = form.cleaned_data['usertype']
            #usertitle = form.cleaned_data['usertitle']

            message = models.insert_tablewithparam(lastname,firstname,email,username,password,address,usertype)
            # redirect to a new URL:
            template = loader.get_template('template.html')
            context = {'table': models.tablename, 'url': models.url, 'message': message}
            return HttpResponse(template.render(context, request))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'error.html', {'form': form})

def newreport(request):
    form = UserReportForm()
    return render(request, 'newreport.html', {'form': form})

# When user submit the form with data this methos triggered and if there is any thing wrong
# it redirect to error page
def setnewReport(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = UserReportForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            usertype = form.cleaned_data['usertype']

            rows_list = models.userTypeReport(usertype)

            # redirect to a new URL:
            template = loader.get_template('getData.html')
            titles = ["UserId", "Firstname", "Lastname", "Email", "Username", "Password", "Address", "User typeid"]
            context = {'type': models.tablename, 'rows_list': rows_list, 'message': models.errormsg, 'titles': titles}
            return HttpResponse(template.render(context, request))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'error.html', {'form': form  })