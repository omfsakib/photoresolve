from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseBadRequest
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def getServices(request, *args, **kwargs):
    base_url = "http://127.0.0.1:8000/static"
    import_services = Services.objects.all().order_by('date_created')
    card = {}
    num = 1
    for i in import_services:
        count = 0
        import_sub_services = SubServices.objects.filter(service=i)
        featureListLeft = []
        featureListRight = []
        for j in import_sub_services:
            count += 1
            name = j.name
            if count <= 4:
                featureListLeft.append(name)
            else:
                featureListRight.append(name)

        if num % 2 == 0:
            viewType = "right"
        else:
            viewType = "left"

        item = {
            'title': i.name,
            'button_name':i.button_name,
            'content': i.description,
            'start': f'Start From ₤{i.rate} / Per Photo',
            'link': 'contact',
            'cover': {
                'image': base_url + i.after.url,
            },
            'featureList': {
                'Left': featureListLeft,
                'Right': featureListRight,
            },
            'viewType': viewType,
        }
        card[f'item{num}'] = item
        num += 1

    return JsonResponse(card,safe=False)

from django.http import HttpResponse

def get_logo(request):
    logo = Logo.objects.first() # get the first logo in the database
    if logo:
        return HttpResponse(logo.svg_code, content_type='image/svg+xml')
    else:
        return HttpResponse(status=404)
    
def get_navigation(request):
    navigation_items = Navigation.objects.all().values()
    return JsonResponse(list(navigation_items), safe=False)

def get_slide_text(request):
    slides = Slide.objects.all()
    data = [{'text': slide.text, 'class': slide.class_name} for slide in slides]
    return JsonResponse(data, safe=False)

def get_slide_info(request):
    base_url = "http://127.0.0.1:8000/static"
    slide = SlideInfo.objects.first()
    data = {'caption': slide.caption, 'class': base_url + slide.cover.url }
    return JsonResponse(data, safe=False)

def get_footer_info(request):
    footer = Contact.objects.first()
    data = {
        'description': footer.description,
        'shortIntro': footer.short_info,
        'phone': footer.phone,
        'email': footer.email,
        'address': footer.address
    }
    return JsonResponse(data)

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        object = Portfolio.objects.create(thumb = uploaded_file)

        return HttpResponse('File uploaded successfully!')
    else:
        return HttpResponseBadRequest('Invalid request')

def get_terms(request):
    terms = TermsAndConditions.objects.first()
    
    if terms:
        return HttpResponse(terms.terms)
    else:
        return HttpResponse(status=404)

def getService(request,*arg,**kwargs):
    base_url = "http://127.0.0.1:8000/static"
    name = kwargs.pop('name')
    import_services = Services.objects.get(name = name)
    import_sub_services =SubServices.objects.filter(service = import_services)
    featureList = []
    sub_services1 = []
    sub_services2 = []
    count = 0
    for i in import_sub_services:
        count += 1
        list = {
            'name': i.name,
        }
        featureList.append(list)
        item = {
            'title' : i.name,
            'description' : i.description,
            'price' : "For only ₤"+ str(i.rate) +"/ photo.",
            'before' : base_url + i.before.url,
            'after' : base_url + i.after.url,
        }
        if count <= 4:
            sub_services1.append(item)
        else:
            sub_services2.append(item)

    return JsonResponse({
        "title": import_services.name,
        'content' : import_services.description,
        'after': base_url + import_services.after.url,
        'featureList':featureList,
        'sub_services1':sub_services1,
        'sub_services2':sub_services2,
        })

def getPortfolio(request):
    base_url = "http://127.0.0.1:8000/static"
    import_portfolio = Portfolio.objects.all().order_by('date_created')

    portfolio = []
    for i in import_portfolio:
        item = {
            'id':i.id,
            'size': "1400-800",
            'thumb': base_url + i.thumb.url,
        }
        portfolio.append(item)
    
    return JsonResponse(portfolio,safe=False)

def getContact(request):
    contact =  Contact.objects.all()[:1]
    for i in contact:
        caption = i.caption
        phone = i.phone
        email = i.email
        address = i.address

    return JsonResponse({
        'caption':caption,
        'phone':phone,
        'email':email,
        'address':address
    })

def getPricing(request):
    import_pricing = Pricing.objects.all().order_by('date_created')

    pricing = []

    for i in import_pricing:
        item = {
            'name':i.name,
            'price':i.rate
        }
        pricing.append(item)
    
    return JsonResponse(pricing,safe=False)

