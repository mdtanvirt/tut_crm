from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import RegistrationForm, AddClientForm, NewOrderForm, NewServiceForm, NewProductForm
from .models import Client, Order, Service

def home(request):

    # Grab all client recods
    clients = Client.objects.all()

    # check the logged in user
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            # then we have to redirect to a page
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('home')

    else:
        return render(request, 'home.html', {'clients': clients})

# this function we will use if we want to use any seperate login page
#def login_view(request):
#    pass

def logout_view(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You are successfully registered and welcome to our site')
            return redirect('home')
    else:
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form':form})

def client(request, pk):
    if request.user.is_authenticated:
        # Look up the specific client data
        client_record = Client.objects.get(id=pk)
        return render(request, 'client.html', {'client_record': client_record})
    else:
        messages.success(request, 'You have to login...')
        return redirect('home')
    
def client_delete(request, pk):
    if request.user.is_authenticated:
        delete_record = Client.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, "You have successfully deleted...")
        return redirect('home')
    else:
        messages.success(request, "You have to login first...")
        return redirect('home')
    
def add_client(request): 
    form = AddClientForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid:
                add_client = form.save()
                messages.success(request, "New Client added ...")
                return redirect('home')
        return render(request, 'add_client.html', {'form':form})

    else:
        messages.success(request, "You have to Login to add new record...")
        return redirect('home')
    
def client_update(request, pk):
    if request.user.is_authenticated:
        current_record = Client.objects.get(id=pk)
        form = AddClientForm(request.POST or None, instance=current_record)
        if request.method == "POST":
            if form.is_valid:
                update_client = form.save()
                messages.success(request, 'Client info updated...')
                return redirect('home')
        return render(request, 'client_update.html', {'form':form})
    else:
        messages.success(request, "You have to login...")
        return redirect('home')
    

# For order View
def orders(request, client_pk):
    if request.user.is_authenticated:
        # Look up the specific client data
        client = Client.objects.get(pk=client_pk)
        order_list = client.orders.all()
        return render(request, 'order.html', {'client': client, 'order_list':order_list})
    else:
        messages.success(request, 'You have to login...')
        return redirect('home')
    

# For new order creation
def new_order(request, client_pk):
    if request.user.is_authenticated:
        client = get_object_or_404(Client, id=client_pk)
        order_list = client.orders.all()
        if request.method == 'POST':
            form = NewOrderForm(request.POST, client=client)
            if form.is_valid():
                order = form.save(commit=False)
                order.client = client
                order.save()
                messages.success(request, "New order created...")
                #return redirect('home')
                return render(request, 'order.html', {'client': client, 'order_list':order_list})
            else:
                messages.success(request, "Order not created...")
                form = NewOrderForm(client=client)
        else:
            form = NewOrderForm(client=client)
        return render(request, 'new_order.html', {'form':form})
    else:
        messages.success(request, "You are not allow to create new order")
        return redirect('home')
    
# For rent info retival
def rent(request, client_pk):
    if request.user.is_authenticated:
        client = get_object_or_404(Client, pk=client_pk)
        rents = client.rent_set.all()
        return render(request, 'rent.html', {'client':client, 'rents':rents})
    else:
        messages.success(request, "You have to login to view rent info")
        return redirect('home')
    
# For rent addition
def new_rent(request, client_pk):
    if request.user.is_authenticated:
        client = get_object_or_404(Client, pk=client_pk)
        rents = client.rent_set.all()
        return render(request, 'new_rent.html', {'client':client, 'rents':rents})
    else:
        messages.success(request, "You have to login to view rent info")
        return redirect('home')
    

# For service list view
def service(request, client_pk):
    if request.user.is_authenticated:
        client = get_object_or_404(Client, pk=client_pk)
        #service = client.service_set.all()
        services = client.service.all()
        return render(request, 'service.html', {'client': client, 'services':services})
    else:
        messages.success(request, "You have to login first...")
        return redirect('home')
    
# For service add
def new_service(request, client_pk):
    if request.user.is_authenticated:
        client = get_object_or_404(Client, id=client_pk)
        services = client.service.all()
        if request.method == 'POST':
            form = NewServiceForm(request.POST, client=client)
            if form.is_valid():
                service = form.save(commit=False)
                service.client = client
                service.save()
                messages.success(request, "New service created...")
                #return redirect('home')
                return render(request, 'service.html', {'client': client, 'services':services})
            else:
                messages.success(request, "Service not created...")
                form = NewServiceForm(client=client)
        else:
            form = NewServiceForm(client=client)
        return render(request, 'new_service.html', {'form':form})
    else:
        messages.success(request, "You are not allow to create new service")
        return redirect('home')
    
#for Product
def product(request, client_pk):
    if request.user.is_authenticated:
        client = get_object_or_404(Client, id=client_pk)
        products = client.product.all()
        return render(request, 'product.html', {'client':client, 'products':products})
    else:
        messages.success(request, "You have to login first.")
        return redirect('home')
    
# For product purchase record add

def new_product(request, client_pk):
    if request.user.is_authenticated:
        client = get_object_or_404(Client, id=client_pk) # get the client ID
        products = client.product.all() # client wise product list get
        if request.method == 'POST':
            form = NewProductForm(request.POST, client=client)
            if form.is_valid():
                product = form.save(commit=False) # this is not fonal save to the DB
                product.client = client # set the client ID
                product.save() # Now save to the DB
                messages.success(request, "New addedd successfully...")
                return render(request, 'product.html', {'client': client, 'products':products})
            else:
                messages.success(request, "Product not added")
                form = new_product(client=client)
        else:
            form = NewProductForm(client=client) # here I am passing the client ID and set the client ID
        return render(request, 'new_product.html', {'form':form})
    else:
        messages.success(request, "You are not allow to access this page")
        return redirect('home')
