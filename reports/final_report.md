# Hacking Predator Prey Dynamics
By Danny Kang </br>
![Image of visualization](https://github.com/kdy304g/HackingPredatorPreyDynamics/blob/master/images/5d657ee2baf4d.image.jpg)

## Motivating Question
The dynamics of interacting populations of predators and their prey have long been a topic of interest in population biology. Classical model that explains this predator-prey dynamics is Lotka-Volterra Model which explains the relationship in terms of differential euqations. According to Lotka-Volterra Model, the population of both predator and prey go through cyclical fluctuations. </br>
We can approach this problem from a different angle using agent based models. Rather than describe relationsihps between properties of populations, behavior of individuals could be determined to produce similar osciallting pattern. 

## Experiment (without grass)
We start from the most simple model where there are only wolves and sheeps in the living environment. Agents are born with set amount of energy and each time they move, their energy is reduced by certain amount. For the population increase, agents reproduce under predetermined probability. 

### Model
Wolves and sheeps live on two dimensional square grid. The grid is initialized with set number of wolves and sheeps where they behave according to rules that govern their moves. Location of agents is random on the 20 by 20 grid.</br>

*Wolf rules* </br>
1. Move randomly to an adjacent cell and decrease energy
2. If on the same cell as one or mroe sheep, then eat a sheep and increase energy (eaten sheep dies)
3. If energy < 0 then die
4. With certain probability reporduce

*Sheep rules* </br>
1. Move randomly to an adjacent cell
2. With certain probability, reproduce

### Result & Interpretation
<p align="center">
   <img src="https://github.com/kdy304g/HackingPredatorPreyDynamics/blob/master/images/1.png" />
   *Fig. 1: When wolf has low reproducibility*
</p>

<p align="center">
   <img src="https://github.com/kdy304g/HackingPredatorPreyDynamics/blob/master/images/2.png" />
   *Fig. 2: When wolf has high reproducibility*
</p>

![Image](https://github.com/kdy304g/HackingPredatorPreyDynamics/blob/master/images/1.png) </br>
*Fig. 1: When wolf has low reproducibility*

![Image](https://github.com/kdy304g/HackingPredatorPreyDynamics/blob/master/images/2.png) </br>
*Fig. 1: When wolf has high reproducibility*

## Experiment (with grass)

### Model
Predators and preys will live on two dimensional square grid. The grid will be initialized randomly with set number of predators and preys and agents (predators and preys) will behave according to rules that define their moves. </br>

*Predator rules </br>
1. Move randomly to an adjacent cell and decrease energy
2. If on the same cell as one or mroe sheep, then eat a sheep and increase energy
3. If energy < 0 then die
4. With certain probability reporduce

*Prey rules </br>
1. Move randomly to an adjacent cell
2. With certain probability, reproduce

I will start with a very simple model as explained above and build and modify on it depending on result.

### Result & Interpretation
grass low regrowth time
grass high regrowth time

## Conclusion & Future Works

## Reference
* Thinking like a wolf, a sheep, or a firefly </br>
http://ccl.northwestern.edu/papers/wolfsheep.pdf </br>

* The Dynamics of the Lynx-Hare System: an Application of the Lotka-Volterra Model
https://link.springer.com/content/pdf/10.1134%2FS000635091601019X.pdf </br>

### Visualization Software
* Mesa </br>
https://mesa.readthedocs.io/en/master/ </br>
Mesa is an agent-based modeling framework in Python. 
