import bge
import mathutils
from mathutils import Vector
from bge import render

moveSpeed=0.2
def main():

    c = bge.logic.getCurrentController()
    player = c.owner
    keyboard=bge.logic.keyboard
    
    jump=c.actuators["Jump"]

    
    wKey=bge.logic.KX_INPUT_ACTIVE==keyboard.events[bge.events.WKEY]
    sKey=bge.logic.KX_INPUT_ACTIVE==keyboard.events[bge.events.SKEY]
    aKey=bge.logic.KX_INPUT_ACTIVE==keyboard.events[bge.events.AKEY]
    dKey=bge.logic.KX_INPUT_ACTIVE==keyboard.events[bge.events.DKEY]
    spaceKey=bge.logic.KX_INPUT_ACTIVE==keyboard.events[bge.events.SPACEKEY]

    if wKey:
        player.applyMovement((0,moveSpeed,0),True)
    elif sKey:
        player.applyMovement((0,-moveSpeed/2,0),True)
    elif aKey:
        player.applyMovement((-moveSpeed/2,0,0),True)
    elif dKey:
        player.applyMovement((moveSpeed/2,0,0),True)
    
    if spaceKey:
        c.activate(jump)
    else:
        c.deactivate(jump)
    
    if player.worldPosition.z<-80:
        bge.logic.restartGame()
        
        
main()
