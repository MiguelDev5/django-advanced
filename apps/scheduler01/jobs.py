from django.conf import settings
import requests
import json
import random
import datetime

def schedule_api():

	print(getCurrentTime())

def getCurrentTime():
	now = datetime.datetime.now()
	m = 2 - now.minute%3
	s = 59 - now.second
	if m==0 and s==0:
		m = 3
	if s < 10:
		s = f"0{s}"
	return f"Actualización en: {m}:{s}"