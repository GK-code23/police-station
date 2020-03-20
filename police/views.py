from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import police_info
import datetime
from django.contrib import messages
from police.form import police_infoForm,criminal_form,lost_found_form,noticeinfoForm,search_helpForm
from police.models import police_info,criminal,lost_and_found,notice,search_help
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.cache import cache_control
from io import BytesIO
from django.template.loader import get_template
import xhtml2pdf
from xhtml2pdf import pisa
from django.views.generic import View
from police.fusioncharts import FusionCharts
from django.template import Context
import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa

def login_request(request):
    return render(request,"police/header.html")

def home(request):
    return render(request,"police/home.html")



def login_main(request):
    context={}
    police = police_info.objects.all()
    notices = notice.objects.all()
    if request.method == "POST":
        buckel = request.POST.get('pol_id',False)
        buckel=int(buckel)
        password = request.POST.get("password",False)


        for i in police:
            if(buckel==i.pol_id and password==i.pol_pass):
                key = i.clas
                print(key)
                user=1
                break
            else:
                user=0

        police=police_info.objects.get(pol_id=i.pol_id)
        print(police)
        if (user==1 and key=="1"):
            #print("Hello")
            return render(request,"police/home.html",{'police':police,'notices':notices})
        if (user==1 and key=="2"):
            #print("Hello")
            return render(request,"police/home2.html",{'police':police,'notices':notices})
        if (user==1 and key=="3"):
            #print("Hello")
            return render(request,"police/home3.html",{'police':police,'notices':notices})
        else:
            context["error"] = "Provide valid cardentials !!!!"
            return render(request,"police/header.html",{'error':context["error"]})
    else:
        print("Hello1")
        return render(request,"police/header.html")

def pol(request):
    one = int(123)
    two = int(456)
    three = int(789)
    if request.method == "POST":
        form = police_infoForm(request.POST)
        print(form)
        key = request.POST.get("secret_key",False)
        id = request.POST.get("pol_id", False)
        key=int(key)

        if(key==one):

            if form.is_valid():
                try:
                    form.save()
                    police = police_info.objects.get(pol_id=id)
                    police.clas="1"
                    police.save()
                    return redirect('/login')
                except:
                    pass
        if (key == two):

            if form.is_valid():
                try:
                    form.save()
                    police = police_info.objects.get(pol_id=id)
                    police.clas = "2"
                    police.save()
                    return redirect('/login')
                except:
                    pass

        if (key == three):

            if form.is_valid():
                try:
                    form.save()
                    police = police_info.objects.get(pol_id=id)
                    police.clas = "3"
                    police.save()
                    return redirect('/login')
                except:
                    pass
    else:
        form =police_infoForm()

    return render(request,"police/index.html",{'form':form})

def fir(request):
    if request.method == "POST":
        form = criminal_form(request.POST)
        print(form)
        print("1")
        if form.is_valid():
            try:
                form.save()
                print(2)
                return render(request,"police/home.html")
            except:
                pass
    else:
        form =criminal_form()
        print("3")
    return render(request,"police/fir.html",{'form':form})

def show(request):
    police = police_info.objects.all()
    print(police)
    for i in police:
        if(i.pol_post=="I.P.S."):
            i.salary="80000"
        if(i.pol_post == "P.I."):
            i.salary = "70000"
        if (i.pol_post == "P.S.I."):
            i.salary = "65000"
        if (i.pol_post== "A.P.I."):
            i.salary = "60000"
        if (i.pol_post== "A.S.I."):
            i.salary = "55000"
        if (i.pol_post== "H.C."):
            i.salary = "50000"
        if (i.pol_post== "P.N."):
            i.salary = "40000"
        if (i.pol_post== "P.C."):
            i.salary = "35000"
        i.save()
    return render(request,"police/show.html",{'police':police})


def firshow(request):
    fir_show =criminal.objects.all()
    return render(request,"police/fir1.html",{'fir_show':fir_show})

def search_pol(request):
    context={}
    query = request.GET.get("search",None)
    qs = police_info.objects.all()
    if query is not None:
        qs = qs.filter(pol_id=query)
        if qs.exists():
            return render(request, "police/show.html", {'police': qs})
        else:
            context["error"] = "There is no Such Record !!!!"
            print(context["error"])
            return render(request, "police/show.html", {'error': context["error"]})
    else:
        context["error"] = " "
        print(context["error"])
        return render(request, "police/show.html", {'error':context["error"]})

