from django.shortcuts import render,redirect
from django.http import HttpResponse ,HttpResponseRedirect
from django.core.paginator import Paginator 
import re 
from .forms import std,pr2
from .models import curd

# Create your views here.
def text(request):
 	return HttpResponse("text masages...")

#display the data in html page..
def show(request):
	display=curd.objects.all() #return all record in database
	form=pr2() #return form

	#pagination set

	
	logic=Paginator(display,5) #set logic
	s=logic.count
	p=logic.num_pages
	page_number=request.GET.get('page') #put data in page variable using GET method
	pagination=logic.get_page(page_number) #show page as your wish . 
	#return render(request , "index.html" , {'page':pagination})
	
	return render(request , "index.html" , {  'form':form , 'data':pagination , 's': s ,'p':p })




#add new data in database..
def Add(request):
	if request.method =="POST":
		form=pr2(request.POST)
		fm=pr2()
		
		if form.is_valid(): #is_valid() is a method thst help to check form vslid or not

			#form validation
			p=request.POST.get('phone')
			n=request.POST.get('name')
			e=request.POST.get('email')

			#number validation
			phone=re.fullmatch("[6-9][0-9]{9}",p)
			#phone=ph.match(p)

			#name validation
			name=re.fullmatch("([a-z. ]+)([a-z. ]+)*$",n)
			#name=na.match(n)

			#email validation
			pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
			email=re.match(pat,e)

			

			if name != None:
				if phone != None:
					if email != None:
						form.save()
						return HttpResponseRedirect('/')
					else:
						return render(request, "alert.html" , {'email':email ,'phone':phone,'name':name, 'form':fm})
				else:
					return render(request , "alert.html" , {'email':email,'phone':phone,'name':name, 'form':fm})
			else:
				return render(request , "alert.html" , {'email':email ,'phone':phone,'name':name, 'form':fm})
				
	else:
		form=pr2()

	return HttpResponseRedirect('/')



			
# this is delete function
def delete(request, id):
	if request.method == 'POST':
		form=curd.objects.get(pk=id) #get record , whouse id is given by user 
		form.delete()  #delete() this function  help delete record by given id 
		return HttpResponseRedirect('/')



def edit(request,id):

	f=curd.objects.get(pk=id) 
	fm=pr2(instance=f) #return specific record 
	form=pr2()
	display=curd.objects.all()
	return render(request, "update.html" , { 'id':id ,'data': display , 'form':form ,'up':fm ,})





def update(request,id):
	if request.method=='POST':
		form=curd.objects.get(pk=id)
		fm=pr2(request.POST, instance=form) # any changeing data in record
		if fm.is_valid():
			fm.save()
			return HttpResponseRedirect('/' , {'form':fm})
	else:
		form=curd.objects.get(pk=id)
		fm=pr2( instance=form) # the data is not change 
	
	return HttpResponseRedirect("/" , {'form':fm })	
		
			
def search(request):
	s=0
	p=0
	if request.method=='POST':
		if request.POST != "":
			s=request.POST.get('search')
			query=curd.objects.filter(name=s).values()
			form=pr2()
			logic=Paginator(query,5) #set logic
			s=logic.count
			p=logic.num_pages
			page_number=request.GET.get('page') #put data in page variable using GET method
			pagination=logic.get_page(page_number) #show page as your wish .			

			return render(request , "search.html", {  'form':form , 'data':pagination , 's': s ,'p':p})
		


					
			

			
			


			




				


	
				
	    
	   

