import bge


def main():

    c = bge.logic.getCurrentController()
    own = c.owner
    
    shotFired=c.sensors["shotFired"]
    ray=c.sensors["ray"]
    
    if ray.positive:
        target=ray.hitObject
        if shotFired.positive:
            target["health"]-=1

main()