@csrf_exempt
def post_query(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        # Create a new ContactQuery object and save it to the database
        query = Queries(name=name, email=email, description=message)
        query.save()

        # Return a success response
        return JsonResponse({'status': 'success'})
    else:
        # Return an error response if the request method is not POST
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    

def home(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('admin:login')
    
    import_services = Services.objects.all().order_by('date_created')
    services = []
    for i in import_services:
        sub_services = []
        import_sub_services = SubServices.objects.filter(service = i)
        for j in import_sub_services:
            sub_item = {
                'id':j.id,
                'name':j.name,
                'description':j.description,
                'rate':j.rate,
                'before':j.before.url,
                'after':j.after.url
            }
            sub_services.append(sub_item)
        item = {
            'id': i.id,
            'name': i.name,
            'description': i.description,
            'rate':i.rate,
            'button_name':i.button_name,
            'after':i.after.url,
            'sub_services': sub_services,
        }
        services.append(item)

    
    if request.method == "POST" and 'sub_services_remove' in request.POST:
        id = request.POST.get('sub_services_remove')
        import_sub_services = SubServices.objects.get(id = id)
        import_sub_services.service = None
        import_sub_services.save()
        return redirect('home')
    
    portfolio = Portfolio.objects.all().order_by('date_created')

    if request.method == "POST" and 'portfolio_image' in request.FILES:
        portfolio_image = request.FILES.get('portfolio_image')
        object = Portfolio.objects.create(thumb = portfolio_image)

        return redirect('home')
    
    if request.method == "POST" and 'portfolio_delete' in request.POST:
        id = request.POST.get('portfolio_delete')
        portfolio = Portfolio.objects.get(id = id)
        portfolio.delete()
        return redirect('home')
    
    pricings = Pricing.objects.all().order_by('date_created')[:3]

    contact_info = Contact.objects.all()[:1]
    contact = {}
    for i in contact_info:
        contact['id'] = i.id
        contact['caption'] = i.caption
        contact['phone'] = i.phone
        contact['email'] = i.email
        contact['address'] = i.address

    if request.method == 'POST' and 'contact_id' in request.POST:
        id = request.POST.get('contact_id')
        cnt = Contact.objects.get(id=id)
        caption = request.POST.get('caption')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        cnt.caption = caption
        cnt.phone = phone
        cnt.email = email
        cnt.address = address
        cnt.save()

        return redirect('home')
    
    queries = Queries.objects.all()
    if request.method == 'POST' and 'query_delete' in request.POST:
        id = request.POST.get('query_delete')
        query = Queries.objects.get(id = id)
        query.delete()
        return redirect('home')
        

    logo = Logo.objects.first()

    if request.method == "POST" and 'logo_code' in request.POST:
        logo_code = request.POST.get('logo_code')
        logo.svg_code = logo_code
        logo.save()

        return redirect('home')
    
    navigations = Navigation.objects.all()[:3]
    if request.method == "POST" and 'navigation_id' in request.POST:
        navigation_id = request.POST.get('navigation_id')
        navigation_name = request.POST.get('navigation_name')
        navigation =  Navigation.objects.get(id = navigation_id)
        navigation.name = navigation_name
        navigation.save()

        return redirect('home')
    
    slides = Slide.objects.all()
    if request.method == "POST" and 'slide_id' in request.POST:
        slide_id = request.POST.get('slide_id')
        slide_text = request.POST.get('slide_text')
        slide_color = request.POST.get('slide_color')
        slide =  Slide.objects.get(id = slide_id)
        slide.text = slide_text
        slide.class_name = slide_color
        slide.save()

        return redirect('home')

    slideinfo = SlideInfo.objects.first()

    if request.method == "POST" and 'slide_caption' in request.POST:
        slide_caption = request.POST.get('slide_caption')
        slideinfo.caption = slide_caption
        slideinfo.save()

        return redirect('home')
    
    footer = Contact.objects.first()
    if request.method == "POST" and 'footer_description' in request.POST:
        footer_description = request.POST.get('footer_description')
        footer_shote_note = request.POST.get('footer_shote_note')
        footer.description = footer_description
        footer.short_info = footer_shote_note
        footer.save()

        return redirect('home')
    
    terms =  TermsAndConditions.objects.first()
    if request.method == "POST" and 'terms_page' in request.POST:
        terms_page = request.POST.get('terms_page')
        terms.terms = terms_page
        terms.save()

        return redirect('home')

    context = {
        'services' : services,
        'portfolio' : portfolio,
        'pricings' : pricings,
        'contact' : contact,
        'queries' : queries,
        'logo' : logo,
        'navigations':navigations,
        'slides':slides,
        'slideinfo':slideinfo,
        'footer':footer,
        'terms':terms
    }
    
    return render(request,'components/home.html',context)

def editService(request,pk):
    service = Services.objects.get(id = pk)

    if request.method == "POST" and 'service_price' in request.POST:
        service_price = request.POST.get('service_price')
        service_description = request.POST.get('service_description')
        service.rate = service_price
        service.description = service_description
        button_name = request.POST.get('before_image')
        service.button_name = button_name
        
        after_image = request.FILES.get('after_image')
        if after_image:
            service.after = after_image
        
        service.save()

        return redirect('home')

    context = {
        'service':service
    }
    return render(request,'components/editService.html',context)

def editSubService(request,pk):
    service = SubServices.objects.get(id = pk)

    if request.method == "POST" and 'service_price' in request.POST:
        service_price = request.POST.get('service_price')
        service_description = request.POST.get('service_description')
        service.rate = service_price
        service.description = service_description
        before_image = request.FILES.get('before_image')
        if before_image:
            service.before = before_image
        
        after_image = request.FILES.get('after_image')
        if after_image:
            service.after = after_image
        
        service.save()

        return redirect('home')

    context = {
        'service':service
    }
    return render(request,'components/editSubService.html',context)

def editPricing(request,pk):
    pricing = Pricing.objects.get(id = pk)

    if request.method == "POST" and 'pricing_name' in request.POST:
        pricing_name = request.POST.get('pricing_name')
        pricing_price = request.POST.get('pricing_price')

        pricing.name = pricing_name
        pricing.rate = pricing_price
        pricing.save()
        
        return redirect('home')

    context = {
        'pricing':pricing
    }
    return render(request,'components/editPricing.html',context)


def editPortfolio(request,pk):
    portfolio = Portfolio.objects.get(id = pk)
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        portfolio.thumb = uploaded_file
        portfolio.save()

        return HttpResponse('File uploaded successfully!')
    else:
        return HttpResponseBadRequest('Invalid request')
