
from datetime import datetime

import qrcode as qrcode
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.contrib import auth
from django.http import HttpResponse, JsonResponse

from fake_product.models import *

from web3 import Web3, HTTPProvider
# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:7545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]
compiled_contract_path = r"D:\blockchain\node_modules\.bin\build\contracts\Structreq.json"
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0x8cc77dee291a9D4D31440Da7e5C99bd2b4048f1a'




def main_index(request):

    return render(request,'main_index.html')

def login(request):
    auth.logout(request)
    return render(request,'loginindex.html')

def logincode(request):
  uname=request.POST['textfield']
  pwd=request.POST['textfield2']
  try:
        ob=login_table.objects.get(username=uname,password=pwd)
        if ob.username != uname or ob.password != pwd:
            return HttpResponse('''<Script>alert("Invalid user and password!");window.location="/login"</Script>''')
        if ob.type == 'admin':
            obb=auth.authenticate(username="admin",password="admin")
            if obb is not None:
                auth.login(request,obb)
            request.session['lid'] = ob.id
            return HttpResponse('''<script>alert('welcome');window.location='/admin_home'</script>''')
        elif ob.type == 'manufacturer':
            obb = auth.authenticate(username="admin", password="admin")
            if obb is not None:
                auth.login(request, obb)
            request.session['lid'] = ob.id
            return HttpResponse('''<script>alert('welcome');window.location='/manufacturer'</script>''')
        elif ob.type == 'distributor':
            obb = auth.authenticate(username="admin", password="admin")
            if obb is not None:
                auth.login(request, obb)
            request.session['lid'] = ob.id
            return HttpResponse('''<script>alert('welcome');window.location='/distributor'</script>''')
        elif ob.type == 'shop':
            obb = auth.authenticate(username="admin", password="admin")
            if obb is not None:
                auth.login(request, obb)
            request.session['lid'] = ob.id
            return HttpResponse('''<script>alert('welcome');window.location='/shop'</script>''')
        elif ob.type == 'rejected':

            return HttpResponse('''<script>alert('You have been rejected');window.location='/'</script>''')
        else:
            return HttpResponse('''<script>alert('invalid username&password');window.location='/'</script>''')
  except:
        return HttpResponse('''<script>alert('invalid username&password');window.location='/'</script>''')

def logout(request):
    return render(request,'login.html')

def registration(request):
        nm=request.POST['textfield']
        plc=request.POST['textfield2']
        pt=request.FILES['file']
        pr=request.FILES['file2']
        em=request.POST['textfield3']
        ph=request.POST['textfield4']
        ty=request.POST['select']
        un=request.POST['textfield5']
        pw=request.POST['textfield6']
        fs=FileSystemStorage()
        fp=fs.save(pt.name, pt)
        fr=fs.save(pr.name, pr)
        ox = manufacturer_table.objects.filter(Q(email=em)|Q(ph_no=ph))
        if len(ox) == 0:
            oy = distributor_table.objects.filter(Q(email=em)|Q(ph_no=ph))
            if len(oy) == 0:
                oz = shop_table.objects.filter(Q(email=em)|Q(ph_no=ph))
                if len(oz) == 0:
                    ob = login_table()
                    ob.username = un
                    ob.password = pw
                    ob.type = 'pending'
                    ob.save()
                    if ty == "manufacturer":
                        ub = manufacturer_table()
                        ub.name = nm
                        ub.place = plc
                        ub.photo = fp
                        ub.proof = fr
                        ub.ph_no = ph
                        ub.email = em
                        ub.LOGIN = ob
                        ub.save()

                    elif ty == "distributor":
                        db = distributor_table()
                        db.name = nm
                        db.place = plc
                        db.photo = fp
                        db.proof = fr
                        db.ph_no = ph
                        db.email = em
                        db.LOGIN = ob
                        db.save()
                    else:
                        sb = shop_table()
                        sb.name = nm
                        sb.place = plc
                        sb.photo = fp
                        sb.proof = fr
                        sb.ph_no = ph
                        sb.email = em
                        sb.LOGIN = ob
                        sb.save()
                    return HttpResponse('''<script>alert('Registration Successful');window.location='/'</script>''')
                else:
                    return HttpResponse('''<script>alert('Email or phone number already existing');window.location='/'</script>''')
            else:
                return HttpResponse('''<script>alert('Email or phone number already existing');window.location='/'</script>''')
        else:
            return HttpResponse('''<script>alert('Email or phone number already existing');window.location='/'</script>''')



def reg_form(request):
    return render(request,'regindex.html')

def reg(request):
    username  = request.GET['username']
    print(username)
    data = {
        'is_taken': login_table.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message']="A user with this username already exists."

        # return HttpResponse("A user with this username already exists.")
    return JsonResponse(data)


@login_required(login_url='/')
def admin_home(request):
    return render(request,'Admin/admin index.html')


@login_required(login_url='/')
def managecategory(request):
    ob=category.objects.all().order_by('-id')
    return render(request,'Admin/manage category.html',{'val': ob})

def addcategory(request):
    return render(request, 'Admin/add category.html')

def addedcategory(request):
    cat=request.POST['textfield']
    des=request.POST['textarea']

    ob=category()
    ob.category=cat
    ob.details=des
    ob.save()

    return HttpResponse('''<script>;window.location='/managecategory#hero'</script>''')

def deletecategory(request,id):
    ob=category.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>;window.location='/managecategory'</script>''')

@login_required(login_url='/')
def manageproduct(request):
    ob=product.objects.all().order_by('-id')
    ob1=category.objects.all().order_by('-id')
    return render(request,'Admin/mng product.html',{'val': ob,'val1':ob1})

def addproduct(request):
    ob=category.objects.all()
    return render(request,'Admin/add product.html',{'val':ob})

def addedproduct(request):
    pn=request.POST['textfield']
    des=request.POST['textarea']
    p=request.FILES['file']
    ct=request.POST['select']
    fs=FileSystemStorage()
    fp=fs.save(p.name,p)
    pr=request.POST['textfield2']
    sz=request.POST.getlist('size')

    ub=product()
    ub.pname=pn
    ub.description=des
    ub.photo=fp
    ub.CATEGORY=category.objects.get(id=ct)
    ub.price=pr
    ub.stock='0'
    ub.size=sz

    ub.save()
    return HttpResponse('''<script>;window.location='/manageproduct#hero'</script>''')

def deleteproduct(request,id):
    ob=product.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>;window.location='/manageproduct#hero'</script>''')

def searchproduct(request):
    if 'textfield' in request.POST and 'select' in request.POST:
        pname=request.POST['textfield']
        cate=request.POST['select']
        ob=product.objects.filter(pname__icontains=pname,CATEGORY__id=cate)
        ob1 = category.objects.all()
        return render(request,'admin/mng product.html',{'val':ob,'val1':ob1,'cat':int(cate),'name':pname})
    # elif 'textfield' in request.POST:
    #     pname = request.POST['textfield']
    #     # cate = request.POST['select']
    #     ob = product.objects.filter(pname__icontains=pname)
    #     ob1 = category.objects.all().order_by('-id')
    #     return render(request, 'admin/mng product.html', {'val': ob,'val1':ob1})
    elif 'select' in request.POST:
        # pname=request.POST['textfield']
        cate=request.POST['select']
        ob=product.objects.filter(CATEGORY__category=cate)
        ob1 = category.objects.all().order_by('-id')
        return render(request,'admin/mng product.html',{'val':ob,'val1':ob1})

def editproduct(request,id):
    ob=product.objects.get(id=id)
    request.session['pid']=id
    os=category.objects.all()
    return render(request, "admin/edit product.html", {"i": ob, "val":os})

def updateproduct(request):
    if 'file' in request.FILES:
        pn = request.POST['textfield']
        des = request.POST['textarea']
        p = request.FILES['file']
        ct = request.POST['select']
        fs = FileSystemStorage()
        fp = fs.save(p.name, p)
        pr = request.POST['textfield2']
        sz = request.POST.getlist('size')

        ub = product.objects.get(id=request.session['pid'])
        ub.pname = pn
        ub.description = des
        ub.photo = fp
        ub.CATEGORY=category.objects.get(id=ct)
        ub.price = pr
        ub.size = sz

        ub.save()
        return HttpResponse('''<script>;window.location='/manageproduct#hero'</script>''')
    else:
        pn = request.POST['textfield']
        des = request.POST['textarea']

        ct = request.POST['select']

        pr = request.POST['textfield2']
        sz = request.POST.getlist('size')

        ub = product.objects.get(id=request.session['pid'])
        ub.pname = pn
        ub.description = des

        ub.CATEGORY = category.objects.get(id=ct)
        ub.price = pr
        ub.size = sz

        ub.save()
        return HttpResponse('''<script>;window.location='/manageproduct#hero'</script>''')

