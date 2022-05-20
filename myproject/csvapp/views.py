from datetime import date
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.http import HttpResponse
import csv
from .models import *
from .models import Customer
import os


# Dynamic Database Data Export to CSV for Django Export CSV
def export_to_csv(request):
    customer = Customer.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="customers' + str(date) + '.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'USERNAME', 'EMAIL', 'PASSWORD', 'PASSWORD1'])
    customer_fields = customer.values_list('id', 'username', 'email', 'password', 'password1')
    for c in customer_fields:
        writer.writerow(c)
    return response


with open('customers.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)


def generate_csv(request):
    product = Product.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=products.csv'
    writer = csv.writer(response)
    writer.writerow(['Customer', 'Name', 'Detail', 'Price', 'File', 'Create_Time'])
    product_fields = product.values_list('customer', 'name', 'detail', 'price', 'file', 'created')
    for p in product_fields:
        writer.writerow(p)
    return response


class CSVPageView(TemplateView):
    template_name = "home.html"


# Simple CSV Write Operation
def csv_simple_write(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv_simple_write.csv"'

    writer = csv.writer(response)
    writer.writerow(['username', 'email', 'password', 'password1'])
    writer.writerow(['rk1', 'r@gmail.com', '111', '111'])
    writer.writerow(['rk2', 'r@gmail.com', '111', '111'])
    writer.writerow(['rk3', 'r@gmail.com', '111', '111'])
    return response


# Writing CSV File From a Dictionary
def csv_dictionary_write(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv_dictionary_write.csv"'

    fieldnames = ['username', 'email', 'password', 'password1']
    writer = csv.DictWriter(response, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow(
        {'username': 'rk1', 'email': 'r@gmail.com', 'password': '111', 'password1': '111'})
    writer.writerow(
        {'username': 'rk2', 'email': 'r@gmail.com', 'password': '111', 'password1': '111'}
    )
    writer.writerow(
        {'username': 'rk1', 'email': 'r@gmail.com', 'password': '111', 'password1': '111'}
    )
    return response


def csv_database_write(request):
    # Get all data from UserDetail Databse Table
    users = Customer.objects.all()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv_database_write.csv"'

    writer = csv.writer(response)
    writer.writerow(['username', 'email', 'password', 'passsword1'])

    for user in users:
        writer.writerow([user.username, user.email, user.password, user.password1])
    return response


def csv_simple_read(request):
    path = os.path.dirname(__file__)
    file = os.path.join(path, 'csv_database_write.csv')

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        # See your console/terminal
        for row in csv_reader:
            if line_count == 0:
                print('\n\nColumn names are {}, {}, {}'.format(row[0], row[1], row[3], row[2]))
                line_count += 1
            else:
                print('\t{} {} lives in {}, and his phone number is {}.'.format(row[0], row[1], row[3], row[2]))
                line_count += 1
        print('Processed {} lines.\n\n'.format(line_count))

        return redirect('/m1/')  # Redirect to home
