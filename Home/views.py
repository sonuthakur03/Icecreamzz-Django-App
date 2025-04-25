from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact, CustomOrder, Order
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User

ice_creams = [
            {
                'id': 1,
                'name': 'Chocolate Heaven',
                'description': 'Rich chocolate ice cream with fudge swirl.',
                'image_url': 'https://images.unsplash.com/photo-1580915411954-282cb1b0d780?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'price': 'Rs. 150'
            },
            {
                'id': 2,
                'name': 'Strawberry Delight',
                'description': 'Fresh strawberry ice cream with real fruit bits.',
                'image_url': 'https://plus.unsplash.com/premium_photo-1661427159078-9d85039e99b8?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'price': 'Rs. 120'
            },
            {
                'id': 3,
                'name': 'Mango Magic',
                'description': 'Tropical mango ice cream with a refreshing taste.',
                'image_url': 'https://images.unsplash.com/photo-1591677445539-840cc64705f3?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'price': 'Rs. 130'
            },
            {
                'id': 4,
                'name': 'Vanilla Dream',
                'description': 'Classic vanilla ice cream with a creamy texture.',
                'image_url': 'https://images.unsplash.com/photo-1560008581-09826d1de69e?q=80&w=1944&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'price': 'Rs. 100'
            },
            {
                'id': 5,
                'name': 'Pistachio Delight',
                'description': 'Creamy pistachio ice cream with a nutty finish.',
                'image_url': 'https://plus.unsplash.com/premium_photo-1663853490433-5ed3ff06f9ea?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'price': 'Rs. 140'
            },
            {
                'id': 6,
                'name': 'Coffee Crunch',
                'description': 'Rich coffee ice cream with a crunchy texture.',
                'image_url': 'https://images.unsplash.com/photo-1598268121084-c8f7126e0cef?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'price': 'Rs. 160'
            }
        ]


# Create your views here.
def index(request):

    return render(request, 'index.html')



def about(request):
    # return HttpResponse("This is about page")
    return render(request, 'about.html')

def services(request):

        context = {
            "ice_creams": ice_creams
        }

        # return HttpResponse("This is services page")
        return render(request, 'services.html',context)



def contact(request):
    # return HttpResponse("This is contact page")

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been saved!")
    return render(request, 'contact.html')




def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Perform authentication logic here
        user = authenticate(request, username=username, password=password)
        
        # If successful, redirect or render a success page
        if user is not None:
            # Log the user in
            auth_login(request, user)
            messages.success(request, "Login successful!")
            return render(request, 'index.html')
        else:
            # Invalid login credentials
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')

    # return HttpResponse("This is login page")
    return render(request, 'login.html')



def logout(request):
    auth_logout(request)
    messages.success(request, "Logged out successfully.")
    return render(request, 'logout.html')



def order_view(request, id):
    # Try to find the ice cream by id
    ice_cream = next((item for item in ice_creams if item["id"] == id), None)

    if not ice_cream:
        return HttpResponse("Ice cream not found", status=404)

    if request.method == "POST":
        quantity = request.POST.get("quantity")
        address = request.POST.get("address")

        # You can add logic here to save or send the order
        order = Order(flavor=ice_cream['name'], quantity=quantity, address=address, date=datetime.today())
        order.save()
        print(f"Order placed: {ice_cream['name']} x {quantity} to {address}")

        return render(request, "order_success.html", {
            "ice_cream": ice_cream,
            "quantity": quantity,
            "address": address,
        })

    return render(request, "order.html", {
        "ice_cream": ice_cream,
        "id": id  
    })

def custom_order(request):
    if request.method == "POST":
        flavor = request.POST.get("flavor")
        toppings = request.POST.getlist("toppings")
        quantity = request.POST.get("quantity")
        address = request.POST.get("address")
        special_instructions = request.POST.get("special_instructions")
        customorder = CustomOrder(flavor=flavor, toppings=toppings, quantity=quantity, address=address,special_instructions=special_instructions, date=datetime.today())
        customorder.save()    
      # You can add logic here to save or send the custom order
        print(f"Custom order placed: {flavor} with {', '.join(toppings)} x {quantity} to {address}")

        return render(request, "order_success.html", {
            "flavor": flavor,
            "toppings": toppings,
            "quantity": quantity,
            "address": address,
        })
    return render(request, 'custom_order.html')

def order_list(request):
    orders = Order.objects.all().order_by('id')
    customOrders = CustomOrder.objects.all().order_by('id')  # Latest first
    return render(request, 'orders_list.html', {'orders': orders, 'customOrders': customOrders})

def delete_order(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        order.delete()
        messages.success(request, "Order deleted successfully.")
    except Order.DoesNotExist:
        try:
            custom_order = CustomOrder.objects.get(id=order_id)
            custom_order.delete()
            messages.success(request, "Custom order deleted successfully.")
        except CustomOrder.DoesNotExist:
            return HttpResponse("Order not found", status=404)

    return redirect('order_list')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)

            user.save()

            messages.success(request, 'User created successfully.')
            return redirect('login')  
    return render(request, 'signup.html')