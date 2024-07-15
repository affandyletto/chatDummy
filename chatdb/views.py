from django.shortcuts import render
import json
from django.shortcuts import render, redirect
from django.views import View
from chatdb.forms import ChatForm
from django.http import JsonResponse

class Home(View):
	def get(self, request):
		form = ChatForm()

		#Edit Here for starting message
		startingMessage="Starting Message"
		return render(request, 'chatdb/home.html',{'form': form, 'startingMessage':startingMessage})

	def post(self, request):
		if request.method == "POST":
			data = request.body
			data = data.decode('utf-8')
			data = json.loads(data)
			chat_message= data['userMessage']


			#Editable Here
			source=[
				{
					"question":"hello 1",
					"answer":"answer of hello 1",
					"source":"source of hello 1"
				},{
					"question":"hello 2",
					"answer":"answer of hello 2",
					"source":"source of hello 2"
				},{
					"question":"hello 3",
					"answer":"answer of hello 3",
					"source":"source of hello 3"
				},{
					"question":"hello 4",
					"answer":"answer of hello 4",
					"source":"source of hello 4"
				},
			]

			

			ai_message = ""
			theSource=""
			for item in source:
				if item['question'] == chat_message:
					ai_message = item['answer']
					theSource=item['source']
					break  # Exit the loop once the matching answer is found
			return JsonResponse({'message': "message", 'response': {
				"answer":ai_message,
				"source":theSource
				}})
			
		return redirect('/')