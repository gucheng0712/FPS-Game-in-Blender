import bge


def main():

    c = bge.logic.getCurrentController()
    own = c.owner
    
    damage=c.sensors["Damage"]
    
    if damage.positive:
        own["Health"]-=50
    
    if own["Health"]<=0:
        bge.logic.restartGame()        

    health=str(own["Health"])
    own.text="HP: "+health


main()
