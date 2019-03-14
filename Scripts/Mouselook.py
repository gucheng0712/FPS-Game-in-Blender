import mathutils
import bge
def main():

	Sensitivity =  0.001
	Invert = 1
	Capped = False

	controller = bge.logic.getCurrentController()

	obj = controller.owner

	gameScreen = gameWindow()

	move = mouseMove(gameScreen, controller, obj)

	sensitivity =  mouseSen(Sensitivity, obj)

	invert = mousePitch(Invert, obj)
	
	capped = mouseCap(Capped, move, invert, obj)
	
	useMouseLook(controller, capped, move, invert, sensitivity)

	centerCursor(controller, gameScreen)
	

def gameWindow():
	
	width = bge.render.getWindowWidth()
	height = bge.render.getWindowHeight()
	
	return (width, height)


def mouseMove(gameScreen, controller, obj):


	mouse = controller.sensors["MouseLook"]


	width = gameScreen[0]
	height = gameScreen[1]


	x = width/2 - mouse.position[0]
	y = height/2 - mouse.position[1]
	

	if not 'mouseInit' in obj:
		obj['mouseInit'] = True
		x = 0
		y = 0
	
	if not mouse.positive:
		x = 0
		y = 0
	return (x, y)



# define Mouse Sensitivity
def mouseSen(sensitivity, obj):
	
	if 'Adjust' in obj:
		
		if obj['Adjust'] < 0.0:
			obj['Adjust'] = 0.0
		
		sensitivity = obj['Adjust'] * sensitivity
	return sensitivity

def mousePitch(invert, obj):
		
	if 'Invert'in obj:
			
		if obj['Invert'] == True:
			invert = -1
		else:
			invert = 1
	return invert

def mouseCap(capped, move, invert, obj):
	
	if 'Cap' in obj:			
		if obj['Cap'] > 180:
			obj['Cap'] = 180
		if obj['Cap'] < 0:
			obj['Cap'] = 0
		
		camOrient = obj.localOrientation
		
		camZ = [camOrient[0][2], camOrient[1][2], camOrient[2][2]]
		
		vec1 = mathutils.Vector(camZ)
		
		camParent = obj.parent
		
		parentZ = [ 0.0, 0.0, 1.0]
		
		vec2 = mathutils.Vector(parentZ)

		rads = mathutils.Vector.angle(vec2, vec1)

		# convert to degrees (approximate)
		angle = rads * ( 180.00 / 3.14) 

		# get amount to limit mouselook
		capAngle = obj['Cap']
				
		# get mouse up down movement
		moveY = move[1] * invert
		
		if (angle > (90 + capAngle/2) and moveY > 0)   or (angle < (90 - capAngle/2) and moveY < 0)  == True:
			capped = True
	return capped

def useMouseLook(controller, capped, move, invert, sensitivity):

	if capped == True:
		upDown = 0
	else:
		upDown = move[1] * sensitivity * invert 
		

	leftRight = move[0] * sensitivity * invert 
		

	actLeftRight = controller.actuators["LeftRight"]
	actUpDown = controller.actuators["UpDown"]  
	
	actLeftRight.dRot = [ 0.0, 0.0, leftRight]
	actLeftRight.useLocalDRot = False  
	
	actUpDown.dRot = [ upDown, 0.0, 0.0]
	actUpDown.useLocalDRot = True
	
	controller.activate(actLeftRight)
	controller.activate(actUpDown) 
	
def centerCursor(controller, gameScreen):

	width = gameScreen[0]
	height = gameScreen[1]
	
	mouse = controller.sensors["MouseLook"]
	
	pos = mouse.position
		
	if pos != [int(width/2), int(height/2)]:
		
		bge.render.setMousePosition(int(width/2), int(height/2))
		
	else:
		actLeftRight = controller.actuators["LeftRight"]
		actUpDown = controller.actuators["UpDown"]  
		

		controller.deactivate(actLeftRight)
		controller.deactivate(actUpDown) 
main()
