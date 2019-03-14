import bge


def main():

    c= bge.logic.getCurrentController()
    elevator = c.owner
    collisionPlayer=c.sensors["Collision"]
    
    moveUp=c.actuators["MoveUp"]
    if(collisionPlayer.positive):
        c.activate(moveUp)



main()
