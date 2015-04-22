"""
Data Comm Project
Plain and Slotted ALOHA
"""

import csv
import random

def simulate(tau, n, protocol='plain'):
	"""tau is the window size, n is the number of transmissions, protocol should be plain/slotted (default plain)"""
	#Get transmission times, sort them. 
	if protocol == 'plain':
		times = sorted(get_packet_times(n, 1))
	else:
		times = sorted(get_packet_times(n, tau))
	collisions = 0
	#Select either 2*tau for danger zone or tau for slotted
	ws = 2*tau
	if protocol == 'slotted':
		ws = tau
	for i in range(len(times)-1):
		#Check for collisions
		if times[i]+(ws) >= times[i+1]:
			collisions += 1
	return collisions

def get_packet_times(n, tau=1):
	step = 1.0/tau #For slotted, set window size to align times to
	start_times = []

	#If tau != 1, we have a synchronied clock w/ window size tau
	if tau != 1:
		for i in range(n):
			start_times.append(random.randrange(0, 1*step, tau*step)/step)
	#If tau == 1, we are doing plain aloha and just want floats between 0, 1 with max precision
	else:
		for i in range(n):
			start_times.append(random.random())
	return start_times

def average_simulation(tau, transmissions, n, protocol='plain'):
	average = 0
	for i in range(n):
		average += simulate(tau, transmissions, protocol)
	return average/float(n)

def output_csv(start, end, step, transmissions, n, outfile):
	if start > end:
		temp = start
		start = end
		end = temp
		step *= -1.0
	with open(outfile, 'w') as csvfile:
		grapher = csv.writer(csvfile, dialect='excel')
		grapher.writerow(['Tau', 'Plain Collisions', 'Slotted Collisions'])
		while start <= end:
			plain_collisions = average_simulation(start, transmissions, n)
			slotted_collisions = average_simulation(start, transmissions, n, 'slotted')
			grapher.writerow([start, plain_collisions, slotted_collisions])
			start += step

