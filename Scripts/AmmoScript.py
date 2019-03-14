import bge

def main():

    c = bge.logic.getCurrentController()
    gun = c.owner
    
    pickUpAmmo=c.sensors["PickUpAmmo"]
    isAiming=c.sensors["IsAiming"]
    leftClick=c.sensors["LeftClick"]
    fire=c.actuators["Fire"]
    shootSound=c.actuators["shootSound"]
    
    
    ammo=str(gun["Ammo"])
    gun.text="Ammo: "+ammo
    
    if (pickUpAmmo.positive and gun["Ammo"]<=300):
        gun["Ammo"]+=100
        
    if(gun["Ammo"]>300):
        gun["Ammo"]=300
    if(isAiming.positive):
        if (leftClick.positive and gun["Ammo"]>0):
            gun["Ammo"]-=1
            c.activate(fire)
            c.activate(shootSound)
            gun.sendMessage("shotFired")
        else:
            c.deactivate(fire)
    else:
        c.deactivate(fire)  
main()
