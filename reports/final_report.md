# Hacking Predator Prey Dynamics
By Danny Kang </br>

<p align="center">
     <img src="https://github.com/kdy304g/HackingPredatorPreyDynamics/blob/master/images/0.jpg" />
</p>

## Motivating Question
The dynamics of interacting populations of predators and their prey have long been a topic of interest in population biology. Classical model that explains this predator-prey dynamics is Lotka-Volterra Model which explains the relationship in terms of differential euqations. According to Lotka-Volterra Model, the population of both predator and prey go through cyclical fluctuations. </br>
We can approach this problem from a different angle using agent based models. Rather than describe relationsihps between properties of populations, behavior of individuals could be determined to produce similar osciallting pattern. 

## Experiment (without grass)
We start from the most simple model where there are only wolves and sheeps in the living environment. Agents are born with set amount of energy and each time they move, their energy is reduced by certain amount. For the population increase, agents reproduce under predetermined probability. 

### Model
Wolves and sheeps live on two dimensional square grid. The grid is initialized with set number of wolves and sheeps where they behave according to rules that govern their moves. More specifically, the model starts with 100sheeps and 40 wolves. Location of agents is random on the 20 by 20 grid.</br>

*Wolf rules* </br>
1. Move randomly to an adjacent cell and decrease energy
2. If on the same cell as one or mroe sheep, then eat a sheep and increase energy (eaten sheep dies)
3. If energy < 0 then die
4. With certain, probability reporduce

*Sheep rules* </br>
1. Move randomly to an adjacent cell
2. With certain probability, reproduce

### Result & Interpretation
There are many ways to influence the population dynamics of this model by changing value of parameters. To list some of them, metabolism of agents, amount of energy gain by a wolf when eat consumes a sheep, and reproducibility of agents. In a grid as small as its size being 20 by 20, reproducibility of wolves has the most powerful influence on the population dynamics. Increasing its value even by one percent brings huge change. If the reproducibility of wolves is 5 percent, then each wolves produce its offspring every twenty stpes and the population increase is exponential. </br>
<p align="center">
     <img src="https://github.com/kdy304g/HackingPredatorPreyDynamics/blob/master/images/1.png" />
     <figcaption>Fig. 1: When wolf has low reproducibility</figcaption>
</p>
In figure 1, reproducibility of wolves is one percent. Initially, the number of sheeps decreases drastically untill step 80. Population of sheep becomes less then that of wolves at about step 20. Similar to the L-V model, the population of sheeps surpasses that of the wolves around step 140. Unfortunately, the cyclical pattern is not observed in this graph as in the L-V model. Rather, the population of sheeps explodes after step 150 while the poulation of wolves reamins steady due to its low reproducibility. </br>

<p align="center">
   <img src="https://github.com/kdy304g/HackingPredatorPreyDynamics/blob/master/images/2.png" />
   <figcaption>Fig. 2: When wolf has high reproducibility</figcaption>
</p>
In figure 2, reproducibility of wolves is three percent. Unlike in the previous graph, the population of sheeps reaches 0 as fast as around step 60. Also, the population of wolves surpasses that of sheeps in only around step 10. This is not too surprising considering that reproduciblity of wolves has trifolded from the previous version of this model. The population of wolves increases mildly untill about step 35 and then starts to decline as there are no more sheeps to prey on. </br>

The model was also tested with different reproducibility for wolves and sheeps and it did not produce the desired cyclical pattern as in the L-V model. 

## Experiment (with grass)
It is not hard to realize the limit of the previous model. The problem is that either the population of sheeps explode and never decrease or that no one survives in the environment because the population of wolves over dominate that of sheeps. To get as close as possible to the pattern in the L-V model, we can conjecture that adding a limiting factor to the population of sheeps while the wolves has low reproducibility would produce somewhat similar patterns. 

### Model
Everything is the same in this model except for the addition of new agent, grass. Grass don't move in any direction and its whole purpose of existence is to be eaten by sheeps. Now, sheeps need grass for survival since their metabolism is not ridiculously efficient(surviving without food) anymore. Grass regrows after being eaten by sheeps every 30 steps. </br>

*Wolf rules* </br>
1. Move randomly to an adjacent cell and decrease energy
2. If on the same cell as one or mroe sheep, then eat a sheep and increase energy
3. If energy < 0 then die
4. With certain probability, reporduce

*Sheep rules* </br>
1. Move randomly to an adjacent cell
2. If on the same cell as grass, then eat grass and increase energy
3. If energy <0 then die
3. With certain probability, reproduce

*Grass rules* </br>
1. If eaten by sheep, die
2. Regrow after 30 steps, once eaten by sheep

### Result & Interpretation
<p align="center">
     <img src="https://github.com/kdy304g/HackingPredatorPreyDynamics/blob/master/images/3.png" />
     <figcaption>Fig. 3: When wolf has low reproducibility</figcaption>
</p>
In figure 3, the population of sheep sharply decreases initially untill step 40. The population of wolf also decreases but not as drastically as sheep untill step 100. The population of sheep reaches its first peak at around step 150 after its sharp decrease from beginning. After that, it fluctuates between 40 and 20. The population of wolf stays between 3 and 5 until it goes extinct at step 740. </br>

<p align="center">
     <img src="https://github.com/kdy304g/HackingPredatorPreyDynamics/blob/master/images/4.png" />
     <figcaption>Fig. 4: When wolf has high reproducibility</figcaption>
</p>
Unlike figure 3, the population of wolf does not decrease sharply in figure 4. This is because of the higher reproducibility of wolf. The population of sheep decreases sharply and slowly increases once wolvese become extinct. From figure 4, we can tell that when reproducibility of wolves is high, wolves deplete their food source too fast that they are bound to become extinct shortly. </br>

Of all the figures shown above, the longest coexistence of wolf and sheep is in figure 3. The difference between the experiments for figure 1 and 3 is that in the experiment for figure 3, grass actively fulfills its role as an inhibiting factor against sheep population since sheeps have limited food source for survival. Another insight is that the equilibrium between wolves and sheeps in figure 3 is maintained untill about step 700 while the population of wolves is small. Wolves start with the population of 40 and they persist by being reduced to population of only 3 to 5. 

## Conclusion & Future Works
Manipulating the parameters for the models yield different patterns in the population of agents. So far, sustainable model where all agents coexist permanently could not be achieved. However, the oscillating pattern in the L-V model is replicated (Fig. 3) in the model where grass is a limiting factor for sheeps and wolves have low reproducibility. </br>
There are many ways models above could be extended and complicated. Models constructed in this paper are result of oversimplification of real world system. For example, agents in this paper move purposelessly in random directions whereas in the real world, predators can chase preys from far distance. Also, sheeps in this paper are inevitably consumed by wolves when they encounter each other in the same cell, but in the real world, there is a chance that prey escapes away from predator. 


## Reference
* Thinking like a wolf, a sheep, or a firefly </br>
http://ccl.northwestern.edu/papers/wolfsheep.pdf </br>

* The Dynamics of the Lynx-Hare System: an Application of the Lotka-Volterra Model
https://link.springer.com/content/pdf/10.1134%2FS000635091601019X.pdf </br>

* The Computational Beauty of Nature </br>
Gary William Flake

### Visualization Software
* Mesa </br>
https://mesa.readthedocs.io/en/master/ </br>
Mesa is an agent-based modeling framework in Python. 
