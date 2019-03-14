import bge


def main():

    c = bge.logic.getCurrentController()
    gun = c.owner
    
    rightClick=c.sensors["RightClick"]

    
    if rightClick.positive:
        if gun["KeyFrame"]<6:
            gun["KeyFrame"]+=1
    else:
        if gun["KeyFrame"]>0:
            gun["KeyFrame"]-=1


main()