def search_police(request):
    context={}
    query = request.GET.get("search",None)
    qs = police_info.objects.all()
    if query is not None:
        qs = qs.filter(pol_id=query)
        if qs.exists():
            return render(request, "police/overall_record.html", {'police': qs})
        else:
            context["error"] = "There is no Such Record !!!!"
            print(context["error"])
            return render(request, "police/overall_record.html", {'error': context["error"]})
    else:
        context["error"] = " "
        print(context["error"])
        return render(request, "police/show.html", {'error':context["error"]})


def search_chart(request):
    context={}
    query = request.GET.get("search",None)
    qs = police_info.objects.all()
    if query is not None:
        qs = qs.filter(pol_id=query)
        if qs.exists():
            return render(request, "police/daily_chart.html", {'police': qs})
        else:
            context["error"] = "There is no Such Record !!!!"
            print(context["error"])
            return render(request, "police/daily_chart.html", {'error': context["error"]})
    else:
        context["error"] = " "
        print(context["error"])
        return render(request, "police/show.html", {'error':context["error"]})


def search_fir(request):
    context={}
    query = request.GET.get("search",None)
    qs = criminal.objects.all()
    if query is not None:
        qs = qs.filter(id=query)
        if qs.exists():
            return render(request,"police/fir1.html",{'fir_show':qs})
        else:
            context["error"] = "There is no Such Record !!!!"
            print(context["error"])
            return render(request, "police/show.html", {'error': context["error"]})

def search_status(request):
    context = {}
    query = request.GET.get("search", None)
    qs = criminal.objects.all()
    print(qs)
    if query is not None:
        qs = qs.filter(id=query)
        if qs.exists():
            return render(request, "police/status_report.html", {'criminal': qs})
        else:
            context["error"] = "There is no Such Record !!!!"
            print(context["error"])
            return render(request, "police/status_report.html", {'error': context["error"]})



def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class GeneratePDF(View):
    def get( request, *args, **kwargs):
        k=kwargs['id']
        police = criminal.objects.get(id=k)
        template = get_template('police/fir_report.html')
        pdf = render_to_pdf('police/fir_report.html',{'police':police})
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename=%s" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename=%s" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")




def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path


def render_pdf_view(request,id):
    police = criminal.objects.get(id=id)
    template_path = 'police/fir_report.html'
    context = {'police': police}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    print(link_callback)
    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def edit(request,pol_id):
    print(pol_id)
    police  = police_info.objects.get(pol_id=pol_id)
    return render(request,"police/edit.html",{'police':police})

def update(request,pol_id):
    police = police_info.objects.get(pol_id=pol_id)
    print(police)
    form = police_infoForm(request.POST, instance=police)
    print(form)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,"police/edit.html",{'police':police})

def delete(request,pol_id):
    police = police_info.objects.get(pol_id=pol_id)
    police.delete()
    return redirect("/show")

def logout_request(request):
    messages.success(request,"logged out succesfully")
    return redirect("/login")

def daily_chart(request):
    police = police_info.objects.all()
    for i in police:
        i.set="1"
        i.save()
    return render(request,"police/daily_chart.html",{'police':police})

def update_daily(request,id):
    x = datetime.datetime.now()
    x=x.strftime("%d")
    y = datetime.datetime.now()

    y=y.strftime("%A")
    y = y.lower()

    police = police_info.objects.get(pol_id=id)
    police.schedule = request.POST.get("schedule")
    k = police.daily_cnt

    b = police.off_day
    m = police.overtime
    print(y,b)
    if(b==y):
        police.overtime = m +1
    police.save()
    if(police.schedule=="None"):
        a=1
    else:
        police.daily_cnt = k+1

    police.set = "0"
    police.save()
    police = police_info.objects.all()
    return render(request,"police/daily_chart.html",{'police':police})

def chart(request):
    police = police_info.objects.all()
    return render(request, 'police/chart.html',{'police':police})



def piechart(request,id):
    police = police_info.objects.get(pol_id=id)
    reg=police.daily_cnt
    over = police.overtime
    # Create an object for the pie3d chart using the FusionCharts class constructor
    pie3d = FusionCharts("pie3d", "ex2" , "100%", "400", "chart-1", "json",
        # The data is passed as a string in the `dataSource` as parameter.

    {
        "chart": {
            "caption": " Contributed Attendance Performanace",
            "subCaption" : "sdfsfxdffd",
            "showValues":"1",
            "showPercentInTooltip" : "0",
            "numberPrefix" : "days",
            "enableMultiSlicing":"1",
            "theme": "fusion"
        },
        "data": [{
            "label": "Regular",
            "value": reg
        }, 
        {
            "label": "Overtime",
            "value": over
        },
        ]
    })

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return  render(request, 'police/piechart.html', {'output' : pie3d.render(), 'chartTitle': 'Performance Chart','police':police})



