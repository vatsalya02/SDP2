import datetime
from time import gmtime,strftime
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
def index(request):
    return render(request, 'home.html')
def registers(request):
    register=False
    if request.method == 'POST':
        name=request.POST.get('name')
        uname = request.POST.get('email')
        pwd = request.POST.get('pd')
        cp=request.POST.get('cpd')
        if Users.objects.filter(email=uname).count() > 0:
            return render(request, 'login.html', {'error': 'Email already Exist'})
        else:
            user = Users(username=name,email=uname, password=pwd,cpassword=cp)
            user.save()
            subject='Thanks For Registering'
            message='HEY '+user.username+''+',you are now successfully registered with Dream Dine.You’ve taken the first step toward becoming a part of our website. We’ll send you timely email and text reminders of new orders through email. We are overwhelmed with your registration.'
            to=user.email
            send_mail(
                subject,
                message,
                'alvatsalya02@gmail.com',
                [to],
            )
            register=True
        return redirect('/login')
    else:
        return render(request, 'login.html',{'msg':'enter valid details'})
    return users

def login(request):
    return render(request,'login.html')
def loginuser(request):
    print(0.1)
    # request.session['cartitems'] = []
    if request.method == 'POST':
        print(0.2)
        uname = request.POST.get('name')
        pwd = request.POST.get('lpd')
        check_user = Users.objects.filter(username=uname, password=pwd)
        request.session.modifed = True
        if uname == "DreamDine" and pwd == "admin":
            return render(request,'admin.html')
        if check_user:
            print(0.3)
            #member = User.objects.get(email=request.POST['login_email'], password=request.POST['lpd'])
            #email=User.objects.get(email=request.POST['login_email'])
            #request.session['email'] = email
            request.session['user'] = uname

            #request.session['cartorder'] = "kishan"
            return render(request, 'index.html',{"username":uname})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'home.html', context)
        return user
def fp(request):
    return render(request,'fp.html')
