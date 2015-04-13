Task:
To simulate both plain and slotted ALOHA, showing how the throughput changes with packet duration tau.

Method:
For plain ALOHA, we can simulate by generating random numbers between 0 and 1. Maybe 1000 numbers. These represent packet start times. Then, they should be sorted. If start time is within tau of another, or end time within tau of another (or 2 tau) there is a collision and both packets fail. If not, it is successful. We need to compute the optimal tau based on the throughput.

For slotted ALOHA, we need to figure out how to simulate this. I think it’s going to be random numbers between 0 and 1 with increments of tau. 

The only thing we need to do for our grade is to show him the simulation, and show a plot of the efficiency/throughput of both protocols with changing tau.