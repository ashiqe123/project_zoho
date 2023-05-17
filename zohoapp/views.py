from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils.text import capfirst
from django.contrib.auth.models import User,auth
from .models import * 
from .models import  customer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db.models import Q

from django.http import JsonResponse


def index(request):

    return render(request,'index.html')

def register(request):
   
    if request.method=='POST':

        first_name=capfirst(request.POST['fname'])
        last_name=capfirst(request.POST['lname'])
        username=request.POST['uname']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email1']
        phone = request.POST['phone']

      
        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                return redirect('register')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                
                user.save()
                u = User.objects.get(id = user.id)

                company_details(contact_number = phone, user = u).save()
    
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('register')   
        return redirect('register')

    return render(request,'register.html')

def login(request):
        
    if request.method == 'POST':
        
        email_or_username = request.POST['emailorusername']
        password = request.POST['password']

        user = authenticate(request, username=email_or_username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('base')
        else:
            return redirect('/')

    return render(request, 'register.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='login')
def base(request):
   
    if request.method=='POST':
       
        if not Unit.objects.filter(unit='BOX').exists():
            Unit(unit='BOX').save()
        if not Unit.objects.filter(unit='UNIT').exists():
            Unit(unit='UNIT').save()
        if not Unit.objects.filter(unit='LITRE').exists():
            Unit(unit='LITRE').save()

        if not Sales.objects.filter(Account_name='General Income').exists():
            Sales(Account_type='INCOME',Account_name='General Income',Account_desc='salesincome').save()
        if not Sales.objects.filter(Account_name='Intrest Income').exists():
            Sales(Account_type='INCOME',Account_name='Intrest Income',Account_desc='salesincome').save()
        if not Sales.objects.filter(Account_name='Late fee Income').exists():
            Sales(Account_type='INCOME',Account_name='Late fee Income',Account_desc='salesincome').save()
        if not Sales.objects.filter(Account_name='Discount Income').exists():
            Sales(Account_type='INCOME',Account_name='Discount Income',Account_desc='salesincome').save()
        if not Sales.objects.filter(Account_name='Other Charges').exists():
            Sales(Account_type='INCOME',Account_name='Other Charges',Account_desc='salesincome').save()
        if not Sales.objects.filter(Account_name='Shipping Charge').exists():
            Sales(Account_type='INCOME',Account_name='Shipping Charge',Account_desc='salesincome').save()


        if not  Purchase.objects.filter(Account_name='Advertising & Marketing').exists():
            Purchase(Account_type='EXPENCES',Account_name='Advertising & Markting',Account_desc='Advertsing Exp').save()
        if not Purchase.objects.filter(Account_name='Debit Charge').exists():
            Purchase(Account_type='EXPENCES',Account_name='Debit Charge',Account_desc='Debited Exp').save()
        if not Purchase.objects.filter(Account_name='Labour Charge').exists():
            Purchase(Account_type='EXPENCES',Account_name='Labour Charge',Account_desc='Labour Exp').save()
        if not Purchase.objects.filter(Account_name='Raw Meterials').exists():
            Purchase(Account_type='EXPENCES',Account_name='Raw Meterials',Account_desc='Raw Meterials Exp').save()

    company = company_details.objects.get(user = request.user)
    context = {
                'company' : company
            }
    return render(request,'loginhome.html',context)

@login_required(login_url='login')
def view_profile(request):

    company = company_details.objects.get(user = request.user)
    context = {
                'company' : company
            }
    return render(request,'profile.html',context)

@login_required(login_url='login')
def edit_profile(request,pk):

    company = company_details.objects.get(id = pk)
    user1 = User.objects.get(id = company.user_id)

    if request.method == "POST":

        user1.first_name = capfirst(request.POST.get('f_name'))
        user1.last_name  = capfirst(request.POST.get('l_name'))
        user1.username = request.POST.get('uname')
        # pat.age = request.POST.get('age')
        # pat.address = capfirst(request.POST.get('address'))
        # pat.gender = request.POST.get('gender')
        # user1.email = request.POST.get('email')
        # pat.email = request.POST.get('email')
        # pat.contact_num = request.POST.get('cnum')
        # #fkey1= request.POST.get('doc')
        # #pat.doctor = doctor.objects.get(id = fkey1)
        # if len(request.FILES)!=0 :
        #     doc.profile_pic = request.FILES.get('file')


        company.save()
        user1.save()
        return redirect('view_profile')

    context = {
        'company' : company,
        'user1' : user1,
    }
    context = {
                'company' : company,
            }
    return render(request,'edit_profile.html',context)

@login_required(login_url='login')
def itemview(request):
    viewitem=AddItem.objects.all()
    return render(request,'item_view.html',{'view':viewitem})


@login_required(login_url='login')
def additem(request):
    unit=Unit.objects.all()
    sale=Sales.objects.all()
    purchase=Purchase.objects.all()
    
    


  
    
        



    accounts = Purchase.objects.all()
    account_types = set(Purchase.objects.values_list('Account_type', flat=True))

    
    account = Sales.objects.all()
    account_type = set(Sales.objects.values_list('Account_type', flat=True))
    
    

    return render(request,'additem.html',{'unit':unit,'sale':sale,'purchase':purchase,
               
                            "account":account,"account_type":account_type,"accounts":accounts,"account_types":account_types,
                            
                            })

@login_required(login_url='login')
def add_account(request):
    if request.method=='POST':
        Account_type  =request.POST['acc_type']
        Account_name =request.POST['acc_name']
        Acount_code =request.POST['acc_code']
        Account_desc =request.POST['acc_desc']
       
        acc=Purchase(Account_type=Account_type,Account_name=Account_name,Acount_code=Acount_code,Account_desc=Account_desc)
        acc.save()                 
        return redirect("additem")
        
    return render(request,'additem.html')


@login_required(login_url='login')
def add(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            radio=request.POST.get('radio')
            if radio=='tax':
    
                
                inter=request.POST['inter']
                intra=request.POST['intra']
                type=request.POST.get('type')
                name=request.POST['name']
                unit=request.POST['unit']
                sel_price=request.POST.get('sel_price')
                sel_acc=request.POST.get('sel_acc')
                s_desc=request.POST.get('sel_desc')
                cost_price=request.POST.get('cost_price')
                cost_acc=request.POST.get('cost_acc')      
                p_desc=request.POST.get('cost_desc')
                u=request.user.id
                us=request.user
                history="Created by" + str(us)
                user=User.objects.get(id=u)
                unit=Unit.objects.get(id=unit)
                sel=Sales.objects.get(id=sel_acc)
                cost=Purchase.objects.get(id=cost_acc)
                ad_item=AddItem(type=type,Name=name,p_desc=p_desc,s_desc=s_desc,s_price=sel_price,p_price=cost_price,unit=unit,
                            sales=sel,purchase=cost,user=user,creat=history,interstate=inter,intrastate=intra
                                )
                
            else:
                                                  
                type=request.POST.get('type')
                name=request.POST['name']
                unit=request.POST['unit']
                sel_price=request.POST.get('sel_price')
                sel_acc=request.POST.get('sel_acc')
                s_desc=request.POST.get('sel_desc')
                cost_price=request.POST.get('cost_price')
                cost_acc=request.POST.get('cost_acc')      
                p_desc=request.POST.get('cost_desc')
                u=request.user.id
                us=request.user
                history="Created by" + str(us)
                user=User.objects.get(id=u)
                unit=Unit.objects.get(id=unit)
                sel=Sales.objects.get(id=sel_acc)
                cost=Purchase.objects.get(id=cost_acc)
                ad_item=AddItem(type=type,Name=name,p_desc=p_desc,s_desc=s_desc,s_price=sel_price,p_price=cost_price,unit=unit,
                            sales=sel,purchase=cost,user=user,creat=history,interstate='none',intrastate='none'
                                )
                ad_item.save()
            ad_item.save()
           
            return redirect("itemview")
    return render(request,'additem.html')



@login_required(login_url='login')
def edititem(request,id):
    pedit=AddItem.objects.get(id=id)
    p=Purchase.objects.all()
    s=Sales.objects.all()
    u=Unit.objects.all()

    accounts = Purchase.objects.all()
    account_types = set(Purchase.objects.values_list('Account_type', flat=True))
    

    
    account = Sales.objects.all()
    account_type = set(Sales.objects.values_list('Account_type', flat=True))
    
    return render(request,'edititem.html',{"account":account,"account_type":account_type,'e':pedit,'p':p,'s':s,'u':u,"accounts":accounts,"account_types":account_types})


@login_required(login_url='login')
def edit_db(request,id):
        if request.method=='POST':
            edit=AddItem.objects.get(id=id)
            edit.type=request.POST.get('type')
            edit.Name=request.POST['name']
            unit=request.POST['unit']
            edit.s_price=request.POST['sel_price']
            sel_acc=request.POST['sel_acc']
            edit.s_desc=request.POST['sel_desc']
            edit.p_price=request.POST['cost_price']
            cost_acc=request.POST['cost_acc']        
            edit.p_desc=request.POST['cost_desc']
            
            
            edit.unit=Unit.objects.get(id=unit)
            edit.sales=Sales.objects.get(id=sel_acc)
            edit.purchase=Purchase.objects.get(id=cost_acc)
            edit.save()
            return redirect('itemview')

        return render(request,'edititem.html')


@login_required(login_url='login')
def detail(request,id):
    user_id=request.user
    items=AddItem.objects.all()
    product=AddItem.objects.get(id=id)
    history=History.objects.filter(p_id=product.id)
    
    
    context={
       "allproduct":items,
       "product":product,
       "history":history,
      
    }
    
    return render(request,'demo.html',context)


@login_required(login_url='login')
def Action(request,id):
    user=request.user.id
    user=User.objects.get(id=user)
    viewitem=AddItem.objects.all()
    event=AddItem.objects.get(id=id)
    

    print(user)
    if request.method=='POST':
        action=request.POST['action']
        event.satus=action
        event.save()
        if action == 'active':
            History(user=user,message="Item marked as Active ",p=event).save()
        else:
            History(user=user,message="Item marked as inActive",p=event).save()
    return render(request,'item_view.html',{'view':viewitem})

@login_required(login_url='login')
def cleer(request,id):
    dl=AddItem.objects.get(id=id)
    dl.delete()
    return redirect('itemview')


@login_required(login_url='login')
def add_unit(request):
    if request.method=='POST':
        unit_name=request.POST['unit_name']
        Unit(unit=unit_name).save()
        return redirect('additem')
    return render(request,"additem.html")


@login_required(login_url='login')
def add_sales(request):
    if request.method=='POST':
        Account_type  =request.POST['acc_type']
        Account_name =request.POST['acc_name']
        Acount_code =request.POST['acc_code']
        Account_desc =request.POST['acc_desc']        
        acc=Sales(Account_type=Account_type,Account_name=Account_name,Acount_code=Acount_code,Account_desc=Account_desc)
        acc.save()
        return redirect('additem')
    return render(request,'additem.html')



# ====================second potion===================================

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from django.core.mail import EmailMessage

from django.conf import settings
from .forms import EmailForm


@login_required(login_url='login')

def payment_term(request):
    if request.method=='POST':
        term=request.POST.getlist('terms[]')
        day=request.POST.getlist('days[]')
        if len(term)==len(day):
            mapped = zip(term,day)
            mapped = list(mapped)
            for ele in mapped:
                created = payment_terms.objects.get_or_create(Terms=ele[0],Days=ele[1])
            return redirect('add_prod')
    return redirect("add_customer")

@login_required(login_url='login')

def invoiceview(request):
    invoicev=invoice.objects.all()
    
    if not payment_terms.objects.filter(Terms='net 15').exists(): 
       payment_terms(Terms='net 15',Days=15).save()
    if not payment_terms.objects.filter(Terms='due end of month').exists():
        payment_terms(Terms='due end of month',Days=60).save()
    elif not  payment_terms.objects.filter(Terms='net 30').exists():
        payment_terms(Terms='net 30',Days=30).save() 
    
    
    context={
        'invoice':invoicev,
        
    }
    return render(request,'invoiceview.html',context)

@login_required(login_url='login')

def detailedview(request,id):
    inv_dat=invoice.objects.all()
    inv_master=invoice.objects.get(id=id)
    invoiceitem=invoice_item.objects.filter(inv_id=id)
    company=company_details.objects.get(user_id=request.user.id)
    
    
    context={
        'inv_dat':inv_dat,
        'invoiceitem':invoiceitem,
        'comp':company,
        'invoice':inv_master,
        
                    }
    return render(request,'invoice_det.html',context)



@login_required(login_url='login')

def dele(request,pk):
    d=invoice.objects.get(id=pk)
    d.delete()
    return redirect('invoiceview')



@login_required(login_url='login')

def add_prod(request):
    sb=payment_terms.objects.all()
    c=customer.objects.all()
    p=AddItem.objects.all()
    i=invoice.objects.all()
    pay=payment_terms.objects.all()
    if not payment_terms.objects.filter(Terms='net 15').exists(): 
       payment_terms(Terms='net 15',Days=15).save()
    if not payment_terms.objects.filter(Terms='due end of month').exists():
        payment_terms(Terms='due end of month',Days=60).save()
    elif not  payment_terms.objects.filter(Terms='net 30').exists():
        payment_terms(Terms='net 30',Days=30).save() 
    
    
   
    if request.user.is_authenticated:
        if request.method=='POST':
            c=request.POST['cx_name']
            cus=customer.objects.get(customerName=c) 
            print(cus.id)  
            custo=cus.id
            invoice_no=request.POST['inv_no']
            terms=request.POST['term']
            term=payment_terms.objects.get(id=terms)
            order_no=request.POST['ord_no']
            inv_date=request.POST['inv_date']
            due_date=request.POST['due_date']
        
            
            cxnote=request.POST['customer_note']
            subtotal=request.POST['subtotal']
            igst=request.POST['igst']
            cgst=request.POST['cgst']
            sgst=request.POST['sgst']
            totaltax=request.POST['totaltax']
            t_total=request.POST['t_total']
            if request.FILES.get('file') is not None:
                file=request.FILES['file']
            else:
                file="/static/images/alt.jpg"
            tc=request.POST['ter_cond']

            status=request.POST['sd']
            if status=='draft':
                print(status)   
            else:
                print(status)  
        
            product=request.POST.getlist('item[]')
            hsn=request.POST.getlist('hsn[]')
            quantity=request.POST.getlist('quantity[]')
            rate=request.POST.getlist('rate[]')
            desc=request.POST.getlist('desc[]')
            tax=request.POST.getlist('tax[]')
            total=request.POST.getlist('amount[]')
            term=payment_terms.objects.get(id=term.id)

            inv=invoice(customer_id=custo,invoice_no=invoice_no,terms=term,order_no=order_no,inv_date=inv_date,due_date=due_date,
                        cxnote=cxnote,subtotal=subtotal,igst=igst,cgst=cgst,sgst=sgst,t_tax=totaltax,
                        grandtotal=t_total,status=status,terms_condition=tc,file=file)
            inv.save()
            inv_id=invoice.objects.get(id=inv.id)
            if len(product)==len(hsn)==len(quantity)==len(desc)==len(tax)==len(total)==len(rate):

                mapped = zip(product,hsn,quantity,desc,tax,total,rate)
                mapped = list(mapped)
                for element in mapped:
                    created = invoice_item.objects.get_or_create(inv=inv_id,product=element[0],hsn=element[1],
                                        quantity=element[2],desc=element[3],tax=element[4],total=element[5],rate=element[6])
                    
                return redirect('invoiceview')
    context={
            'c':c,
            'p':p,
            'i':i,
            'pay':pay,
            'sb':sb,
    }       
    return render(request,'createinvoice.html',context)


@login_required(login_url='login')

def add_payment(request):
    if request.method=='POST':
            terms=request.POST.get()
    return redirect('add_prod')


@login_required(login_url='login')

def add_cx(request):
    if request.user.is_authenticated:
        if request.method=='POST':
                user=request.user.id
                user=User.objects.get(id=user)
                print(user)
                name=request.POST.get('name')
                email=request.POST.get('email')
                pos=request.POST.get('position')
                state=request.POST.get('state')
                com_name=request.POST.get('company')
                customer(customerName=name,customerEmail=email,placeofsupply=pos,state=state,companyName=com_name,user_id=user.id).save()
        return redirect('add_prod')



@login_required(login_url='login')

def edited_prod(request,id):
    print(id)
    c = customer.objects.all()
    p = AddItem.objects.all()
    invoiceitem = invoice_item.objects.filter(inv_id=id)
    invoic = invoice.objects.get(id=id)
    pay=payment_terms.objects.all()
  
    if request.method == 'POST':
        u=request.user.id
        c=request.POST['cx_name']
        
        cust=customer.objects.get(customerName=c) 
        invoic.customer=cust
        term=request.POST['term']
        
        
        invoic.terms = payment_terms.objects.get(id=term)
        invoic.inv_date = request.POST['inv_date']
        invoic.due_date = request.POST['due_date']
        invoic.cxnote = request.POST['customer_note']
        invoic.subtotal = request.POST['subtotal']
        invoic.igst = request.POST['igst']
        invoic.cgst = request.POST['cgst']
        invoic.sgst = request.POST['sgst']
        invoic.t_tax = request.POST['totaltax']
        invoic.grandtotal = request.POST['t_total']

        if request.FILES.get('file') is not None:
            invoic.file = request.FILES['file']
        else:
            invoic.file = "/static/images/alt.jpg"

            invoic.terms_condition = request.POST.get('ter_cond')
        
        status=request.POST['sd']
        if status=='draft':
            invoic.status=status      
        else:
            invoic.status=status   
         
        invoic.save()
        
        print("/////////////////////////////////////////////////////////")
        product=request.POST.getlist('item[]')
        hsn=request.POST.getlist('hsn[]')
        quantity=request.POST.getlist('quantity[]')
        rate=request.POST.getlist('rate[]')
        desc=request.POST.getlist('desc[]')
        tax=request.POST.getlist('tax[]')
        total=request.POST.getlist('amount[]')
        obj_dele=invoice_item.objects.filter(inv_id=invoic.id)
        obj_dele.delete()
       
        if len(product)==len(hsn)==len(quantity)==len(desc)==len(tax)==len(total)==len(rate):

            mapped = zip(product,hsn,quantity,desc,tax,total,rate)
            mapped = list(mapped)
            for element in mapped:
                created = invoice_item.objects.get_or_create(inv=invoic,product=element[0],hsn=element[1],
                                    quantity=element[2],desc=element[3],tax=element[4],total=element[5],rate=element[6])
                
            return redirect('detailedview',id)
                    
    context = {
            'c': c,
            'p': p,
            'inv': invoiceitem,
            'i': invoic,
            'pay':pay,
        }             
        
    return render(request, 'invoiceedit.html', context)




@login_required(login_url='login')

def edited(request,id):
    c=customer.objects.all()
    p=AddItem.objects.all()
    invoiceitem=invoice_item.objects.filter(inv_id=id)
    inv=invoice.objects.get(id=id)
    context={
        'c':c,
        'p':p,
        'inv':invoiceitem,
        'inv':inv,
        
    }
    
    return render(request,'editinvoice.html')



@login_required(login_url='login')

def itemdata(request):
    cur_user = request.user.id
    user = User.objects.get(id=cur_user)
    company = company_details.objects.get(user = user)
    # print(company.state)
    id = request.GET.get('id')
    cust = request.GET.get('cust')
    
        
    item = AddItem.objects.get(Name=id)
    cus=customer.objects.get(customerName=cust)
    rate = item.s_price
    place=company.state
    gst = item.intrastate
    igst = item.interstate
    desc=item.s_desc
    print(place)
    mail=cus.customerEmail
    
    place_of_supply = customer.objects.get(customerName=cust).placeofsupply
    print(place_of_supply)
    return JsonResponse({"status":" not",'mail':mail,'desc':desc,'place':place,'rate':rate,'pos':place_of_supply,'gst':gst,'igst':igst})
    return redirect('/')



def allestimates(request):
    pass


def newestimate(request):
    pass


from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def customerdata(request):
    customer_id = request.GET.get('id')
    print(customer_id)
    cust = customer.objects.get(customerName=customer_id)
    data7 = {'email': cust.customerEmail}
    
    print(data7)
    return JsonResponse(data7)





class EmailAttachementView(View):
    form_class = EmailForm
    template_name = 'newmail.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'email_form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            files = request.FILES.getlist('attach')

            try:
                mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
                for f in files:
                    mail.attach(f.name, f.read(), f.content_type)
                mail.send()
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Sent email to %s'%email})
            except:
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Either the attachment is too big or corrupt'})

        return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})


# for getting customer detail when select a customer


# def get_customer_details(request):
#     if request.method == "GET":
#         customer_id = request.GET.get("customer_id")
#         try:
#             customer = cx.objects.get(id=customer_id)
#             return JsonResponse({
#               "cx": customer.cx,
#               "cx_mail": customer.cx_mail,
              
#             })
#         except cx.DoesNotExist:
#             return JsonResponse({
#               "cx": "",
#               "cx_mail": "",
             
#             })
#     else:
#         return JsonResponse({
#           "cx": "",
#           "cx_mail": "",
          
#         })


# # for getting product detail when select a product
# def get_product_details(request):
#     if request.method == "GET":
#         product_id = request.GET.get("product_id")
#         try:
#             product = AddItem.objects.get(id=product_id)
#             return JsonResponse({
#               "name": product.Name,
#               "sel_price": product.s_price,
#               "s_desc": product.s_desc
#             })
#         except AddItem.DoesNotExist:
#             return JsonResponse({
#               "name": "",
#               "sel_price": "",
#               "s_desc": ""
#             })
#     else:
#         return JsonResponse({
#           "name": "",
#           "sel_price": "",
#           "s_desc": ""
#         })
def add_customer_for_estimate(request):
   
    return render(request,'createinvoice.html',{'sb':sb})

def add_customer_for_invoice(request):
    pt=payment_terms.objects.all()
    if request.user.is_authenticated:
        if request.method=='POST':
            type=request.POST.get('type')
            txtFullName=request.POST['txtFullName']
            cpname=request.POST['cpname']
           
            email=request.POST.get('myEmail')
            wphone=request.POST.get('wphone')
            mobile=request.POST.get('mobile')
            skname=request.POST.get('skname')
            desg=request.POST.get('desg')      
            dept=request.POST.get('dept')
            wbsite=request.POST.get('wbsite')

            gstt=request.POST.get('gstt')
            posply=request.POST.get('posply')
            tax1=request.POST.get('tax1')
            crncy=request.POST.get('crncy')
            obal=request.POST.get('obal')

            select=request.POST.get('pterms')
            pterms=payment_terms.objects.get(id=select)
            pterms=request.POST.get('pterms')

            plst=request.POST.get('plst')
            plang=request.POST.get('plang')
            fbk=request.POST.get('fbk')
            twtr=request.POST.get('twtr')
        
            atn=request.POST.get('atn')
            ctry=request.POST.get('ctry')
            
            addrs=request.POST.get('addrs')
            addrs1=request.POST.get('addrs1')
            bct=request.POST.get('bct')
            bst=request.POST.get('bst')
            bzip=request.POST.get('bzip')
            bpon=request.POST.get('bpon')
            bfx=request.POST.get('bfx')

            sal=request.POST.get('sal')
            ftname=request.POST.get('ftname')
            ltname=request.POST.get('ltname')
            mail=request.POST.get('mail')
            bworkpn=request.POST.get('bworkpn')
            bmobile=request.POST.get('bmobile')

            bskype=request.POST.get('bskype')
            bdesg=request.POST.get('bdesg')
            bdept=request.POST.get('bdept')
            u = User.objects.get(id = request.user.id)

          
            ctmr=customer(customerName=txtFullName,customerType=type,
                        companyName=cpname,customerEmail=email,customerWorkPhone=wphone,
                         customerMobile=mobile,skype=skname,designation=desg,department=dept,
                           website=wbsite,GSTTreatment=gstt,placeofsupply=posply, Taxpreference=tax1,
                             currency=crncy,OpeningBalance=obal,PaymentTerms=pterms,
                                PriceList=plst,PortalLanguage=plang,Facebook=fbk,Twitter=twtr,
                                 Attention=atn,country=ctry,Address1=addrs,Address2=addrs1,
                                  city=bct,state=bst,zipcode=bzip,phone1=bpon,
                                   fax=bfx,CPsalutation=sal,Firstname=ftname,
                                    Lastname=ltname,CPemail=mail,CPphone=bworkpn,
                                    CPmobile= bmobile,CPskype=bskype,CPdesignation=bdesg,
                                     CPdepartment=bdept,user=u )
            ctmr.save()  
            
            return redirect("add_prod")
        return render(request,"createinvoice.html",)
    
def payment_term_for_invoice(request):
    if request.method=='POST':
        term=request.POST.get('term')
        day=request.POST.get('day')
        ptr=payment_terms(Terms=term,Days=day)
        ptr.save()
        return redirect("add_prod")