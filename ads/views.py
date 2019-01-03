from .models import Ad, Interaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
import math
import pandas as pd
import random
def home(request):
 
	if not request.session.get('user_interaction_id', None):
		new = Interaction()
		new.save()
		request.session['user_interaction_id'] = new.id

	df = pd.DataFrame.from_records(Interaction.objects.all().values(), columns=['ad_1', 'ad_2', 'ad_3', 'ad_4', 'ad_5', 'ad_6', 'ad_7', 'ad_8', 'ad_9', 'ad_10']) 
	N = len(df)#Number of users
	d = len(df.columns) #Number of ads
	ads_selected = []
	ads_rewards = [0] * d 

	numbers_of_rewards_1 = [0] * d
	numbers_of_rewards_0 = [0] * d

	for n in range(0, N):#For each user
		ad = 0
		max_random = 0
		for i in range(0, d):#for each add
			random_beta = random.betavariate(numbers_of_rewards_1[i] + 1, numbers_of_rewards_0[i] + 1)

			if random_beta > max_random:
				max_random = random_beta 
				ad = i
				ads_rewards[i] += df.values[n, i]

		ads_selected.append(ad)
		reward = df.values[n, ad]
		if reward == 1:
			numbers_of_rewards_1[ad] += 1
		else:
			numbers_of_rewards_0[ad] += 1

	ads = Ad.objects.all()
	context = {
		'clicks' : ads_rewards,
		'numb1' : numbers_of_rewards_1,
		'numb0' : numbers_of_rewards_0,
		'selected' : ads_selected,#The ads displayed to all users
        'ad' : ads[ad]#Display the ad that the algorithm predicted for the last user. This would converge with time
    }
	return render(request,'ads/home.html', context)

def like(request, ad):
	inter_id = 0
	cell = f"ad_{ad}"
	inter_id = request.session['user_interaction_id']
	Interaction_Thomas.objects.filter(pk=inter_id).update(**{cell : 1})

	return redirect( reverse_lazy('ads-home') )

def dislike(request, ad):
	inter_id = 0
	cell = f"ad_{ad}"
	inter_id = request.session['user_interaction_id']
	Interaction_Thomas.objects.filter(pk=inter_id).update(**{cell : 0})

	return redirect( reverse_lazy('ads-home') )


	