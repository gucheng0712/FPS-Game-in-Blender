import bge


def main():

    c = bge.logic.getCurrentController()
    door = c.owner
    message=c.sensors["EnemyNumReduction"]
    openDoor=c.actuators["OpenDoor"]
    print(door["enemyLeftNum"])
    if message.positive:
        door["enemyLeftNum"]-=1
        if door["enemyLeftNum"]<=0:
            c.activate(openDoor)
main()
