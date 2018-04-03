import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go(viz.FULLSCREEN)
viz.clearcolor(viz.SLATE)
import vizinfo

f22 = viz.addChild('f-22 front.osgb',scale=(0.04,0.04,0.04))
pic22 = viz.addTexture('f-22.jpg') 
f22.texture(pic22)

ground = viz.addChild('sky_night.OSGB',scale=(60,60,60))
ground2= viz.addChild('ground_stone.OSGB',scale=(700,700,700))
ground3 = viz.addChild('xinkong2.OSGB',scale=(800,800,800))
ground4= viz.addChild('chongdong2.OSGB',pos=(0,5900,20000),euler=(0,60,0),scale=(150,150,150))

#ground4= viz.addChild('diqiu.OSGB',scale=(50,50,50))
#pic4 = viz.addTexture('4096_earth.jpg')
#ground4.texture(pic4)
#pic4 = viz.addTexture('4096_clouds.jpg')

building=viz.addChild('weilaidushi.osgb',pos=(0,-800,43000),scale=(40,40,40))
building2=viz.addChild('chengshi.osgb',pos=(-1720,-140,3000),scale=(3.5,3.5,3.5))
weixing = viz.addChild('weixing.osgb',pos=(0,7000,0),scale=(0.0001,0.0001,0.0001))

#xingkong diqiu rotation
UPDATE_RATE = 0
SPEED = 2.0
angle = 0
def rotateModel():
	global angle
	angle = angle + (SPEED * viz.elapsed())
	ground3.setEuler([0,0,angle])
#	ground4.setEuler([0,angle,0])
vizact.ontimer(UPDATE_RATE, rotateModel)


f221 = viz.addChild('f-22 FRONT.osgb', pos=(0,0,-3000),scale=(0.04,0.04,0.04))
# Load texture 
pic221 = viz.addTexture('f-222.jpg') 
f221.texture(pic221)
f221.addAction(vizact.moveTo([0,0,-1800],speed=400))
f221.addAction(vizact.moveTo([0,1200,0],speed=300))
f221.addAction(vizact.move(0,0,350,100))

f222 = viz.addChild('f-22 FRONT.osgb', pos=(100,0,-3100),scale=(0.04,0.04,0.04))
f222.texture(pic22)
f222.addAction(vizact.moveTo([150,0,-1800],speed=400))
f222.addAction(vizact.moveTo([320,1200,0],speed=310))
f222.addAction(vizact.move(0,0,350,100))

f223 = viz.addChild('f-22 FRONT.OSGB', pos=(-100,0,-3100),scale=(0.04,0.04,0.04))
f223.texture(pic22)
f223.addAction(vizact.moveTo([-150,0,-1800],speed=400))
f223.addAction(vizact.moveTo([-320,1200,0],speed=310))
f223.addAction(vizact.move(0,0,350,100))

f161 = viz.addChild('f-16.osgb', pos=(-200,0,-3200),scale=(0.05,0.05,0.05))
f161.addAction(vizact.moveTo([-300,0,-1800],speed=390))
f161.addAction(vizact.moveTo([-500,1150,0],speed=290))
f161.addAction(vizact.move(0,0,350,100))

f162 = viz.addChild('f-16.osgb', pos=(200,0,-3200),scale=(0.05,0.05,0.05))
f162.addAction(vizact.moveTo([300,0,-1800],speed=390))
f162.addAction(vizact.moveTo([500,1150,0],speed=290))
f162.addAction(vizact.move(0,0,350,100))

f163 = viz.addChild('f-16.osgb', pos=(-300,0,-3300),scale=(0.05,0.05,0.05))
f163.addAction(vizact.moveTo([-450,0,-1800],speed=390))
f163.addAction(vizact.moveTo([-700,1150,0],speed=290))
f163.addAction(vizact.move(0,0,350,100))

f164 = viz.addChild('f-16.osgb', pos=(300,0,-3300),scale=(0.05,0.05,0.05))
f164.addAction(vizact.moveTo([450,0,-1800],speed=390))
f164.addAction(vizact.moveTo([700,1150,0],speed=290))
f164.addAction(vizact.move(0,0,350,100))

