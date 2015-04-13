"""
Data Comm Project
Plain and Slotted ALOHA
"""

import random

def simulate_plain(tau, n):
	"""tau is the window size, n is the number of transmissions"""
	pass


def simulate_slotted(tau, n):
	"""tau is the window size, n is the number of transmissions"""
	pass

def get_packet_times(tau=1, n):
	step = 1.0/tau #For slotted, set window size to align times to
	start_times = []

	for i in range(n):
		start_times.append(random.randrange(0, 1*step, tau*step)/step)

	return start_times