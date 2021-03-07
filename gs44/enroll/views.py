from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'enroll/home.html')



def show_subdetails(request,my_id,my_subid):
    if my_id==1 and my_subid==5:  # by defalut the <my_id> is string or we can use <int:my_id> in urls)
        sttudent={'id':my_id,'name': 'sonam','info':'sub detials'}
    if my_id==2 and my_subid==6:
        sttudent={'id':my_id,'name': 'firoz','info':'sub detials'}
    
    if my_id==3 and my_subid==7:
        sttudent={'id':my_id,'name': 'geeky','info':'sub detials'}

    return render(request,'enroll/show.html',sttudent)






def show_details(request,my_id):
    if my_id=='1':  # by defalut the <my_id> is string or we can use <int:my_id> in urls)
        sttudent={'id':my_id,'name': 'sonam'}
    if my_id=='2':
        sttudent={'id':my_id,'name': 'firoz'}
    
    if my_id=='3':
        sttudent={'id':my_id,'name': 'geeky'}

    print(my_id)
    return render(request,'enroll/show.html',sttudent)






# def show_details(request,my_id):
#     print(my_id)
#     return render(request,'enroll/show.html',{'id':my_id})