# Hacking Predator Prey Dynamics
By Danny Kang
![Image of visualization](https://github.com/kdy304g/HackingPredatorPreyDynamics/blob/master/images/5d657ee2baf4d.image.jpg)

## Abstract
Evolution by natural selection is one of the most widely accepted theory that explains the important question of how we became as we are. Humans, luckily enough, had superior intelligence to endure severe conditions and defend themselves against predators. This, however, is not a common phenomenon among other species. Predators are sometimes more intelligent then preys, or preys are not fast enough to escape from predators. Depending on various factors, the predator-prey dynamics (the population of predator and prey) show different patterns. </br>

Lotka-Volterra Model captures Lynx-Hare system in Canada that was collected by the Hudson Bay Company in 1845-1935 reasonably well. The model is based on two equations that each defines the rate at which population of predator and prey changes according to time. While this model is a good representation of empirical data, an alternative model based on different approach could be made to introduce different perspective on predator prey dynamics. </br>

In this paper, python functions and classes will be used to take an agent based modeling approach to model predator-prey dynamics. The goal of this agent based modeling is to produce similar pattterns to that of empirical data of Hare and Lynx and experiment with parameters to observe and study several interesting predator-prey dynamics.

## Annotated Bibliography
### Reference
* The Dynamics of the Lynx-Hare System: an Application of the Lotka-Volterra Model
https://link.springer.com/content/pdf/10.1134%2FS000635091601019X.pdf </br>
This research paper validates the Lotka-Volterra Model by testing symmetry frequency distributions of deviations between the theoretical trajectories and the empirical datasets and presene or absence of serial correlation. According to the validation, Lotka-Volterra Model is suitable for describing empirical data. 

### Visualization Software
* Mesa </br>
https://mesa.readthedocs.io/en/master/ </br>
Mesa is an agent-based modeling framework in Python. 

## Experiment
Change in population of predator and prey according to time will be analyzed. </br>
Predators and preys can be modeled as agents living in a grid, with set of rules that governing their trajectories and survival. Both predators and prey would live with energy, and would cease to survive when they run out of energy.

### Predator
* Move randomly to an adjacent cell and decrease energy
* If there is no remaining energy, die
* If on the same cell as one or more preys, then eat a prey and increase energy
* Reproduce asexually with set parameter for probability 

### Prey
* Move randomly to an adjacent cell
* Reproduce asexually with set parameter for probability

## Experiment Variation
* If there are limited food sources for preys in the environment, under what condition or parameters would agent based modeling be able to produce similar pattern to that of empirical data?
* If predators actively chase preys instead of moving randomly, under what condition or parameters would agent based modeling be able to produce similar pattern to that of empirical data?

## Result
Results of experiments would resemble the oscillating pattern of empirical data.
![Image of visualization](https://github.com/kdy304g/HackingPredatorPreyDynamics/blob/master/images/graph1.png)

## Result Interpretation
Agent based modeling approach for predator-prey population can produce various patterns. Either predator or prey could become extinct or there can be a stablized oscillating pattern of ups and downs for both parties. 

## Causes for Concern
* The paper mentioned in this report employs very complex mathematical standards to validate the Lotka-Volterra Model. Thus, validating the agent based model for predator-prey could be a hassle.
* Reasonable scope of the project is a must since there is no prior expereience with using Mesa and model needs to be made by a single person.

## Next Steps
* Build the model
* Produce population graph
* Analyze result
* Experiment with variation
