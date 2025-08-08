from django.shortcuts import render, get_object_or_404, redirect
from.models import Book, Order
from django.db.models import Sum

# Create your views here.
from django.db.models import Sum
def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

# this logic will display the particular book detail because here
# we are passing a book_id and therefore whenever your book_id will 
# match it will display only that book details

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity',1))
        Order.objects.create(book=book, quantity=quantity)
        return redirect('cart')
    return redirect('book_detail',book_id=book_id)

def cart(request):
    orders = Order.objects.all()
    total = sum(order.total_price() for order in orders)
    return render(request, 'cart.html', {'orders':orders, 'total':total})

def analytics(request):
    total_sales = Order.objects.count()
    total_revenue = sum(order.total_price() for order in Order.objects.all())
    total_books = Order.objects.values('book__title').annotate(total_qty=Sum('quantity')).order_by('-total_qty')[:5]
    return render(request, 'analytics.html', {
        'total_sales':total_sales,
        'total_revenue': total_revenue,
        'total_books':total_books
    })






