from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule

from code.agents import Wolf, Sheep, GrassPatch
from code.model import WolfSheepPredation


def wolf_sheep_portrayal(agent):
    if agent is None:
        return

    portrayal = {"Shape": "circle",
                 "Filled": "true"}

    if type(agent) is Sheep:
        portrayal["Color"] = "#0000FF"
        portrayal["r"] = 0.8
        portrayal["Layer"] = 1

    elif type(agent) is Wolf:
        portrayal["Color"] = "#FF0000"
        portrayal["r"] = 0.8
        portrayal["Layer"] = 2

    elif type(agent) is GrassPatch:
        if agent.fully_grown:
            portrayal["Color"] = "#00AA00"
        else:
            portrayal["Color"] = "#D6F5D6"
        portrayal["Shape"] = "rect"
        portrayal["Layer"] = 0
        portrayal["w"] = 1
        portrayal["h"] = 1

    return portrayal

canvas_element = CanvasGrid(wolf_sheep_portrayal, 20, 20, 500, 500)
chart_element = ChartModule([{"Label": "Predator", "Color": "#FF0000"},
                             {"Label": "Prey", "Color": "#0000FF"}])

server = ModularServer(WolfSheepPredation, [canvas_element, chart_element],
                       "PredatorPrey")
# server.launch()
