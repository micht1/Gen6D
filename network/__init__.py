from Gen6D.network.detector import Detector
from Gen6D.network.refiner import VolumeRefiner
from Gen6D.network.selector import ViewpointSelector

name2network={
    'refiner': VolumeRefiner,
    'detector': Detector,
    'selector': ViewpointSelector,
}
