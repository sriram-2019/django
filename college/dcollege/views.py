from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from dcollege.models import staff_sign
from dcollege.models import student_sign
from dcollege.models import photo_p
import mysql.connector as mysql
import re
from io import BytesIO
import zlib
import os
from datetime import datetime
def index(request):
        if request.method=="POST":
            if "sign_up" in request.POST:
                return render(request,"student_signup.html")
            elif 'stu_log' in request.POST:
               print("hello")
            elif("mysub" in request.POST):
                    username = request.POST.get('user', '')
                    if username == '':
                        return JsonResponse({'success': False, 'error': 'Username is required'})
                    else:
                        # Process the form data
                        return JsonResponse({'success': True})
            elif("staff_sub" in request.POST):
                return render(request,'staff_reg.html')
            elif("staffs" in request.POST):
                staff_name=request.POST.get('staff_name','')
                if(staff_name==''):
                    return JsonResponse({'success':False,'error':'username must filled'})
                else:
                    return JsonResponse({'success':True})
        return render(request,'l.html')
def student_signs(request):
    if(request.method=="POST"):
        name=request.POST["user"]
        password=request.POST["password"]
        roll=request.POST["roll"]
        mobile=request.POST["mobile"]
        school=request.POST["school"]
        address=request.POST["address"]
        email=request.POST["email"]
        dob=request.POST["dob"]
        tenth=request.POST["10th"]
        twelth=request.POST["12th"]
        cutoff=request.POST["cutoff"]
        cgpa=request.POST["poly"]
        if(cgpa==''):
            cgpa=0
        save_db=student_sign(name=name,roll_no=roll,password=password,mobile=mobile,email=email,dob=dob,school=school,address=address,tenth=tenth,twelve=twelth,twelth_cutoff=cutoff,cgpa=cgpa)
        save_db.save()
    return render(request,'ll.html')
def staff(request):
     if(request.method=="POST"):
            staffid = request.POST["staffid"]
            staffname = request.POST["staffname"]
            staffemail = request.POST["staffmail"]
            staffconfirm = request.POST["staffconfirm"]
            staff=staff_sign(staffid=staffid,staffname=staffname,staffemail=staffemail,staffconfirm=staffconfirm)
            staff.save()
     return render(request,'ll.html')
def index2(request):
    if request.method == 'POST':
        
        try:
                stud=request.POST.get("student_name")
                request.session["stu_name"]=stud
                con=mysql.connect(host='localhost',username='root',password='sriram',database='col')
                cur=con.cursor()
                query=f"select password from student_signup where roll_no='{stud}'"
                cur.execute(query)
                res=cur.fetchone()
                password=res[0]
                student_pass=request.POST.get("student_password")
                
                if(password!=student_pass):
                    message = 'enter the correct password'
                    data = {
                            'message': message,
                        
                            }
                    return JsonResponse(data)
                else:
                    message='success'
                    data={
                    'message':message,
                    }
                    return JsonResponse(data)
        except:
                    message='invalid username'
                    data={
                        'message':message,
                    }
                    return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request method'})
def photo(request):
    if(request.method=="POST"):
        event_name=request.POST.get('event-name')
        if(event_name==''):
              return JsonResponse({"success":False,"error":"username must be filled"})
        else:
             return JsonResponse({"success":True})
    return render(request,'student_upload.html')
def photo1(request):
    if request.method == 'POST':
        event_name=request.POST.get("event-name")
       
        from_date=request.POST.get("fromdate")
        to_date=request.POST.get("todate")
        event_title=request.POST.get("title")
        event_org=request.POST.get("event-org")
        file=request.FILES.get("file_name")
        from_obj = datetime.strptime(from_date, '%Y-%m-%d')
        to_obj=datetime.strptime(to_date,"%Y-%m-%d")
        year=from_obj.strftime("%Y")
        ac_years=int(year)
        ac_year=f"{ac_years-1}-{ac_years}"
        from_month=from_obj.strftime("%m")
        from_year=from_obj.strftime("%y")
        to_year=to_obj.strftime("%y")
        to_month=to_obj.strftime("%m")
        from_day=from_obj.strftime("%d")
        to_day=to_obj.strftime("%d")
        current_month = datetime.now().month
        current_year = datetime.now().year
        message="message"
        from_month=int(from_month)
        to_month=int(to_month)
        from_year=int(from_year)
        to_year=int(to_year)
        if(from_month>current_month and from_year==current_year):
            message="from date month is greater than current month "
            data={
                  'message':message
            }
            return JsonResponse(data)
        elif(from_month>to_month and from_year==to_year):
            message="from_date month must be less than to_date month"
            data={
                'message':message
            }
            return JsonResponse(data)
        elif((from_day>to_day and from_month<to_month)):
            message="from_date day must be less than to_date day"
            data={
                  'message':message
            }
            return JsonResponse(data)
        else:
            roll_no=request.session.get("stu_name")
            with file.open(mode='rb') as r:
                read=r.read()
            
            compressed=zlib.compress(read)
          
            save_file=photo_p(file_name=f"{datetime.now()}.pdf",file=compressed,title=event_title,from_date=from_date,to_date=to_date,event_org=event_org,academic=ac_year,roll_no=roll_no)
            save_file.save()
            message="success"
            data={
            'message':message            
            }
            return JsonResponse(data)
    return render(request,'student_upload.html')
def gets(request):
     from_date=request.POST.get("from-date")
     to_date=request.POST.get("to-date")
     data={
          'from':from_date,
          'to':to_date
     }
     return JsonResponse(data)
def display_data(request):
    from_value = request.GET.get('from')
    to_value=request.GET.get('to')
    from_value = datetime.strptime(from_value, '%Y-%m-%d').date()
    to_value = datetime.strptime(to_value, '%Y-%m-%d').date()
    from_value=photo_p.objects.filter(from_date__range=[from_value, to_value]).values("file_name","event_org","title","academic","from_date","to_date","ids")
    context = {'from': from_value}
    return render(request, 'sel.html', context)
def get_file(request):
     if request.method=="POST":
        name=request.POST.get('fileName')
        if name:
            roll_nos=request.session.get("stu_name")
            name=name.strip()
            res=photo_p.objects.get(file_name=name)
            compressed_data = zlib.decompress(res.file)
            response = HttpResponse(content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{name}"'
            with BytesIO(compressed_data) as f:
                 response.write(f.read())
            return response

        return render(request,"ll.html")
def all_file(request):
    if request.method=="POST":
        name=request.POST.get('fileName')
        if name:
            roll_nos=request.session.get("stu_name")
            name=name.strip()
            res=photo_p.objects.get(file_name=name)
            compressed_data = zlib.decompress(res.file)
            response = HttpResponse(content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{name}"'
            with BytesIO(compressed_data) as f:
                 response.write(f.read())
            return response
            
    return render(request,"ll.html")
def index3(request):
    if("certificate" in request.POST):
        return render( request,"student_upload.html")
    if("download" in request.POST):
         return render(request,"download.html")
    if("select_date" in request.POST):
         return render(request,"date.html")
    if("select_all" in request.POST):
        roll_no=request.session.get('stu_name')
        res = photo_p.objects.filter(roll_no=roll_no).values("file_name","event_org","title","academic","from_date","to_date","ids")
        context = {"form": res}
        return render(request, "table2.html", context)

    return render(request,"Button.html")
