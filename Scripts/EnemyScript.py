import bge
import random

c=bge.logic.getCurrentController()
enemy=c.owner
scene=bge.logic.getCurrentScene()
one=scene.objects["one"]
two=scene.objects["two"]
three=scene.objects["three"]
four=scene.objects["four"]

player=scene.objects["Player"]

objectList=[one,two,three,four]

radar=c.sensors["radar"]
collision=c.sensors["collision"]
pathFollow=c.actuators["pathFollow"]



def playerSearch():
    if(enemy["searchTime"]>0):
        enemy["searchTime"]-=1
    if(enemy["searchTime"]<=0):
        choice=random.choice(objectList)
        pathFollow.target=choice
        enemy["searchTime"]=200

def playerFound():
    print("Found")
    pathFollow.target=player
    pathFollow.velocity=10;

def main():
    
    if(radar.positive):
        enemy["searching"]=False
    else:
        enemy["searching"]=True      
    
    if(enemy["searching"]==True):
        playerSearch()
    else:
        playerFound()
        
    c.activate(pathFollow)
    
    if enemy["health"]<=0:
        enemy.sendMessage("enemyNumReduction")   
        enemy.endObject();
    
    if collision.positive:
        enemy.sendMessage("damage")

main()