@login_required(login_url='/')
def verify_manufacturer(request):
    ob=manufacturer_table.objects.all().order_by('-id')
    return render(request,'Admin/verify manufacturer.html',{'val':ob,"name":""})

def accept_manufacturer(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='manufacturer'
    ob.save()
    return HttpResponse('''<script>;window.location='/verify_manufacturer#hero'</script>''')

def reject_manufacturer(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='rejected'
    ob.save()
    return HttpResponse('''<script>;window.location='/verify_manufacturer#hero'</script>''')


def searchman(request):
    name=request.POST['textfield']
    ob=manufacturer_table.objects.filter(name__icontains=name)
    return render(request,'admin/verify manufacturer.html',{'val':ob,"name":name})


@login_required(login_url='/')
def view_stockinfo(request):
    ob=product.objects.all().order_by('-id')
    for i in ob:
        obp=manufacture_product.objects.filter(PRODUCT__id=i.id).order_by("-date")
        c=0
        for j in obp:
            c=c+int(j.stock)
        i.stock=c
        if len(obp)>0:
            i.date=obp[0].date
        else:
            i.date=" "
        # print(i)
    obc=category.objects.all()
    return render(request,'Admin/view stock info.html',{'val':ob,"c":obc})

def searchproduct_a(request):
    if 'textfield' in request.POST and 'select' in request.POST:
        pname = request.POST['textfield']
        cate = request.POST['select']
        ob = product.objects.filter(pname__icontains=pname, CATEGORY__id=cate)
        ob1 = category.objects.all()
        return render(request, 'Admin/view stock info.html', {'val': ob, 'c': ob1,'cat':int(cate),'name':pname})
    elif 'select' in request.POST:
        cate = request.POST['select']
        ob = product.objects.filter(CATEGORY__category=cate)
        ob1 = category.objects.all()
        return render(request,'Admin/view stock info.html', {'val': ob, 'c': ob1,'cat':int(cate)})


@login_required(login_url='/')
def verify_distributor(request):
    ob=distributor_table.objects.all().order_by('-id')
    return render(request,'Admin/verify distributor.html',{'val':ob,'name':""})

def accept_distributor(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='distributor'
    ob.save()
    return HttpResponse('''<script>;window.location='/verify_distributor#hero'</script>''')

def reject_distributor(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='rejected'
    ob.save()
    return HttpResponse('''<script>;window.location='/verify_distributor#hero'</script>''')

def searchdist(request):
    name=request.POST['textfield']
    ob=distributor_table.objects.filter(name__icontains=name)
    return render(request,'admin/verify distributor.html',{'val':ob,'name':name})

@login_required(login_url='/')
def verify_shop(request):
    ob=shop_table.objects.all().order_by('-id')
    return render(request,'Admin/verify shop.html',{'val':ob})

def accept_shop(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='shop'
    ob.save()
    return HttpResponse('''<script>;window.location='/verify_shop#hero'</script>''')

def reject_shop(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='rejected'
    ob.save()
    return HttpResponse('''<script>;window.location='/verify_shop#hero'</script>''')

def searchshop(request):
    name=request.POST['textfield']
    ob=shop_table.objects.filter(name__icontains=name)
    return render(request,'admin/verify shop.html',{'val':ob,'name':name})

@login_required(login_url='/')
def manufacturer(request):
    return render(request,'Manufacturer/man index.html')

@login_required(login_url='/')
def viewproduct(request):
    ob=product.objects.all().order_by('-id')
    for i in ob:
        obp=manufacture_product.objects.filter(PRODUCT__id=i.id,MANFACTURER__LOGIN__id=request.session['lid'])
        if len(obp)>0:
            i.mdate=obp[0].date
            i.stock=obp[0].stock
        c = 0
        for j in obp:
            c = c + int(j.stock)
        i.stock = c
    ob1=category.objects.all().order_by('-id')
    return render(request,'Manufacturer/view product.html',{'val': ob,'val1':ob1})


def updatequantity(request,id):
    request.session['pid']=id
    ob=product.objects.get(id=id)
    print(type(ob.size))
    print(ob.size)
    list_data = ob.size[1:-1].split(', ')

    # Converting each element to a string and removing the quotes
    list_data = [element.strip()[1:-1] for element in list_data]




    return render(request,'Manufacturer/update quantity.html',{'val':ob,'sizee':list_data})


def updatedstock(request):
    stock=request.POST['textfield']
    size=request.POST['select']
    obp = manufacture_product.objects.filter(PRODUCT__id=request.session['pid'], MANFACTURER__LOGIN__id=request.session['lid'],size=size)
    # if len(obp)==0:
    ub = manufacture_product()
    ub.stock=stock
    ub.size=size
    ub.PRODUCT=product.objects.get(id=request.session['pid'])
    ub.date=datetime.today()
    ub.MANFACTURER=manufacturer_table.objects.get(LOGIN__id=request.session['lid'])
    ub.save()
    return HttpResponse('''<script>;window.location='/viewproduct#hero'</script>''')
    # else:
    #     ub=obp[0]
    #     ub.stock = stock
    #     ub.size = size
    #     ub.PRODUCT = product.objects.get(id=request.session['pid'])
    #     ub.date = datetime.today()
    #     ub.MANFACTURER = manufacturer_table.objects.get(LOGIN__id=request.session['lid'])
    #     ub.save()
    #     return HttpResponse('''<script>;window.location='/viewproduct#hero'</script>''')

def viewstock(request,id,name):
    request.session['d']=id
    request.session['n']=name
    ob=manufacture_product.objects.filter(PRODUCT__id=id).order_by('-id')
    return render(request,'Manufacturer/stock info.html',{'val':ob,'name':name})

def search_stock(request):
    date=request.POST['date']
    ob=manufacture_product.objects.filter(MANFACTURER__LOGIN__id=request.session['lid'],date=date,PRODUCT__id=request.session['d'])
    return  render(request,"Manufacturer/stock info.html",{'val':ob,"d":date,'name':request.session['n']})


def searchproducts(request):
    if 'textfield' in request.POST and 'select' in request.POST:
        pname = request.POST['textfield']
        cate = request.POST['select']
        ob = product.objects.filter(pname__icontains=pname, CATEGORY__id=cate)
        ob1 = category.objects.all()
        return render(request, 'Manufacturer/view product.html', {'val': ob, 'val1': ob1,'cat':int(cate),'name':pname})
    elif 'select' in request.POST:
        cate = request.POST['select']
        ob = product.objects.filter(CATEGORY__category=cate)
        ob1 = category.objects.all()
        return render(request,'Manufacturer/view product.html', {'val': ob, 'val1': ob1,'cat':int(cate)})

@login_required(login_url='/')
def view_update_dist_req(request):
    ob=distributor_req_master.objects.filter(MANFACTURER__LOGIN__id=request.session['lid']).order_by('-id')
    return render(request,'Manufacturer/view req&update status.html',{"val":ob})

def view_req_details(request,id):
    ob=distributor_req_details.objects.filter(DISTRIBUTOR_MASTER=id)
    l=[]
    total=0
    for i in ob:
        sum=int(i.quantity)*int(i.PRODUCT.PRODUCT.price)
        total = int(sum) + int(total)
        l.append({
            "pname":i.PRODUCT.PRODUCT.pname,
            "size":i.PRODUCT.size,
            "tp":sum,
            "quantity":i.quantity
        })
    t=int(total)
    return render(request,'Manufacturer/view req details.html',{"val":l,'total':t})


def accept_distreq(request,id):
    obb=distributor_req_details.objects.filter(DISTRIBUTOR_MASTER__id=id)

    for i in obb:
        print(i.PRODUCT.id)
        obd = manufacture_product.objects.get(id=i.PRODUCT.id)
        obd.stock=int(obd.stock)-int(i.quantity)
        obd.save()
        ob = distributor_req_master.objects.get(id=id)
        ob.status = 'Accepted'
        ob.save()

        for j in range(i.quantity):
            obdq=distributor_product()
            obdq.DISTRIBUTOR_REQUEST_id=i.id
            obdq.status="Available"
            obdq.date=datetime.today()
            obdq.save()


    #     blockchain connection
            ob1 = qrcode.QRCode(
                version=1,  # The QRcode version (1-40), higher is a larger code.
                error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L, M, Q, H).
                box_size=10,  # The size of each box in the QRcode.
                border=4,  # The border size around the QRcode.
            )
            # Add data to the QRcode
            ob1.add_data(str(obdq.id))
            ob1.make(fit=True)

            # Create a PIL (Python Imaging Library) image from the QRcode data
            ob1 = ob1.make_image(fill_color="black", back_color="white")
            # Save the image to a file or display it
            ob1.save("media/qr/" + str(obdq.id) + ".png")
            with open(
                    r'D:\blockchain\node_modules\.bin\build\contracts\Structreq.json') as file:
                contract_json = json.load(file)  # load contract info as JSON
                contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
            contract = web3.eth.contract(address='0x80144D70BD035CA7A46CE688b548A9CFa8eaE5e7', abi=contract_abi)
            blocknumber = web3.eth.get_block_number()
            message2 = contract.functions.addreq(blocknumber + 1, str(request.session['lid']), str(ob.MANFACTURER.id),
                                                 str(obdq.id), str(1),
                                                 str(datetime.today()), str('distributor request')
                                                 ).transact({'from':web3.eth.accounts[0]})

    return HttpResponse('''<script>;window.location='/view_update_dist_req'</script>''')

def reject_distreq(request,id):
    ob=distributor_req_master.objects.get(id=id)
    ob.status='Rejected'
    ob.save()
    return HttpResponse('''<script>;window.location='/view_update_dist_req'</script>''')

def search_req(request):
    date=request.POST['textfield2']
    ob = distributor_req_master.objects.filter(MANFACTURER__LOGIN__id=request.session['lid'],date=date)
    return  render(request,"Manufacturer/view req&update status.html",{'val':ob,'date':date})

@login_required(login_url='/')
def distributor(request):
    return render(request,'Distributor/distributor index.html')


@login_required(login_url='/')
def view_manufacturer(request):
    ob=manufacturer_table.objects.all().order_by('-id')
    return render(request,'Distributor/view manufacturer.html',{'val': ob,'name':""})

def searchman1(request):
    name=request.POST['textfield']
    ob=manufacturer_table.objects.filter(name__icontains=name)
    return render(request,'Distributor/view manufacturer.html',{'val':ob,'name':str(name)})


def view_product(request,id):
    op=category.objects.all().order_by('-id')
    request.session['mid']=id
    ob=manufacture_product.objects.filter(MANFACTURER__id=id).order_by('-id')
    return render(request,'Distributor/view product.html',{"val":ob,'val1':op})

def searchproduct_d(request):
    # if 'textfield' in request.POST and 'select' in request.POST:
    #     pname = request.POST['textfield']
    #     cate = request.POST['select']
    #     ob = product.objects.filter(PRODUCT__pname__icontains=pname,PRODUCT__CATEGORY__category=cate)
    #     ob1 = category.objects.all()
    #     return render(request,'Distributor/view product.html', {'val': ob, 'val1': ob1})
    # elif 'select' in request.POST:
    #     cate = request.POST['select']
    #     ob = product.objects.filter(PRODUCT__CATEGORY__category=cate)
    #     ob1 = category.objects.all()
    #     return render(request,'Distributor/view product.html', {'val': ob, 'val1': ob1})
    # #
    pname=request.POST['textfield']
    op = category.objects.all().order_by('-id')
    cate=request.POST['select']
    ob=manufacture_product.objects.filter(PRODUCT__pname__icontains=pname,PRODUCT__CATEGORY__id=cate)
    return render(request,'Distributor/view product.html',{'val':ob,'val1':op,'name':pname,'cat':int(cate)})


def send_req(request,id,p,s):
    request.session['pid']=id
    request.session['s']=s
    return render(request, 'Distributor/send request.html',{"p":p})

def stock(request):
    stock = request.GET['st']

    obb=manufacture_product.objects.get(id=request.session["pid"])
    pstock=obb.stock
    print(stock)

    print(obb.stock,"====")
    if int(pstock)>= int(stock):
        data = {"stock": "l"}
    else:
        data = {"stock": "g"}

    print(data)

    # data = {
    #     'is_taken': manufacture_product.objects.filter(stock__gt=stock).exists()
    # }
    # if data['is_taken']:
    #     data['error_message']="stock is greater."

        # return HttpResponse("A user with this username already exists.")



    return JsonResponse(data)


def add_request(request):
    pid=request.session['pid']
    mid=request.session['mid']
    qty=request.POST['qty']

    ob=distributor_req_master.objects.filter(MANFACTURER__id=mid,DISTRIBUTOR__LOGIN__id=request.session['lid'],status='cart')
    if len(ob)==0:
        ob=distributor_req_master()
        ob.MANFACTURER=manufacturer_table.objects.get(id=mid)
        ob.DISTRIBUTOR=distributor_table.objects.get(LOGIN__id=request.session['lid'])
        ob.status='cart'
        ob.date=datetime.today()
        ob.amount=0
        ob.save()
    else:
        ob=ob[0]

    obc=distributor_req_details.objects.filter(DISTRIBUTOR_MASTER__id=ob.id,PRODUCT__id=pid)
    if len(obc)==0:
        obc=distributor_req_details()
        obc.DISTRIBUTOR_MASTER=ob
        obc.PRODUCT=manufacture_product.objects.get(id=pid)
        obc.quantity=qty
        obc.save()
    else:
        obc=obc[0]
        obc.quantity=int(obc.quantity)+int(qty)
        obc.save()
    obc=distributor_req_details.objects.filter(DISTRIBUTOR_MASTER__id=ob.id)
    t=0
    for i in obc:
        i.tp=int(i.quantity)*int(i.PRODUCT.PRODUCT.price)
        t=t+int(i.tp)
        request.session['amt']=t
    return render(request,'Distributor/view product req.html',{"val":obc,"t":t})


def finish_order(request):
    # pid = request.session['pid']
    amt=request.session['amt']
    mid = request.session['mid']
    print(amt)
    ob=distributor_req_master.objects.filter(MANFACTURER__id=mid, DISTRIBUTOR__LOGIN__id=request.session['lid'],status='cart').update(status='pending',amount=float(amt))

    # ob[0].status='pending'
    # ob[0].amount=float(amt)
    # ob[0].save()

    return HttpResponse('''<script>alert('order successful');window.location='/distributor'</script>''')


@login_required(login_url='/')
def view_product_req(request):
    return render(request,'Distributor/view product req.html')

@login_required(login_url='/')
def view_reqstatus(request):
    ob=distributor_req_master.objects.filter(DISTRIBUTOR__LOGIN__id=request.session['lid']).order_by('-id')
    return render(request,'Distributor/view status.html',{"val":ob,"date":""})

def view_reqstatus_details(request,id):
    # request.session['d']=id
    ob = distributor_req_details.objects.filter(DISTRIBUTOR_MASTER=id)
    l = []
    total = 0
    for i in ob:
        sum = int(i.quantity) * int(i.PRODUCT.PRODUCT.price)
        total = int(sum) + int(total)
        l.append({
            "pname": i.PRODUCT.PRODUCT.pname,
            "size": i.PRODUCT.size,
            "tp": sum,
            "quantity": i.quantity
        })
    t = int(total)
    return render(request, 'Distributor/view req status.html', {"val": l, 'total': t})


def search_req_status(request):
    date=request.POST['date']
    ob=distributor_req_master.objects.filter(DISTRIBUTOR__LOGIN__id=request.session['lid'],date=date)
    return  render(request,'Distributor/view status.html',{'val':ob,'date':date})

@login_required(login_url='/')
def view_reqst_shop(request):
    ob = shop_req_master.objects.filter(DISTRIBUTOR__LOGIN__id=request.session['lid']).order_by('-id')
    return render(request,'Distributor/view req from shop.html', {"val": ob,"date":""})

def view_req_details_s(request,id):
    ob=shop_req_details.objects.filter(SHOP_MASTER=id)
    l=[]
    total=0
    for i in ob:
        sum=int(i.quantity)*int(i.PRODUCT.PRODUCT.price)
        total = int(sum) + int(total)
        l.append({
            "pname":i.PRODUCT.PRODUCT.pname,
            "size":i.PRODUCT.size,
            "tp":sum,
            "quantity":i.quantity
        })
    t=int(total)
    return render(request,'Distributor/view req details.html',{"val":l,'total':t})


def accept_shopreq(request,id):
    obb=shop_req_details.objects.filter(SHOP_MASTER__id=id)
    for i in obb:
        d=i.SHOP_MASTER.DISTRIBUTOR.id
        pid=i.PRODUCT.PRODUCT.id
        print(i.PRODUCT.id)

        oc=distributor_product.objects.filter(DISTRIBUTOR_REQUEST__PRODUCT__PRODUCT__id=pid,DISTRIBUTOR_REQUEST__DISTRIBUTOR_MASTER__DISTRIBUTOR__id=d,status='Available')

        ob = shop_req_master.objects.get(id=id)
        ob.status = 'Accepted'
        ob.save()

        print(i.quantity)
        print(len(oc))
        for j in range(i.quantity):
            obdq=shop_product()
            obdq.SHOP=ob.SHOP
            obdq.DISTRIBUTOR_PRODUCT_id=oc[j].id
            obdq.status="Available"
            obdq.date=datetime.today()
            obdq.save()
            print("+++++++++++++++++++++++++++++++++++++++++++")

            obc=distributor_product.objects.get(id=oc[j].id)
            obc.status='na'
            obc.save()
            obc.save()

            with open(
                    r'D:\blockchain\node_modules\.bin\build\contracts\Structreq.json') as file:
                contract_json = json.load(file)  # load contract info as JSON
                contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
            contract = web3.eth.contract(address='0x8cc77dee291a9D4D31440Da7e5C99bd2b4048f1a', abi=contract_abi)
            blocknumber = web3.eth.get_block_number()
            message2 = contract.functions.addreq(blocknumber + 1, str(request.session['lid']), str(ob.SHOP.id),
                                                 str(obc.id), str(1),
                                                 str(datetime.today()), str('shop request')
                                                 ).transact({'from': web3.eth.accounts[0]})


    return HttpResponse('''<script>;window.location='/view_reqst_shop'</script>''')

def reject_shopreq(request,id):
    ob=shop_req_master.objects.get(id=id)
    ob.status='Rejected'
    ob.save()
    return HttpResponse('''<script>;window.location='/view_reqst_shop'</script>''')

def search_req_s(request):
    date=request.POST['textfield2']
    ob = shop_req_master.objects.filter(DISTRIBUTOR__LOGIN__id=request.session['lid'],date=date)
    return  render(request,'Distributor/view req from shop.html',{'val':ob,"date":date})




@login_required(login_url='/')
def shop(request):
    return render(request,'Shop/shop index.html')

@login_required(login_url='/')
def view_distributor(request):
    ob = distributor_table.objects.all().order_by('-id')
    return render(request, 'Shop/view distributor.html', {'val': ob,'name':""})

def searchdist1(request):
    name=request.POST['textfield']
    ob=distributor_table.objects.filter(name__icontains=name)
    return render(request,'Shop/view distributor.html',{'val':ob,'name':name})

def view_product_s(request,id):
    op=category.objects.all().order_by('-id')
    request.session['did'] = id
    ob = distributor_req_details.objects.filter(DISTRIBUTOR_MASTER__DISTRIBUTOR__id=id).order_by('-id')
    res=[]
    ids=[]
    for i in ob:
        if i.PRODUCT.id not in ids:
            j=distributor_product.objects.filter(status='Available',DISTRIBUTOR_REQUEST__DISTRIBUTOR_MASTER__DISTRIBUTOR__id=i.DISTRIBUTOR_MASTER.DISTRIBUTOR.id,DISTRIBUTOR_REQUEST__PRODUCT__id=i.PRODUCT.id )
            i.quantity=len(j)
            ids.append(i.PRODUCT.id)
            res.append(i)
    return render(request,'Shop/view product.html', {"val": res, 'val1': op})

def searchproduct_s(request):
    op = category.objects.all().order_by('-id')
    pname=request.POST['textfield']
    cate=request.POST['select']
    id=request.session['did']
    ob = distributor_req_details.objects.filter(DISTRIBUTOR_MASTER__DISTRIBUTOR__id=id, PRODUCT__PRODUCT__CATEGORY__id = cate)

    if pname!="":

        ob = distributor_req_details.objects.filter(DISTRIBUTOR_MASTER__DISTRIBUTOR__id=id,PRODUCT__PRODUCT__CATEGORY__id =cate,PRODUCT__PRODUCT__pname__icontains=pname)

    return render(request,'Shop/view product.html',{'val':ob, 'val1': op,'name':pname,'cat':int(cate)})


def send_request(request,id,p,s):
    request.session['spid']=id
    request.session['s']=s
    return render(request,'Shop/send request.html',{"p":p})



def stock1(request):
    quantity = request.GET['st']
    id=request.session['did']
    obb=distributor_product.objects.filter(status="Available",DISTRIBUTOR_REQUEST__DISTRIBUTOR_MASTER__DISTRIBUTOR__id=id,DISTRIBUTOR_REQUEST__PRODUCT__id=request.session["spid"])
    # obb=distributor_req_details.objects.get(PRODUCT__id=request.session["spid"])
    pstock=len(obb)
    print(quantity)

    # print(obb.quantity,"====")
    if int(pstock)>= int(quantity):
        data = {"quantity": "l"}
    else:
        data = {"quantity": "g"}

    print(data)
    return JsonResponse(data)





def add_request_s(request):
        pid=request.session['spid']
        did=request.session['did']
        qty=request.POST['qty']

        ob=shop_req_master.objects.filter(DISTRIBUTOR__id=did,SHOP__LOGIN__id=request.session['lid'],status='cart')
        if len(ob)==0:
            ob=shop_req_master()
            ob.DISTRIBUTOR=distributor_table.objects.get(id=did)
            ob.SHOP=shop_table.objects.get(LOGIN__id=request.session['lid'])
            ob.status='cart'
            ob.date=datetime.today()
            ob.amount=0
            ob.save()
        else:
            ob=ob[0]

        obc=shop_req_details.objects.filter(SHOP_MASTER__id=ob.id,PRODUCT__id=pid)
        if len(obc)==0:
            obc=shop_req_details()
            obc.SHOP_MASTER=ob
            obc.PRODUCT=manufacture_product.objects.get(id=pid)
            # obc.PRODUCT=shop_req_details.objects.get(PRODUCT__id=pid)
            obc.quantity=qty
            obc.save()
        else:
            obc=obc[0]
            obc.quantity=int(obc.quantity)+int(qty)
            obc.save()
        obc=shop_req_details.objects.filter(SHOP_MASTER__id=ob.id)
        t=0
        for i in obc:
            i.tp=int(i.quantity)*int(i.PRODUCT.PRODUCT.price)
            t=t+int(i.tp)
            request.session['amt']=t
        return render(request,'Shop/view product req.html',{"val":obc,"t":t})


def finish_order_s(request):
    # pid = request.session['pid']
    amt=request.session['amt']
    did = request.session['did']
    print(amt)
    ob=shop_req_master.objects.filter(DISTRIBUTOR__id=did,SHOP__LOGIN__id=request.session['lid'],status='cart').update(status='pending',amount=float(amt))

    # ob[0].status='pending'
    # ob[0].amount=float(amt)
    # ob[0].save()

    return HttpResponse('''<script>alert('order successful');window.location='/shop'</script>''')



@login_required(login_url='/')
def view_request_status(request):
    ob=shop_req_master.objects.filter(SHOP__LOGIN__id=request.session['lid']).order_by('-id')
    return render(request,'Shop/view req status.html',{"val":ob,"date":""})

def view_reqstatus_details_s(request,id):
    # request.session['d']=id
    ob = shop_req_details.objects.filter(SHOP_MASTER=id)
    l = []
    total = 0
    for i in ob:
        sum = int(i.quantity) * int(i.PRODUCT.PRODUCT.price)
        total = int(sum) + int(total)
        l.append({
            "pname": i.PRODUCT.PRODUCT.pname,
            "size": i.PRODUCT.size,
            "tp": sum,
            "quantity": i.quantity
        })
    t = int(total)
    return render(request, 'Shop/view req details.html', {"val": l, 'total': t})


def search_req_status_s(request):
    date=request.POST['date']
    ob=shop_req_master.objects.filter(SHOP__LOGIN__id=request.session['lid'],date=date)
    return  render(request,'Shop//view req status.html',{'val':ob,"date":date})



@login_required(login_url='/')
def view_order(request):
    order_id=[]
    ob=order_details.objects.filter(PRODUCT__SHOP_MASTER__SHOP__LOGIN__id=request.session['lid']).order_by('-id')
    for i in ob:
        order_id.append(i.ORDER.id)
    ob1 = order.objects.filter(id__in=order_id).order_by('-id')
    return render(request, 'Shop/view purchase details.html',{'val':ob1,"date":""})

def viewmore(request,id):
    detail_obj=order_details.objects.filter(ORDER_id=id)
    return render(request,'Shop/view more product.html',{'val':detail_obj,'total':detail_obj[0].ORDER.amount,'name':detail_obj[0].ORDER.USER.name,'phone':detail_obj[0].ORDER.USER.ph_no,'gst':detail_obj[0].ORDER.gst})


def view_ordersearch(request):
    date=request.POST['textfield']
    order_id = []
    ob = order_details.objects.filter(PRODUCT__SHOP_MASTER__SHOP__LOGIN__id=request.session['lid'])
    for i in ob:
        order_id.append(i.ORDER.id)
    ob1 = order.objects.filter(id__in=order_id,date=date)
    return render(request, 'Shop/view purchase details.html',{'val':ob1,"date":date})

@login_required(login_url='/')
def managebill(request):
    try:
        OB1=bill.objects.get(SHOP__LOGIN__id=request.session['lid'],status='CART')
        ob = bill_details.objects.filter(BILL__SHOP__LOGIN__id=request.session['lid'],BILL__status='CART')

        return render(request,'Shop/manage bill.html',{'val': ob,'total':OB1.amount,'oid':OB1.id})
    except:
        ob = bill_details.objects.filter(BILL__SHOP__LOGIN__id=request.session['lid'],BILL__status='CART')
        return render(request,'Shop/manage bill.html',{'val': ob,'total':0,'oid':0})



def deleteviewproduct(request,id,qid):
    print(request.POST, "uuuuuuuuuuuuuuuu")
    obd = bill_details.objects.get(id=id)
    j=obd.amount
    obp = product.objects.get(id=obd.PRODUCT.id)
    obp.stock = float(obp.stock) + int(qid)
    obp.save()
    ob11 = bill.objects.get(id=obd.BILL.id)
    o=int(ob11.amount)-int(j)
    ob11.amount=o
    ob11.save()
    id=obd.BILL.id
    obd.delete()
    ob2 = bill_details.objects.filter(BILL__id=id)
    if len(ob2) == 0:
        ob1 = bill.objects.get(id=id)
        ob1.delete()
    return HttpResponse('''<Script>;window.location="/managebill"</Script>''')

def addbill(request,id):
    request.session['oid']=id
    # request.POST['qid']=qid
    return render(request,'Shop/add bill.html')



def addbillcode(request):
    uname=request.POST['textfield']
    pswd=request.POST['textfield2']
    qty1 = bill.objects.get(id=request.session['oid'])
    qt2=bill_details.objects.filter(BILL__id=request.session['oid'])
    for i in qt2:
        qq = shop_product.objects.filter(SHOP__LOGIN__id=request.session['lid'],DISTRIBUTOR_PRODUCT__DISTRIBUTOR_REQUEST__PRODUCT__PRODUCT__id=i.PRODUCT.id, status='Available')
        for j in range(i.quantity):
            obs=shop_product.objects.get(id=qq[j].id)
            obs.status='na';
            obs.save()
            with open(r'D:\blockchain\node_modules\.bin\build\contracts\Structreq.json') as file:
                contract_json = json.load(file)  # load contract info as JSON
                contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
            contract = web3.eth.contract(address='0x8cc77dee291a9D4D31440Da7e5C99bd2b4048f1a', abi=contract_abi)
            blocknumber = web3.eth.get_block_number()
            message2 = contract.functions.addreq(blocknumber + 1, str(request.session['lid']), str(uname),
                                                 str(obs.DISTRIBUTOR_PRODUCT.id), str(1),
                                                 str(datetime.today()), str('shop bill')
                                                 ).transact({'from': web3.eth.accounts[0]})

    qty1.status = 'Paid'
    qty1.user = uname
    qty1.ph_no =pswd
    qty1.save()
    return HttpResponse('''<script>alert('Bill Added');window.location='/managebill'</script>''')

@login_required(login_url='/')
def viewbill(request):
    ob = bill.objects.filter(SHOP__LOGIN__id=request.session['lid']).order_by('-id')
    return render(request, 'Shop/view bill.html',{'val':ob,"date":""})


def view_billsearch(request):
    date=request.POST['textfield']
    id = []
    ob = bill_details.objects.filter(BILL__SHOP__LOGIN__id=request.session['lid'])
    for i in ob:
        id.append(i.BILL.id)
    ob1 = bill.objects.filter(id__in=id,date=date)
    return render(request, 'Shop/view bill.html',{'val':ob1,"date":date})


def viewmore_bill(request,id):
     detail_obj = bill_details.objects.filter(BILL_id=id)
     return render(request, 'Shop/view more .html', {'val': detail_obj,'total':detail_obj[0].amount,'name':detail_obj[0].BILL.user,'phone':detail_obj[0].BILL.ph_no,'gst':detail_obj[0].BILL.amount})


def ordrprdct(request):
    pob=shop_product.objects.filter(SHOP__LOGIN__id=request.session['lid']).order_by('-id')
    rid=[]
    for i in pob:
        rid.append(i.DISTRIBUTOR_PRODUCT.DISTRIBUTOR_REQUEST.PRODUCT.PRODUCT.id)
    print(rid,"))))))))))))))))))))))))))))))))))")
    print(rid,"))))))))))))))))))))))))))))))))))")
    print(rid,"))))))))))))))))))))))))))))))))))")
    print(rid,"))))))))))))))))))))))))))))))))))")
    my_objects = product.objects.filter(id__in=rid)
    for i in my_objects:
        ob=shop_product.objects.filter(SHOP__LOGIN__id=request.session['lid'],DISTRIBUTOR_PRODUCT__DISTRIBUTOR_REQUEST__PRODUCT__PRODUCT__id=i.id,status='Available')
        i.stock=len(ob)
    print(my_objects)

    # Set the number of items per page
    items_per_page = 3

    # Create a Paginator instance
    paginator = Paginator(my_objects, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)
    return render(request, 'Shop/order products.html',{'my_objects':my_objects,"name":""})







def srchordr_products(request):
    n = request.POST['textfield']
    pob = shop_product.objects.filter(SHOP__LOGIN__id=request.session['lid']).order_by('-id')
    rid = []
    for i in pob:
        rid.append(i.DISTRIBUTOR_PRODUCT.DISTRIBUTOR_REQUEST.PRODUCT.PRODUCT.id)

    print(rid, "))))))))))))))))))))))))))))))))))")
    my_objects = product.objects.filter(id__in=rid,pname__icontains=n)
    for i in my_objects:
        ob = shop_product.objects.filter(SHOP__LOGIN__id=request.session['lid'], DISTRIBUTOR_PRODUCT__DISTRIBUTOR_REQUEST__PRODUCT__PRODUCT__id=i.id,status='Available')
        i.stock = len(ob)
    print(my_objects)



    # Set the number of items per page
    items_per_page = 3

    # Create a Paginator instance
    paginator = Paginator(my_objects, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)

    return render(request, 'Shop/order products.html', {'my_objects': my_objects,"name":n})





def ordrdtls(request,id):
    request.session['pid']=id
    ob=product.objects.get(id=id)
    ob1 = shop_product.objects.filter(SHOP__LOGIN__id=request.session['lid'],DISTRIBUTOR_PRODUCT__DISTRIBUTOR_REQUEST__PRODUCT__PRODUCT__id=ob.id, status='Available')
    ob.stock = len(ob1)
    return render(request, 'Shop/order details.html',{'val':ob})







def ordrprdctcode(request):
    btn=request.POST['Submit']
    if btn == 'BILL NOW':
        qty = request.POST['textfield3']
        qq = shop_product.objects.filter(SHOP__LOGIN__id=request.session['lid'],DISTRIBUTOR_PRODUCT__DISTRIBUTOR_REQUEST__PRODUCT__PRODUCT__id=request.session['pid'],status='Available')
        tt = int(qq.DISTRIBUTOR_PRODUCT.DISTRIBUTOR_REQUEST.PRODUCT.PRODUCT.price) * int(qty)
        stock = len(qq)
        print(stock, qty, "jjjjjjjjjjjjjjjjjjjjjj")
        nstk = int(stock) - int(qty)
        if stock >= int(qty):
            up = product.objects.get(id=request.session['pid'])
            up.stock = nstk
            up.save()
            q = bill.objects.filter(SHOP=shop_table.objects.get(LOGIN__id=request.session['lid']), status='CART')
            if len(q) == 0:
                qt = bill()
                qt.date = datetime.now()
                qt.SHOP = shop_table.objects.get(LOGIN__id=request.session['lid'])
                qt.status = 'CART'
                qt.amount = tt
                qt.user = 'pending'
                qt.ph_no = '0'
                qt.save()
                qty1 = bill_details()
                qty1.quantity = qty
                qty1.PRODUCT = product.objects.get(id=request.session['pid'])
                qty1.BILL = qt
                qty1.amount = tt
                qty1.date = datetime.today()
                qty1.save()
                return HttpResponse('''<script>alert('ORDER NOW');window.location='/managebill'</script>''')
            else:
                total = int(q[0].amount) + int(tt)
                qt = bill.objects.get(id=q[0].id)
                qt.amount = total
                qt.save()
                qty1 = bill_details.objects.filter(PRODUCT__id=request.session['pid'], BILL__id=q[0].id)
                if len(qty1) == 0:
                    qqt = bill_details()
                    qqt.BILL = q[0]
                    qqt.amount = tt
                    qqt.PRODUCT = product.objects.get(id=request.session['pid'])
                    qqt.quantity = qty

                    qqt.date = datetime.today()
                    qqt.save()
                else:
                    qry1 = bill_details.objects.get(id=qty1[0].id)
                    quty = int(qty1[0].quantity) + int(qty)
                    ott = int(qq.price) * int(quty)
                    ott = int(str(ott + ott * 0.08).split('.')[0])
                    qry1.amount = ott
                    qry1.quantity = quty
                    qry1.date = datetime.today()
                    qry1.save()
                    return HttpResponse('''<script>alert('placed order successfuly');window.location='/managebill'</script>''')
        else:
            return HttpResponse('''<script>alert('OUT OF STOCK');window.location='/ordrprdct'</script>''')

    else:

        qty=request.POST['textfield3']
        pp=product.objects.get(id=request.session['pid'])
        qq = shop_product.objects.filter(SHOP__LOGIN__id=request.session['lid'],DISTRIBUTOR_PRODUCT__DISTRIBUTOR_REQUEST__PRODUCT__PRODUCT__id=request.session['pid'],status='Available')

        tt = int(pp.price)* int(qty)
        tt=tt+(tt*0.08)
        tt=int(str(tt).split('.')[0])
        stock =len(qq)
        print(stock,qty,"jjjjjjjjjjjjjjjjjjjjjj")
        nstk = int(stock) - int(qty)
        if stock >= int(qty):
            up=product.objects.get(id=request.session['pid'])
            up.stock=nstk
            up.save()
            q=bill.objects.filter(SHOP=shop_table.objects.get(LOGIN__id=request.session['lid']),status='CART')
            if len(q)==0:
                qt=bill()
                qt.date=datetime.now()
                qt.SHOP=shop_table.objects.get(LOGIN__id=request.session['lid'])
                qt.status='CART'
                qt.amount=tt
                qt.user = 'pending'
                qt.ph_no = '0'
                qt.save()
                qty1=bill_details()
                qty1.quantity=qty
                qty1.PRODUCT=product.objects.get(id=request.session['pid'])
                qty1.BILL=qt
                qty1.amount=tt
                qty1.date = datetime.today()
                qty1.save()
                return HttpResponse('''<script>alert('ORDER NOW');window.location='/managebill'</script>''')
            else:
                total = int(q[0].amount) + int(tt)
                qt=bill.objects.get(id=q[0].id)
                qt.amount=total
                qt.save()
                qty1=bill_details.objects.filter(PRODUCT__id=request.session['pid'],BILL__id=q[0].id)
                if len(qty1)==0:
                    qqt=bill_details()
                    qqt.BILL=q[0]
                    qqt.amount = tt
                    qqt.PRODUCT=product.objects.get(id=request.session['pid'])
                    qqt.quantity=qty

                    qqt.date=datetime.today()
                    qqt.save()
                else:
                    qry1=bill_details.objects.get(id=qty1[0].id)
                    quty=int(qty1[0].quantity) + int(qty)
                    ott = int(pp.price)* int(quty)
                    ott=int(str(ott+ott*0.08).split('.')[0])
                    qry1.amount=ott
                    qry1.quantity=quty
                    qry1.date=datetime.today()
                    qry1.save()
                return HttpResponse('''<script>alert('ADD TO CART');window.location='/ordrprdct'</script>''')
        else:
            return HttpResponse('''<script>alert('OUT OF STOCK');window.location='/ordrprdct'</script>''')



@login_required(login_url='/')
def view_returninfo(request):
    ob=return_table.objects.filter(ORDER__PRODUCT__SHOP_MASTER__SHOP__LOGIN=request.session['lid']).order_by('-id')
    return render(request,'Shop/view return info.html',{'val':ob,"date":""})

def rejectreturninfo(request,id):
    ob=return_table.objects.get(id=id)
    ob.status='Rejected'
    ob.save()
    return HttpResponse('''<script>;window.location='/view_returninfo'</script>''')

def acceptreturninfo(request,id):
    ob=return_table.objects.get(id=id)
    ob.status='Accepted'
    ob.save()
    return HttpResponse('''<script>;window.location='/view_returninfo'</script>''')

def search_retuninfo(request):
    date=request.POST['date']
    ob=return_table.objects.filter(date=date)
    return  render(request,'Shop/view return info.html',{'val':ob,"d":date})




#--------------------------------------webservices--------------------------------------#

import json
def and_logincode(request):
  print(request.POST)
  uname=request.POST['uname']
  pwd=request.POST['pass']
  try:
        ob=login_table.objects.get(username=uname,password=pwd)
        data={"task":"valid","lid":ob.id}
        r=json.dumps(data)
        return HttpResponse(r)

  except Exception as e:
      print(e)

      data = {"task": "invalid"}
      r = json.dumps(data)
      return HttpResponse(r)

def and_registration(request):
      name = request.POST['name']
      place = request.POST['place']
      post = request.POST['post']
      pin = request.POST['pin']
      phone = request.POST['phone']
      email = request.POST['email']
      un = request.POST['username']
      pw = request.POST['password']

      ob = login_table()
      ob.username = un
      ob.password = pw
      ob.type = 'user'
      ob.save()

      ub = user_table()
      ub.name = name
      ub.place = place
      ub.post = post
      ub.pin = pin
      ub.ph_no = phone
      ub.email = email
      ub.LOGIN = ob
      ub.save()
      data={"task":"valid"}
      r=json.dumps(data)
      return HttpResponse(r)




def and_category(request):
    ob = category.objects.all()
    list = []
    for i in ob:
        row = {"cat": i.category,"cid": i.id}
        list.append(row)
    d = json.dumps(list)
    return HttpResponse(d)



def and_vshop(request):
    ob=shop_table.objects.all()
    list=[]
    for i in ob:
        row={"name":i.name,"place":i.place,"phone":i.ph_no,"email":i.email,"photo":i.photo.url,"id":i.id}
        list.append(row)
    d=json.dumps(list)
    return HttpResponse(d)


def and_vshop_search(request):
    s=request.POST['sn']
    ob=shop_table.objects.filter(name__istartswith=s)
    list=[]
    for i in ob:
        row={"name":i.name,"place":i.place,"phone":i.ph_no,"email":i.email,"photo":i.photo.url,"id":i.id}
        list.append(row)
    d=json.dumps(list)
    return HttpResponse(d)


def and_vproduct_details(request):
    # shopid=request.POST["shopid"]
    ob=shop_req_details.objects.all()
    list=[]
    for i in ob:

        row={"name":i.PRODUCT.PRODUCT.pname,"price":str(i.PRODUCT.PRODUCT.price),"photo":i.PRODUCT.PRODUCT.photo.url,"desc":i.PRODUCT.PRODUCT.description,"cat":i.PRODUCT.PRODUCT.CATEGORY.category,"id":i.PRODUCT.PRODUCT.id}
        if row not in list:
            list.append(row)
    d=json.dumps(list)
    print(list)
    return HttpResponse(d)



def and_vproduct(request):
    shopid=request.POST["shopid"]
    ob=shop_req_details.objects.filter(SHOP_MASTER__SHOP=shopid)
    list=[]
    # for i in ob:
    #
    #     row={"name":i.PRODUCT.PRODUCT.pname,"price":str(i.PRODUCT.PRODUCT.price),"photo":i.PRODUCT.PRODUCT.photo.url,"id":i.id}
    #     if row not in list:
    #         list.append(row)

    productlist = []

    for i in ob:
        if i.PRODUCT.PRODUCT.id in productlist:
            pass
        else:
            productlist.append(i.PRODUCT.PRODUCT.id)
            row={"name":i.PRODUCT.PRODUCT.pname,"price":str(i.PRODUCT.PRODUCT.price),"photo":i.PRODUCT.PRODUCT.photo.url,"id":i.id}
            list.append(row)



    d=json.dumps(list)
    print(list)
    return HttpResponse(d)


def and_vproduct_search(request):
    print(request.POST)
    cat=request.POST['cat']
    pn=request.POST['pn']
    shopid=request.POST['shopid']
    # ob=product.objects.filter(CATEGORY__id=cat,pname__istartswith=pn,SHOP_MASTER__SHOP=shopid)
    # list = []
    # for i in ob:
    #     row = {"name": i.pname, "price": str(i.price), "photo": i.photo.url, "id": i.id}
    #     list.append(row)
    # d = json.dumps(list)
    # return HttpResponse(d)
    productlist=[]
    ob = shop_req_details.objects.filter(PRODUCT__PRODUCT__CATEGORY__id=cat,PRODUCT__PRODUCT__pname__istartswith=pn,SHOP_MASTER__SHOP=shopid)
    list = []
    for i in ob:
        if i.PRODUCT.PRODUCT.id in productlist:
            pass
        else:
            productlist.append(i.PRODUCT.PRODUCT.id)
            row = {"name": i.PRODUCT.PRODUCT.pname, "price": str(i.PRODUCT.PRODUCT.price),
                   "photo": i.PRODUCT.PRODUCT.photo.url, "id": i.id}
            list.append(row)

    d = json.dumps(list)
    print(list)
    return HttpResponse(d)



def and_vone_productdet(request):
    pid=request.POST["pid"]
    shopid=request.POST["shopid"]
    i=shop_req_details.objects.get(id=pid)

    ob=shop_req_details.objects.filter(SHOP_MASTER__SHOP=shopid,PRODUCT__PRODUCT__id=i.PRODUCT.PRODUCT.id)
    sizelis=[]
    size=""
    for k in ob:
        if k.PRODUCT.size in sizelis:
            pass
        else:
            sizelis.append(k.PRODUCT.size)
            size=size+k.PRODUCT.size+" "


    # data = {"task": "valid","image":ob.photo.url,"name":ob.pname,"price":ob.price
    #     ,"desc":ob.description,"cat":ob.CATEGORY.category,"size":ob.size}
    row = {"task": "valid","name": i.PRODUCT.PRODUCT.pname, "price": str(i.PRODUCT.PRODUCT.price),
           "image": i.PRODUCT.PRODUCT.photo.url,"size":size,
           "desc": i.PRODUCT.PRODUCT.description, "cat": i.PRODUCT.PRODUCT.CATEGORY.category,
           "id": i.PRODUCT.PRODUCT.id}
    r = json.dumps(row)
    print("=",pid)
    print("=",row)
    return HttpResponse(r)


def add_to_cart(request):
    print(request.POST,"=================================")
    shop_req_id = request.POST['srid']
    qty = request.POST['quantity']
    lid = request.POST['lid']
    size = request.POST['size']

    print(shop_req_id, "PPPPPPPPPPPPPPPPPPPPPPP")
    print(qty, "qqqqqqqqqqqqqqqqqqqqqqq")
    print(lid, "lllllllllllllllllllllllll")

    ob = shop_req_details.objects.get(id=shop_req_id)
    tt = int(ob.PRODUCT.PRODUCT.price) * int(qty)
    print(tt,"price=====================tt========",ob.PRODUCT.PRODUCT.price,qty)
    productid=ob.PRODUCT.PRODUCT.id
    shopid=ob.SHOP_MASTER.SHOP.id
    ob1 = shop_product.objects.filter(SHOP__id=shopid,DISTRIBUTOR_PRODUCT__DISTRIBUTOR_REQUEST__PRODUCT__PRODUCT__id=productid,status='Available')


    st=shop_req_details.objects.filter(SHOP_MASTER__SHOP__id=shopid,PRODUCT__PRODUCT__id=productid,PRODUCT__size=size)
    if len(ob1)>int(qty):
        # for h in st:
        #     if h.PRODUCT.stock>int(qty):
                stock =len(ob1)
                print(stock, "SSSSSSSSSSSSSSSSSSSSSSSSS")
                nstk = int(stock) - int(qty)
                print(nstk, "OOOOOOOOOOOOOOOOOOOO")
                # if int(stock) >= int(qty):
                up = shop_req_details.objects.get(id=shop_req_id)
                up.stock = nstk
                up.save()


                q = order.objects.filter(USER__LOGIN__id=lid, status='cart')
                if len(q) == 0:
                    obe = order()
                    obe.amount = tt
                    obe.gst=int(tt)+int(tt)*0.08
                    obe.status = 'cart'
                    obe.date = datetime.now().strftime("%Y-%m-%d")
                    obe.USER = user_table.objects.get(LOGIN__id=lid)
                    obe.save()
                    obe1 = order_details()
                    obe1.quantity = qty
                    obe1.ORDER = obe
                    obe1.size = size
                    obe1.PRODUCT = up
                    obe1.save()
                    data = {"task": "valid"}
                    r = json.dumps(data)
                    print(r)
                    return HttpResponse(r)
                else:

                    total=int(q[0].amount)+int(tt)
                    print(total, "KKKKKKKKKKKKKKKK")

                    obr = order.objects.get(id=q[0].id)
                    obr. amount= total
                    obr.gst=int(total)+int(total)*0.08
                    obr.status = 'cart'
                    obr.save()
                    obr1 = order_details()
                    obr1.quantity = qty
                    obr1.ORDER = obr
                    obr1.PRODUCT = up
                    obr1.size=size
                    obr1.status='cart'
                    # obf = Offer.objects.filter(PRODUCT__id=up.id, fromdate__lte=datetime.datetime.today(),
                    #                            todate__gte=datetime.datetime.today())
                    # print(obf,"+++++++++++=============")
                    # if len(obf) > 0:
                    #     obr1.OFFER = obf[0].offer
                    #     tt = tt - (tt * float(obf[0].offer) / 100)
                    #     total = int(obr.total) + int(tt)
                    #     obr.total = total
                    #
                    #     obr.save()
                    # else:
                    #     obr1.OFFER = '0'
                    #     total = int(obr.total) + int(tt)
                    #     print(total,"===========+++++++++++")
                    #     obr.total = total
                    #
                    #     obr.save()
                    obr1.save()
                    data = {"task": "valid","tt":str(tt)}

                    r = json.dumps(data)
                    print(r)
                    return HttpResponse(r)


    else:

        data = {"task": "Invalid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)





def user_view_cart(request):
    lid=request.POST["lid"]
    ob=order_details.objects.filter(ORDER__USER__LOGIN__id=lid,ORDER__status="cart")
    list = []
    amount=0
    gst=0
    for i in ob:
        ob1 = order.objects.filter(id=i.ORDER.id)
        amount=amount+((i.PRODUCT.PRODUCT.PRODUCT.price)*i.quantity)
        gst=amount+amount*0.08
        row={"odid":i.id,"pname":i.PRODUCT.PRODUCT.PRODUCT.pname,"price":(i.PRODUCT.PRODUCT.PRODUCT.price)*i.quantity,"image":i.PRODUCT.PRODUCT.PRODUCT.photo.url,"size":i.PRODUCT.PRODUCT.size,"quantity":i.quantity,"lid":i.id,'amt':ob1[0].amount,'gst':str(ob1[0].gst).split('.')[0],'oid':ob1[0].id}
        list.append(row)
    data={"amt":amount,"data":list,"gst":str(gst).split('.')[0]}
    print(data)
    return JsonResponse(data,safe=False)

def cancel_s_order(request):
    print(request.POST, "uuuuuuuuuuuuuuuu")
    qty = request.POST['qty']
    oid = request.POST['oid']
    obd = order_details.objects.get(id=oid)
    h=int(obd.PRODUCT.PRODUCT.PRODUCT.price)*int(qty)
    print(h,"hhhhhhhhhhhhhhhh")
    obp = product.objects.get(id=obd.PRODUCT.PRODUCT.PRODUCT.id)
    obp.stock = float(obp.stock) + int(qty)
    obp.save()
    on = order.objects.get(id=obd.ORDER.id)
    k=int(on.amount)-int(h)
    on.amount=k
    on.save()
    id = obd.ORDER.id
    obd.delete()
    ob2 = order_details.objects.filter(ORDER__id=id)
    if len(ob2) == 0:
        ob1 = order.objects.get(id=id)
        ob1.delete()
    data = {"task": "valid"}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)



def payment(request):
    oid=request.POST['bid']
    oborder=order.objects.get(id=oid)
    oborder.status="Paid"
    oborder.save()

    qt2 = order_details.objects.filter(ORDER__id=oid)
    for i in qt2:
        qq = shop_product.objects.filter(SHOP__id=i.PRODUCT.SHOP_MASTER.SHOP.id,
                                         DISTRIBUTOR_PRODUCT__DISTRIBUTOR_REQUEST__PRODUCT__PRODUCT__id=i.PRODUCT.PRODUCT.PRODUCT.id,
                                         status='Available')
        for j in range(i.quantity):
            obs = shop_product.objects.get(id=qq[j].id)
            obs.status='na';
            obs.save()

            with open(r'D:\blockchain\node_modules\.bin\build\contracts\Structreq.json') as file:
                contract_json = json.load(file)  # load contract info as JSON
                contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
            contract = web3.eth.contract(address='0x8cc77dee291a9D4D31440Da7e5C99bd2b4048f1a', abi=contract_abi)
            blocknumber = web3.eth.get_block_number()
            message2 = contract.functions.addreq(blocknumber + 1, str(qq[0].SHOP.LOGIN.id), str(oborder.USER.name),
                                                 str(obs.DISTRIBUTOR_PRODUCT.id), str(1),
                                                 str(datetime.today()), str('shop bill')
                                                 ).transact({'from': web3.eth.accounts[0]})

    data = {"task": "valid"}
    d = json.dumps(data)
    print(list)
    return HttpResponse(d)


def ordrprdctcodeand(request):
    print(request.POST,"hhhhhhhhhhhh")
    qty=request.POST['quantity']
    pid=request.POST['srid']
    size=request.POST['size']
    lid=request.POST['lid']

    qq=shop_req_details.objects.get(id=pid)
    prid=qq.PRODUCT.PRODUCT.id
    tt = int(qq.PRODUCT.PRODUCT.price)* int(qty)

    ob1 = shop_product.objects.filter(SHOP__id=qq.SHOP_MASTER.SHOP.id,DISTRIBUTOR_PRODUCT__DISTRIBUTOR_REQUEST__PRODUCT__PRODUCT__id=prid,status='Available')

    stock = len(ob1)
    print(stock,qty,"jjjjjjjjjjjjjjjjjjjjjj")


    nstk = int(stock) - int(qty)
    if stock >= int(qty):
        up=shop_req_details.objects.get(id=pid)
        up.quantity=nstk
        up.save()
        q=order.objects.filter(USER=user_table.objects.get(LOGIN__id=lid),status='pending')
        if len(q)==0:
            qt=order()
            qt.date=datetime.today()

            qt.USER=user_table.objects.get(LOGIN=lid)
            qt.status='order'
            qt.amount=tt

            qt.gst =int(tt)+int(tt)*0.08
            qt.save()
            qty1=order_details()
            qty1.quantity=qty
            qty1.PRODUCT=shop_req_details.objects.get(id=pid)
            qty1.ORDER=qt
            qty1.size=size
            qty1.date = datetime.today()
            qty1.save()
            data = {"task": "valid","gst":str(qt.gst).split('.')[0],"amt":tt,'oid':qt.id}
            r = json.dumps(data)
            print(r)
            return HttpResponse(r)
        else:
            total = int(q[0].amount) + int(tt)
            qt=order.objects.get(id=q[0].id)
            qt.amount=total
            qt.gst=0
            qt.save()
            qty1=order_details.objects.filter(PRODUCT__id=pid,ORDER__id=q[0].id)
            if len(qty1)==0:
                qqt=order_details()
                qqt.ORDER=q[0]
                qqt.PRODUCT=shop_req_details.objects.get(id=pid)
                qqt.quantity=qty
                qqt.save()
            else:
                qry1=order_details.objects.get(id=qty1[0].id)
                quty=int(qty1[0].quantity) + int(qty)
                qry1.quantity=quty
                qry1.save()
                data = {"task": "valid","amt":qry1.ORDER.amount,'oid':qry1.ORDER.id}
                r = json.dumps(data)
                print(r)
                return HttpResponse(r)
    else:
        data = {"task": "out"}
        r = json.dumps(data)
        print(r)

        return HttpResponse(r)


def and_vpurchase_history(request):
    lid=request.POST["lid"]
    ob=order_details.objects.filter(ORDER__USER__LOGIN_id=lid).order_by('-id')

    list=[]
    for i in ob:
        obb=return_table.objects.filter(ORDER__id=i.id,status='Accepted')
        if len(obb) == 0:
            row = {"pname": i.PRODUCT.PRODUCT.PRODUCT.pname, "price": i.PRODUCT.PRODUCT.PRODUCT.price,
                   "photo": str(i.PRODUCT.PRODUCT.PRODUCT.photo.url), "quantity": i.quantity, "size": i.size,
                   "status": i.ORDER.status, "date": str(i.ORDER.date), "id": i.id,"res":"No"}

        else:
            row = {"pname": i.PRODUCT.PRODUCT.PRODUCT.pname, "price": i.PRODUCT.PRODUCT.PRODUCT.price,
                   "photo": str(i.PRODUCT.PRODUCT.PRODUCT.photo.url), "quantity": i.quantity, "size": i.size,
                   "status": i.ORDER.status, "date": str(i.ORDER.date), "id": i.id,"res":"yes"}

        #     list.append(row)
        list.append(row)
    d=json.dumps(list)

    print(list)
    return HttpResponse(d)


def and_return_product(request):
    rs = request.POST['Reason']
    oitem = request.POST['oid']
    print("^^^^^^^^^^^^^^^", request.POST)
    ob = return_table()
    ob.ORDER = order_details.objects.get(id=oitem)
    ob.date = datetime.today()
    ob.status='pending'
    ob.reason = rs
    ob.save()

    data = {"task": "valid"}
    r = json.dumps(data)
    return HttpResponse(r)


def and_vreturn_info(request):
    o_id=request.POST["o_id"]

    ob=order_details.objects.filter(id=o_id)

    list=[]
    for i in ob:
        row={"pname":i.PRODUCT.PRODUCT.PRODUCT.pname,"price":i.PRODUCT.PRODUCT.PRODUCT.price,"photo":str(i.PRODUCT.PRODUCT.PRODUCT.photo.url)[1:],"quantity":i.quantity,"size":i.size,"status":i.ORDER.status,"date":str(i.ORDER.date),"id":i.id}

        list.append(row)
    d=json.dumps(list)
    print(list)
    return HttpResponse(d)




def andviewproducts(request):
    print(request.POST)
    b = request.POST['srno']
    # b = request.POST['srid']

    # db = Db()
    r = {}
    # qry = "SELECT * FROM `medicine` WHERE id='"+str(b)+"'"
    # res = db.selectOne(qry)
    data = []
    # try:
    if True:
        with open(compiled_contract_path) as file:
            contract_json = json.load(file)  # load contract info as JSON
            contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
        contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
        blocknumber = web3.eth.get_block_number()
        print(blocknumber)
        sollist=[]
        ulist=[]
        for i in range(blocknumber,2, -1):
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])

            # decoded_input[1]['fid']
            print(decoded_input,"=======")
            if int(decoded_input[1]['mid']) == int(b):

                print(decoded_input,"**************************")
                if decoded_input[1]['status']=='distributor request' or decoded_input[1]['status']=='shop request'\
                        or decoded_input[1]['status']=='shop bill':
                    print("ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
                    print(decoded_input[1])
                    # mid = decoded_input[1]['mid'].split('#')
                    sollist.append(decoded_input[1]['status'])
                    ulist.append([decoded_input[1]['fid'],decoded_input[1]['tid'],decoded_input[1]['date']])
                    # ob=medicine_table.objects.get(id=b)
                    # r['med'] = str(ob.name)
                    # r['mf'] = str(ob.mnf_date)
                    # r['exp'] = ob.exp_date
                    # r['qty'] = ob.stock
                    # r['price'] = ob.price
                    # # r['info'] = decoded_input[1]['fid']+"------------>"+decoded_input[1]['tid']
                    # r['status'] = "ok"
                    # sollist.append(r)
                    # return JsonResponse(r,safe=False)
            # else:
            #         r['status'] = "none"
            #         r['med'] = 0
            #         r['mf'] = 0
            #         r['exp'] = 0
            #         r['qty'] = 0
            #         r['price'] = 0
                    # r['info'] = decoded_input[1]['fid']+"------------>"+decoded_input[1]['tid']
            #         sollist.append(r)
                    # return JsonResponse(r,safe=False)
        print(")))))))))))))))))))))))))000")
        print(")))))))))))))))))))))))))000")
        print(")))))))))))))))))))))))))000")
        print(")))))))))))))))))))))))))000")
        print(")))))))))))))))))))))))))000")
        print(")))))))))))))))))))))))))000")
        print(")))))))))))))))))))))))))000")
        print(")))))))))))))))))))))))))000")
        print(sollist)
        print(ulist)
        print(r, "+===================")

        if len(sollist)==3:
            print("Original","==============")
            obp=shop_table.objects.get(LOGIN__id=ulist[0][0])

            shopdata=obp.name+" sell to "+ulist[0][1]+" on "+ulist[0][2].split(".")[0]

            obd = distributor_table.objects.get(LOGIN__id=ulist[1][0])

            distributor=obd.name+" sell to "+obp.name+" on "+ulist[1][2].split(".")[0]

            print(ulist[0][0],"==================")
            print(ulist[0][0],"==================")
            print(ulist[0][0],"==================")
            print(ulist[0][0],"==================")
            print(ulist[0][0],"==================")
            print(ulist[0][0],"==================")
            print(ulist[0][0],"==================)))))))))))))))))")
            obm=manufacturer_table.objects.get(LOGIN__id=ulist[2][0])
            manufracture=obm.name+" sell to "+obd.name+" on "+ulist[2][2].split(".")[0]
            r={}
            obb=distributor_product.objects.get(id=b)
            ob = obb.DISTRIBUTOR_REQUEST.PRODUCT.PRODUCT
            # b = obb.PRODUCT
            r['med'] = str(ob.pname)
            r['mf'] = str(obb.DISTRIBUTOR_REQUEST.PRODUCT.date)

            r['size'] = obb.DISTRIBUTOR_REQUEST.PRODUCT.size
            r['price'] = ob.price
            r['img'] = ob.photo.url

            r['task'] = "product"
            r['manu'] = manufracture
            r['dis'] = distributor
            r['pha'] = shopdata
            print(manufracture)
            print(distributor)
            print(shopdata)
            print(r,"==================")
            return JsonResponse(r, safe=False)
        print("++++++++++++++++++++++++++++++++++++++++++++")
        return JsonResponse({"task":"fake"}, safe=False)
    # except Exception as e:
    #     print(e)
    #     pass
    # return JsonResponse({"task": "fake"}, safe=False)

























