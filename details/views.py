from django.shortcuts import render, redirect
from .models import Inquery, News
from django.contrib.auth import authenticate
from django.http import HttpResponse
from .resources import PersonResource , NewsResource
from django.contrib import messages


def index(request):
	if request.method == 'POST':
		print('if')
		try:
			print('try')
			name = request.POST.get('name')
			print(name)
			email = request.POST.get('email')
			subject = request.POST.get('subject')
			message = request.POST.get('message')
			print(message)
			form_data = Inquery(name = name, email = email, subject = subject, message = message)

			form_data.save() 
			messages.success(request, 'Your query has successfully deliver.')
			print('SAVE')
			return render(request, 'index.html')


		except:
			print('except')
			if request.method == 'POST':
				print('if')
				try:
					print('if try')
					email = request.POST.get('EMAIL')
					print(email)
					new_data = News(EMAIL = email)
					print(1)
				
					new_data.save()
					print('EMAIL.save()')

					return render(request, 'index.html')

				except:
					pass

	else:
		print('else')
		return render(request, 'index.html')

def export(request):

    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    return response