def overall_record(request):
    police = police_info.objects.all()
    return render(request, 'police/overall_record.html', {'police': police})


def investigation_report(request):
    criminal_1 = criminal.objects.all()
    return render(request,"police/status_report.html",{'criminal':criminal_1})

def update_status(request,id):
    police = criminal.objects.get(id=id)
    police.status = request.POST.get("status")
    police.save()
    police = criminal.objects.all()
    return render(request, "police/status_report.html", {'criminal': police})


def lost_found(request):
    print("shyam")
    if request.method == "POST":
        form = lost_found_form(request.POST)
        print(form)
        if form.is_valid():
            try:
                form.save()
                return redirect('/home')
            except:
                pass
    else:
        form =lost_found_form()
    return render(request,"police/lostfound.html",{'form':form})

def showlf(request):
    context = {}
    police =lost_and_found.objects.all()
    return render(request,"police/lostfountshow.html",{'criminal':police})


def noticeadd(request):
    notices = notice.objects.all()
    if request.method == "POST":
        form =noticeinfoForm(request.POST)
        print(form)
        if form.is_valid():
            print("1")
            form.save()
            print("2")
            return render(request,"police/home.html",{'notices':notices})

    else:
        form=noticeinfoForm()
    return render(request, "police/noteiceinsert.html", {'form':form})

def notices(request):
    notes= notice.objects.all()
    return render(request,"police/notice.html",{'my_note':notes})

def deletenotice(request,id):
    mynote=notice.objects.get(id=id)
    mynote.delete()
    return redirect('/notices')
def editnotice(request,id):
    note =notice.objects.get(id=id)
    return render(request, "police/noticeedit.html", {'note': note})

def nupdate(request,id):
    ins = notice.objects.get(id=id)
    print(ins)
    form= noticeinfoForm(request.POST,instance=ins)
    print(form)
    if(form.is_valid):
        print("1")
        form.save()
        return redirect("/notices")
    return render(request,"police/noticeedit.html",{'ins': ins})

def help(request):
    return render(request,"police/help.html")

def search_lost_found(request):
    context={}
    name = request.GET.get("name", None)
    phone = request.GET.get("ph", None)
    se = search_help.objects.all()


    article= request.GET.get("article_type",None)
    qs = lost_and_found.objects.all()
    report_type = request.GET.get("report_type",None)
    location = request.GET.get("location",None)
    if article is not None:
        qs = qs.filter(article_type=article,report_type=report_type,loc_of_incedent=location)
        print(qs)
        for i in qs:
            k = i.id
        m = search_help(name=name, ph=phone,case_id=k)
        m.save()
        if qs.exists():
            return render(request,"police/lostfountshow.html",{'criminal':qs})
        else:
            context["error"] = "No such item found!!!!"
            print(context["error"])
            return render(request, "police/lostfountshow.html", {'error': context["error"]})

def search_lost12(request):
    context = {}
    query = request.GET.get("search", None)
    qs = lost_and_found.objects.all()
    if query is not None:
        qs = qs.filter(id=query)
        print(qs)
        if qs.exists():
            print(qs)
            return render(request, "police/lostfountshow.html", {'criminal': qs})
        else:
            context["error"] = "There is no Such Record !!!!"
            print(context["error"])
            return render(request, "police/lostfountshow.html", {'error': context["error"]})


def police_station(request):
    return render(request,"police/police_station.html")

def request1(request):
    se = search_help.objects.all()
    return render(request,"police/request1.html",{'se':se})

def deletere(request,id):
    se = search_help.objects.get(id=id)
    se.delete()
    return redirect("/request")

def search_ls(request,id):

    query = id
    qs = lost_and_found.objects.all()
    if query is not None:
        qs = qs.filter(id=query)
        print(qs)
        if qs.exists():
            print(qs)
            return render(request, "police/lostfountshow.html", {'criminal': qs})
        else:
            context["error"] = "There is no Such Record !!!!"
            print(context["error"])
            return render(request, "police/lostfountshow.html", {'error': context["error"]})


def fir_report1(request,id):
    police = criminal.objects.get(id=id)
    template = get_template('police/fir_report.html')
    return render(request,'police/fir_report1.html', {'police': police})