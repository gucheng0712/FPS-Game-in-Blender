import bge


def main():

    cont = bge.logic.getCurrentController()
    own = cont.owner

    timeAmount=(100-own["timer"])
    time=round(timeAmount,1)
    totalTime=str(time)
    
    if time<=0:
        bge.logic.restartGame();
    
    own.text="Time: "+totalTime

main()