wurenji=viz.addChild('wurenji.osgb', pos=(0,1000,-4000),scale=(0.00005,0.00005,0.00005))
pic2 = viz.addTexture('wurenji.jpg') 
wurenji.texture(pic2)
wurenji.addAction(vizact.moveTo([-10,1200,-1800],speed=490))
wurenji.addAction(vizact.moveTo([-10,1200,0],speed=390))
wurenji.addAction(vizact.move(0,0,350,100))

yuzhoufeichuan6=viz.addChild('yuzhoufeichuan6.3ds', pos=(30800,1500,-32000))

yuzhoufeichuan6.addAction(vizact.moveTo([30800,2000,6000],speed=1000))
yuzhoufeichuan6.addAction(vizact.moveTo([30800,3000,12000],speed=200))
yuzhoufeichuan6.addAction(vizact.move(0,100,200,100))


#viz.MainView.setPosition(0,0,0)
view = viz.MainView
viz.MainView.setPosition(0,50,-4500)

UPDOWN_SPEED = 350
TURN_SPEED = 60

SUPERMOVE_SPEED = 1500
def updatef22():

	#move view forward and backward
	if viz.key.isDown(viz.KEY_UP):
		view.move([0,UPDOWN_SPEED*viz.elapsed(),0],viz.BODY_ORI)
	elif viz.key.isDown(viz.KEY_DOWN):
		view.move([0,-UPDOWN_SPEED*viz.elapsed(),0],viz.BODY_ORI)

	#rotate body of view left and right
	if viz.key.isDown(viz.KEY_RIGHT):
		view.setEuler([TURN_SPEED*viz.elapsed(),0,0],viz.BODY_ORI,viz.REL_PARENT)
	elif viz.key.isDown(viz.KEY_LEFT):
		view.setEuler([-TURN_SPEED*viz.elapsed(),0,0],viz.BODY_ORI,viz.REL_PARENT)

	#set the f22 to view position and body orientation
	f22.setPosition(view.getPosition())
	f22.setEuler(view.getEuler(viz.BODY_ORI))
	f22.setPosition([0,-45,100],viz.REL_LOCAL)
		
	#set the f22 to view SUPERMOVE
	if viz.key.isDown(viz.KEY_CONTROL_L):
	    view.move([0,0,SUPERMOVE_SPEED*viz.elapsed()],viz.BODY_ORI,viz.REL_PARENT)
	if viz.key.isDown(viz.KEY_CONTROL_L):
	    f22.setPosition([0,0,20],viz.REL_LOCAL)
	if viz.key.isDown(viz.KEY_PAGE_UP):
	    view.move([0,0,350*viz.elapsed()],viz.BODY_ORI,viz.REL_PARENT)
	if viz.key.isDown(viz.KEY_PAGE_UP):
		f22.setPosition([0,0,8],viz.REL_LOCAL)
	if viz.key.isDown(viz.KEY_PAGE_DOWN):
	    view.move([0,0,-350*viz.elapsed()],viz.BODY_ORI,viz.REL_PARENT)
	if viz.key.isDown(viz.KEY_PAGE_DOWN):
		f22.setPosition([0,0,-9],viz.REL_LOCAL)


vizact.ontimer(0,updatef22)

def mousemove(e):
	euler = view.getEuler(viz.HEAD_ORI)
	euler[0] += e.dx*0.1
	euler[1] += -e.dy*0.1
	euler[1] = viz.clamp(euler[1],-85.0,85.0)
	view.setEuler(euler,viz.HEAD_ORI)

viz.callback(viz.MOUSE_MOVE_EVENT,mousemove)

viz.mouse(viz.OFF)
viz.mouse.setVisible(False)

vizact.onmousedown(viz.MOUSEBUTTON_LEFT,view.reset,viz.HEAD_ORI)
vizact.onmousedown(viz.MOUSEBUTTON_RIGHT,view.reset, viz.BODY_ORI |viz.HEAD_POS)
vizact.onmousedown(viz.MOUSEBUTTON_RIGHT,updatef22)
