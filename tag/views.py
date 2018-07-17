from .models import Player

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

import json
import random

def player_create(request):
	body=json.loads(request.body.decode('utf-8'))
	def r64(): return random.randint(0, 63)
	player=Player(password=body['password'], x=r64(), y=r64())
	player.save()
	return HttpResponse(json.dumps({
		'id': player.id,
		'x': player.x,
		'y': player.y,
	}))

def player_move(request):
	body=json.loads(request.body.decode('utf-8'))
	player=Player.objects.get(id=body['id'])
	if player.password!=body['password']: return HttpResponse(status=401)
	if   body['direction']=='up'   : player.y+=1
	elif body['direction']=='right': player.x+=1
	elif body['direction']=='down' : player.y-=1
	elif body['direction']=='left' : player.x-=1
	else: return HttpResponse(status=400)
	player.save()
	return HttpResponse(json.dumps({
		'id': player.id,
		'x': player.x,
		'y': player.y,
	}))

def player_get_all(request):
	return HttpResponse(json.dumps([
		{'id': i.id, 'x': i.x, 'y': i.y}
		for i in Player.objects.all()
	]))

def player_arena(request):
	return HttpResponse(loader.get_template('tag/arena.html').render({}, request))
