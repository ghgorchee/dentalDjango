from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
	return render(request, 'home.html', {})


def contact(request):
	if request.method == 'POST':
		# do stuff
		name = request.POST['message-name']
		email = request.POST['message-email']
		message = request.POST['message']

		# Send Email
		send_mail(
			'Website Message from: ' + email, # Subject
			'Contact Name: ' + name + ' ======== ' + 'Message: ' + message, # message
			email, # from email
			['rli@arlico.us'], # to email
			fail_silently=False,
			)

		return render(request, 'contact.html', {})

	else:
		# return the page
		return render(request, 'contact.html', {})