def forget_pwd(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        pwd = request.POST.get('lpd')
        check_user = Users.objects.get(username=uname)
        if check_user:
            check_user.password=pwd
            check_user.save()
        return render(request,'login.html',{'msg':'Password Updated'})
def menu(request):
    uname=request.session['user']
    return render(request,'menu.html',{'name':uname})
def userinfo(request):
    student=Users.objects.all()
    return render(request, 'display.html', {'student':student,'title':'User Info'})
def ni(request,cartobj=None):
    print(cartobj)
    nitems = item.objects.filter(category="North Indian Specials")

    return render(request, 'north.html',{'nitems':nitems})
def si(request):
    sitems = item.objects.filter(category="South Indian Specials")
    return render(request, 'south.html', {'sitems': sitems})
def italian(request):
    iitems = item.objects.filter(category="Italian & Spanish Dishes")
    return render(request, 'italian.html', {'iitems': iitems})

def sb(request):
    sbitems = item.objects.filter(category="Sweets & Bakings")
    return render(request, 'sb.html', {'sbitems': sbitems})
def dd(request):
    dditems = item.objects.filter(category="Deserts & Drinks")
    return render(request, 'dd.html',{'dditems': dditems})
def ss(request):
    ssitems = item.objects.filter(category="Snacks & Starters")
    return render(request, 'ss.html',{'ssitems': ssitems})
def sp(request):
    spitems = item.objects.filter(category="Seasonal Specials")
    return render(request, 'sp.html',{'spitems': spitems})
def ws(request):
    wsitems = item.objects.filter(category="Weekend Specials")
    return render(request, 'ws.html',{'wsitems': wsitems})
def goback(request):
    uname = request.session['user']

    return render(request,'index.html',{'username':uname})


def logout(request):
    del request.session['user']
    return redirect('/login')
def productinfo(request):
    pro = item.objects.all()
    return render(request, 'displayproduct.html', {'pro':pro,'title':'ProductDetails Info'})
def additem(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category=request.POST.get('category')
        image=request.POST.get('image')
        items= item(name=name, price=price,category=category,image=image)
        items.save()
        return render(request,'additem.html',{'msg': 'Added'})
    else:
        return render(request, 'admin.html')
def add(request):
    return render(request,'additem.html')
def delete(request):
    pro = item.objects.all()
    return render(request, 'delete.html', {'pro': pro, 'title': 'ProductDetails Info'})
def deleteitem(request,name):
    pro = item.objects.get(name = name).delete()
    return render(request, 'admin.html', {'msg': 'Deleted'})
def update_form(request,name,price):
    return  render(request,'updateitem.html',{'name':name,'price':price})
def updateitem(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category=request.POST.get('category')
        pro = item.objects.get(name=name)
        pro.name=name
        pro.category=category
        pro.price=price
        pro.save()
        return render(request, 'admin.html', {'msg': 'updated'})
    else:
        return render(request, 'admin.html', {'msg': 'cannotupdate'})
def update(request):
    pro = item.objects.all()
    return render(request, 'update.html', {'pro':pro,'title':'ProductDetails Info'})

def cart_add(request,name):
    uname = request.session['user']
    user = Users.objects.get(username=uname)
    items = get_object_or_404(item,name=name)
    #if store.objects.filter(items__name=name).count() == 0:
    if request.method == 'POST':
        qty = request.POST.get('qty')
        storeItems.quantity = qty
        cart_item = storeItems.objects.create(
                items=items,
                users=user,
                quantity=qty,
            )

    return redirect(request.META['HTTP_REFERER'])
    #return render(request,'menu.html')
    # return render(request,redirect_html,context=cot)
    # return redirect(request.META['HTTP_REFERER'])
def get_cart_items(request):
    uname = request.session['user']
    user = Users.objects.get(username=uname)
    cart_items = storeItems.objects.filter(users=user)
    amount =0;
    for cart_item in cart_items:
        print(cart_item.quantity)
        print(cart_item.items.name)
        amount = amount+cart_item.quantity*cart_item.items.price
    print('amount is',amount)
    # bill = cart_items.aggregate(Sum('add'))
    # #number = cart_items.aggregate(Sum('quantity'))
    # #pieces = cart_items.aggregate(Sum('item__pieces'))
    #print(request.session['cartorder'])
    # a = bill.get("add__sum")
    # count = number.get("quantity__sum")
    # total_pieces = pieces.get("item__pieces__sum")
    context = {
        'cart_items': cart_items,
        'total':amount,
    }
    return render(request, 'cart.html', context)
def remove(request,name):
    cartitems = storeItems.objects.filter(items__name = name)
    cartitems.delete()
    return redirect(request.META['HTTP_REFERER'])
def order(request):
    return render(request,'order.html')
def end(request):
    return render(request,'end.html')
def amount(request,total,cart_items):
    uname = request.session['user']
    user = Users.objects.get(username=uname)
    cart_items = storeItems.objects.filter(users=user).first()
    order=orders_foods.objects.create(
        cart_items=cart_items,
        total=total
    )
    return render(request,'amount.html')
def pay(request):
    return render(request,'payment.html')
def addpayment(request):
    if request.method == 'POST':
        name = request.POST.get('firstname')
        email = request.POST.get('email')
        address=request.POST.get('address')
        city=request.POST.get('city')
        zip = request.POST.get('zip')
        state = request.POST.get('state')
        name_on_card = request.POST.get('cardname')
        cardno = request.POST.get('cardnumber')
        expmonth = request.POST.get('expmonth')
        expyear = request.POST.get('expyear')
        cvv = request.POST.get('cvv')
        payments = bill(name=name, email=email,address=address,city=city,zip=zip,state=state,name_on_card=name_on_card,cardno=cardno,expmonth=expmonth,expyear=expyear,cvv=cvv)
        payments.save()
        return render(request,'end.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
@login_required(login_url='/loginusers')
def table(request):
    date_table=datetime.date.today()
    time_table=datetime.datetime.now().time()
    bcount=1
    a = book_tables.objects.filter(date_table=date_table).count()
    b = bcount - a
    if b==0:
        print("all tables booked")
    return render(request,'table.html',{'tcount':b})
def add_table(request):
    date_table = datetime.date.today()
    time_table = datetime.datetime.now().time()
    bcount = 1
    a = book_tables.objects.filter(date_table=date_table).count()
    b = bcount - a
    if b>0:
        if request.method=='POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            guest = request.POST.get('guest')
            date_table = request.POST.get('date')
            time_table = request.POST.get('time')
            category = request.POST.get('category')
            msg = request.POST.get('message')
            book=book_tables(name=name,email=email,phone=phone,guest=guest,date_table=date_table,time_table=time_table,category=category,msg=msg)
            book.save()
            return render(request,'end.html',{'msg':'Table Booked Sucessfully'})
    else:
        return render(request, 'sorry.html', {'msg': 'Total Table Booked'})
def feedback(request):
    return render(request,'feedback.html')
def cater(request):
    uname = request.session['user']
    return render(request,'catering.html',{'username':uname})
def delights(request):
    return render(request, 'delights.html')
def desserts(request):
    return render(request, 'desserts.html')
def tropics(request):
    return render(request, 'tropics.html')
def maincourse(request):
    return render(request, 'main.html')
def paan(request):
    return render(request, 'paan.html')
def relishes(request):
    return render(request, 'relishes.html')
def dishes(request):
    return render(request, 'dishes.html')
def drinks(request):
    return render(request, 'drinks.html')
def delights_add(request):
    uname = request.session['user']
    user = Users.objects.get(username=uname)
    if request.method=="POST":
        dcategory = request.POST.get('dcategory')
        dcapacity=request.POST.get('dcapacity')
        items=item.objects.get(name=dcategory)
        dprice=items.price*int(dcapacity)
        delight = Catering_order_table(uname=user.username,dcategory=dcategory,dcapacity=dcapacity,dprice=dprice)
        delight.save()
        print(str(delight.cid))
        return render(request,'catering.html',{'msg':'Delights added to menu'})
def desserts_add(request):
    uname = request.session['user']
    user = Users.objects.get(username=uname)
    cater_order= Catering_order_table.objects.get(uname=user.username)
    print(str(cater_order))
    if request.method=="POST":
        dcategory = request.POST.get('decategory')
        decapcity=request.POST.get('decapcity')
        items = item.objects.get(name=dcategory)
        deprice = items.price * int(decapcity)
        cater_order.decategory=dcategory
        cater_order.decapacity=decapcity
        cater_order.deprice=deprice
        cater_order.save()
        return render(request,'catering.html',{'msg':'Desserts added to menu'})
def dishes_add(request):
    uname = request.session['user']
    user = Users.objects.get(username=uname)
    cater_order = Catering_order_table.objects.get(uname=user.username)
    print(str(cater_order))
    if request.method == "POST":
        dicategory = request.POST.get('dicategory')
        dicapcity = request.POST.get('dicapcity')
        items = item.objects.get(name=dicategory)
        deprice = items.price * int(dicapcity)
        cater_order.dicategory = dicategory
        cater_order.dicapacity = dicapcity
        cater_order.diprice=deprice
        cater_order.save()
        return render(request,'catering.html',{'msg':'Dishes added to menu'})
def paan_add(request):
    uname = request.session['user']
    user = Users.objects.get(username=uname)
    # cid=request.session['cid']
    cater_order = Catering_order_table.objects.get(uname=user.username)
    print(str(cater_order))
    if request.method == "POST":
        pcategory = request.POST.get('pcategory')
        pcapcity = request.POST.get('pcapcity')
        items = item.objects.get(name=pcategory)
        pprice = items.price * int(pcapcity)
        cater_order.pcategory = pcategory
        cater_order.pcapacity = pcapcity
        cater_order.pprice=pprice
        cater_order.save()
        return render(request,'catering.html',{'msg':'Paan Specials added to menu'})
def tropics_add(request):
    uname = request.session['user']
    user = Users.objects.get(username=uname)
    # cid=request.session['cid']
    cater_order = Catering_order_table.objects.get(uname=user.username)
    print(str(cater_order))
    if request.method == "POST":
        tcategory = request.POST.get('tcategory')
        tcapcity = request.POST.get('tcapacity')
        items = item.objects.get(name=tcategory)
        tprice = items.price * int(tcapcity)
        cater_order.tcategory = tcategory
        cater_order.tcapacity = tcapcity
        cater_order.tprice=tprice
        cater_order.save()
        return render(request,'catering.html',{'msg':'Tropics added to menu'})
def drinks_add(request):
    uname = request.session['user']
    user = Users.objects.get(username=uname)
    # cid=request.session['cid']
    cater_order = Catering_order_table.objects.get(uname=user.username)
    print(str(cater_order))
    if request.method == "POST":
        tcategory = request.POST.get('drcategory')
        tcapcity = request.POST.get('drcapcity')
        items = item.objects.get(name=tcategory)
        drprice = items.price * int(tcapcity)
        cater_order.drcategory = tcategory
        cater_order.drcapacity = tcapcity
        cater_order.drprice=drprice
        cater_order.save()
        return render(request,'catering.html',{'msg':'Drinks added to menu'})
def relishes_add(request):
    uname = request.session['user']
    user = Users.objects.get(username=uname)
    # cid=request.session['cid']
    cater_order = Catering_order_table.objects.get(uname=user.username)
    print(str(cater_order))
    if request.method == "POST":
        tcategory = request.POST.get('recategory')
        tcapcity = request.POST.get('recapacity')
        items = item.objects.get(name=tcategory)
        rprice = items.price * int(tcapcity)
        cater_order.rcategory = tcategory
        cater_order.rcapacity = tcapcity
        cater_order.rprice=rprice
        cater_order.save()
        return render(request, 'catering.html', {'msg': 'Relishes added to menu'})
def maincourse_add(request):
    uname = request.session['user']
    user = Users.objects.get(username=uname)
    # cid=request.session['cid']
    cater_order = Catering_order_table.objects.get(uname=user.username)
    print(str(cater_order))
    if request.method == "POST":
        tcategory = request.POST.get('maincategory')
        tcapcity = request.POST.get('maincapcity')
        items = item.objects.get(name=tcategory)
        mprice = items.price * int(tcapcity)
        cater_order.maincategory = tcategory
        cater_order.maincapacity = tcapcity
        cater_order.mprice=mprice
        cater_order.save()
        return render(request, 'catering.html', {'msg': 'Main Course added to menu'})
def get_cater_items(request):
    uname = request.session['user']
    user = Users.objects.get(username=uname)
    # cid=request.session['cid']
    cater_order = Catering_order_table.objects.get(uname=user.username)
    if cater_order:
        t=int(cater_order.dprice)+int(cater_order.diprice)+int(cater_order.deprice)+int(cater_order.drprice)+int(cater_order.pprice)+int(cater_order.tprice)+int(cater_order.mprice)+int(cater_order.rprice)
        context={
            'cater':cater_order,
            'total':t,
            }
        return render(request,'order.html',context)
    else:
        return render(request, 'order.html', {'msg':'Menu NOt Selected!!!!!'})

def cater_order(request):
    return render(request,'end.html')
def feedback_add(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        mailid=request.POST.get('mailid')
        service=request.POST.get('service')
        food=request.POST.get('food')
        cleanliness=request.POST.get('cleanliness')
        ResponseTime=request.POST.get('Response Time')
        recommend=request.POST.get('recommend')
        rating=request.POST.get('rating')
        fb = Feedback(firstname=firstname,mailid=mailid,service=service,food=food,cleanliness=cleanliness,ResponseTime=ResponseTime,recommend=recommend,rating=rating)
        fb.save()
        return render(request,'feedback.html',{'msg':'Review Submited'})
def add_contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        query = request.POST.get('query')
        c=Contact(name=name,email=email,city=city,query=query)
        c.save()
        return render(request, 'contact.html', {'msg': 'Query Submited To Team'})
def pre_order(request):
    uname = request.session['user']
    user = Users.objects.get(username=uname)
    # cid=request.session['cid']
    cater_order =orders_foods.objects.all()
    return render(request, 'history.html', {'history': cater_order})
def pay_page(request):
    return render(request,'amount.html')
def search_add(request):
    if request.method=='POST':
        search = request.POST.get('search')
        items=item.objects.filter(name=search)
        return render(request,'search.html',{'items':items})
def cart_add_search(request,name):
    uname = request.session['user']
    user = Users.objects.get(username=uname)
    items = get_object_or_404(item,name=name)
    #if store.objects.filter(items__name=name).count() == 0:
    if request.method == 'POST':
        qty = request.POST.get('qty')
        storeItems.quantity = qty
        cart_item = storeItems.objects.create(
                items=items,
                users=user,
                quantity=qty,
            )

    return render(request,'menu.html',{'msg':'Added To Cart'})
def dummy(request):
    i=item.objects.all()
    return render(request,'dummy.html',{'items':i})
def add_rec(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        taste = request.POST.get('taste')
        timing = request.POST.get('timing')
        new = request.POST.get('new')
        rec=recommendation(name=name,email=email,age=age,phone=phone,kind=taste,time=timing,newvar=new)
        rec.save()
        if rec.time=="morning":
            rm=ritems.objects.filter(category="morning")
            return render(request,'morning.html',{'rm':rm})
        elif rec.time=="afternoon":
            ra = ritems.objects.filter(category="afternoon")
            return render(request, 'after.html',{'ra':ra})
        elif rec.time=="evening":
            re = ritems.objects.filter(category="evening")
            return render(request, 'eve.html',{'re':re})
        elif rec.time=="night":
            rn= ritems.objects.filter(category="night")
            return render(request, 'night.html',{'rn':rn})
        else:
            ro = ritems.objects.filter(category="other")
            return render(request, 'other.html',{'ro':ro})

def recomd(request):
    return render(request,'rec.html')
def cart_add_ritems(request,name):
    uname = request.session['user']
    user = Users.objects.get(username=uname)
    items = get_object_or_404(item,name=name)
    #if store.objects.filter(items__name=name).count() == 0:
    if request.method == 'POST':
        qty = request.POST.get('qty')
        storeItems.quantity = qty
        cart_item = storeItems.objects.create(
                items=items,
                users=user,
                quantity=qty,
            )
    uname = request.session['user']
    user = Users.objects.get(username=uname)
    cart_items = storeItems.objects.filter(users=user)
    amount = 0;
    for cart_item in cart_items:
        print(cart_item.quantity)
        print(cart_item.items.name)
        amount = amount + cart_item.quantity * cart_item.items.price
    print('amount is', amount)
    context = {
        'cart_items': cart_items,
        'total': amount,
    }
    return render(request,'cart.html', context)

