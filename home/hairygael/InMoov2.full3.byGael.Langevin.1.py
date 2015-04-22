#file : InMoov2.full3.byGael.Langevin.1.py

# this script is provided as a basic guide
# most parts can be run by uncommenting them
# InMoov now can be started in modular pieces
import random
leftPort = "COM20"
rightPort = "COM7"
 
i01 = Runtime.createAndStart("i01", "InMoov")
#inmoov = Runtime.createAndStart("alice", "ProgramAB") 
#inmoov.startSession() 
directionServo = Runtime.createAndStart("directionServo","Servo")
forwardServo = Runtime.createAndStart("forwardServo","Servo")
#cleverbot = Runtime.createAndStart("cleverbot","CleverBot")

# starts everything
##i01.startAll(leftPort, rightPort)
directionServo.attach("COM7", 12)
forwardServo.attach("COM7", 13)
# starting parts
i01.startMouthControl(leftPort)
i01.startMouth()
#to tweak the default voice
i01.mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Ryan&txt=")


i01.startHead(leftPort)
##############
# tweaking default settings of jaw
i01.head.jaw.setMinMax(65,90)
#i01.head.jaw.map(0,180,10,35)
i01.mouthControl.setmouth(65,90)
i01.head.jaw.setRest(90)
# tweaking default settings of eyes
i01.head.eyeY.setMinMax(0,180)
i01.head.eyeY.map(0,180,80,100)
i01.head.eyeY.setRest(85)
i01.head.eyeX.setMinMax(0,180)
i01.head.eyeX.map(0,180,70,100)
i01.head.eyeX.setRest(85)
i01.head.neck.setMinMax(0,180)
i01.head.neck.map(0,180,15,155)
i01.head.neck.setRest(70)
i01.head.rothead.setMinMax(0,180)
i01.head.rothead.map(0,180,30,150)
i01.head.rothead.setRest(86)
###################
i01.startEyesTracking(leftPort)
i01.startHeadTracking(leftPort)
##############
i01.startEar()
##############
torso = i01.startTorso("COM20")
# tweaking default torso settings
torso.topStom.setMinMax(0,180)
torso.topStom.map(0,180,67,110)
torso.midStom.setMinMax(0,180)
torso.topStom.map(0,180,60,120)
#torso.lowStom.setMinMax(0,180)
#torso.topStom.setRest(90)
#torso.midStom.setRest(90)
#torso.lowStom.setRest(90)
##############
i01.startLeftHand(leftPort)
# tweaking default settings of left hand
i01.leftHand.thumb.setMinMax(0,180)
i01.leftHand.index.setMinMax(0,180)
i01.leftHand.majeure.setMinMax(0,180)
i01.leftHand.ringFinger.setMinMax(0,180)
i01.leftHand.pinky.setMinMax(0,180)
i01.leftHand.thumb.map(0,180,45,140)
i01.leftHand.index.map(0,180,40,140)
i01.leftHand.majeure.map(0,180,30,176)
i01.leftHand.ringFinger.map(0,180,25,175)
i01.leftHand.pinky.map(0,180,15,112)
################
i01.startLeftArm(leftPort)
#tweak defaults LeftArm
#i01.leftArm.bicep.setMinMax(0,90)
#i01.leftArm.rotate.setMinMax(46,160)
#i01.leftArm.shoulder.setMinMax(30,100)
#i01.leftArm.omoplate.setMinMax(10,75)
################
i01.startRightHand(rightPort,"atmega2560")
# tweaking defaults settings of right hand
i01.rightHand.thumb.setMinMax(0,180)
i01.rightHand.index.setMinMax(0,180)
i01.rightHand.majeure.setMinMax(0,180)
i01.rightHand.ringFinger.setMinMax(0,180)
i01.rightHand.pinky.setMinMax(0,180)
i01.rightHand.thumb.map(0,180,55,135)
i01.rightHand.index.map(0,180,35,140)
i01.rightHand.majeure.map(0,180,8,120)
i01.rightHand.ringFinger.map(0,180,40,125)
i01.rightHand.pinky.map(0,180,10,110)
#################
i01.startRightArm(rightPort)
# tweak default RightArm
#i01.rightArm.bicep.setMinMax(0,90)
#i01.rightArm.rotate.setMinMax(46,160)
#i01.rightArm.shoulder.setMinMax(30,100)
#i01.rightArm.omoplate.setMinMax(10,75)

################

# starting part with a reference, with a reference
# you can interact further
#opencv = i01.startOpenCV()
#opencv.startCapture()
# or you can use i01's reference
#i01.opencv.startCapture()

#i01.headTracking.faceDetect()
#i01.eyesTracking.faceDetect()
#i01.headTracking.pyramidDown()
############################################################
#to tweak the default PID values
i01.eyesTracking.xpid.setPID(20.0,5.0,0.1)
i01.eyesTracking.ypid.setPID(20.0,5.0,0.1)
i01.headTracking.xpid.setPID(12.0,5.0,0.1)
i01.headTracking.ypid.setPID(12.0,5.0,0.1)
############################################################

#i01.startPIR("COM20",30)
 
 
 
#def input():
    #print 'python object is ', msg_clock_pulse
    #pin = msg_i01_right_publishPin.data[0]
    #print 'pin data is ', pin.pin, pin.value
    #if (pin.value == 1):
        #i01.mouth.speak("I was dreaming")
        #powerup()
        #relax()
############################################################
 
helvar = 1
weathervar = 1
 
# play rock paper scissors
inmoov = 0
human = 0
###############################################################

# after a start you may call detach to detach all
# currently attached servos
#i01.detach()
#i01.attach()
 
# auto detaches any attached servos after 120 seconds of inactivity
#i01.autoPowerDownOnInactivity(100)


#i01.speakErrors(false)
# purges any "auto" methods
#i01.purgeAllTasks()
 
# remote control services
# WebGUI - for more information see
# http://myrobotlab.org/service/WebGUI
 
# XMPP - for more information see
# http://myrobotlab.org/service/XMPP
 
# system check - called at anytime
#i01.systemCheck()
 
# take the current position of all attached servos <- FIXME
# and create a new method named "newGesture"
#i01.captureGesture("newGesture")
 
# all ear associations are done python startEar() only starts
# the peer service
# After ear.startListening(), the ear will listen for commands


#############################################################################################
# i01.systemCheck()

#i01.mouth.speakBlocking(cleverbot.chat("hi"))
#i01.mouth.speakBlocking(cleverbot.chat("how are you"))
 
# verbal commands
ear = i01.ear
 
ear.addCommand("rest", "python", "rest")

ear.addCommand("attach head", "i01.head", "attach")
ear.addCommand("disconnect head", "i01.head", "detach")
ear.addCommand("attach eyes", "i01.head.eyeY", "attach")
ear.addCommand("disconnect eyes", "i01.head.eyeY", "detach")
ear.addCommand("attach right hand", "i01.rightHand", "attach")
ear.addCommand("disconnect right hand", "i01.rightHand", "detach")
ear.addCommand("attach left hand", "i01.leftHand", "attach")
ear.addCommand("disconnect left hand", "i01.leftHand", "detach")
ear.addCommand("attach everything", "i01", "attach")
ear.addCommand("disconnect everything", "i01", "detach")
ear.addCommand("attach left arm", "i01.leftArm", "attach")
ear.addCommand("disconnect left arm", "i01.leftArm", "detach")
ear.addCommand("attach right arm", "i01.rightArm", "attach")
ear.addCommand("disconnect right arm", "i01.rightArm", "detach")
ear.addCommand("attach torso", "i01.torso", "attach")
ear.addCommand("disconnect torso", "i01.torso", "detach")
ear.addCommand("attach jaw", "i01.head.jaw", "attach")
ear.addCommand("disconnect jaw", "i01.head.jaw", "detach")
ear.addCommand("attach wheel", "directionServo","forwardServo", "attach")
ear.addCommand("disconnect wheel", "directionServo","forwardServo", "detach")
ear.addCommand("search humans", "python", "trackHumans")
ear.addCommand("quit search", "python", "stopTracking")
ear.addCommand("track", "python", "trackPoint")
ear.addCommand("freeze track", "python", "stopTracking")
 
ear.addCommand("open hand", "python", "handopen")
ear.addCommand("close hand", "python", "handclose")
ear.addCommand("camera on", i01.getName(), "cameraOn")
ear.addCommand("off camera", i01.getName(), "cameraOff")
ear.addCommand("capture gesture", i01.getName(), "captureGesture")
# FIXME - lk tracking setpoint
ear.addCommand("giving", i01.getName(), "giving")
ear.addCommand("fighter", i01.getName(), "fighter")
ear.addCommand("fist hips", "python", "fistHips")
ear.addCommand("look at this", i01.getName(), "lookAtThis")
ear.addCommand("victory", i01.getName(), "victory")
ear.addCommand("arms up", "python", "armsUp")
ear.addCommand("arms front", i01.getName(), "armsFront")
ear.addCommand("da vinci", i01.getName(), "daVinci")
# FIXME -  
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")
ear.addCommand("stop listening", ear.getName(), "stopListening")
 
##sets the servos back to full speed, anywhere in sequence or gestures
ear.addCommand("full speed", "python", "fullspeed")
##sequence1
ear.addCommand("grab the bottle", "python", "grabthebottle")
ear.addCommand("take the glass", "python", "grabtheglass")
ear.addCommand("poor bottle", "python", "poorbottle")
ear.addCommand("give the glass", "python", "givetheglass")
##sequence2
ear.addCommand("take the ball", "python", "takeball")
ear.addCommand("reach the ball", "python", "getball")
ear.addCommand("keep the ball", "python", "keepball")
ear.addCommand("approach the left hand", "python", "approachlefthand")
ear.addCommand("use the left hand", "python", "uselefthand")
ear.addCommand("more", "python", "more")
ear.addCommand("hand down", "python", "handdown")
ear.addCommand("is it a ball", "python", "isitaball")
ear.addCommand("put it down", "python", "putitdown")
ear.addCommand("drop it", "python", "dropit")
ear.addCommand("remove your left arm", "python", "removeleftarm")
ear.addCommand("relax", "python", "relax")
##sequence2 in one command
ear.addCommand("what is it", "python", "studyball")
##extras
ear.addCommand("perfect", "python", "perfect")
ear.addCommand("delicate grab", "python", "delicategrab")
ear.addCommand("release delicate", "python", "releasedelicate")
ear.addCommand("open your right hand", "python", "openrighthand")
ear.addCommand("open your left hand", "python", "openlefthand")
ear.addCommand("close your right hand", "python", "closerighthand")
ear.addCommand("close your left hand", "python", "closelefthand")
ear.addCommand("slowly close your right hand", "python", "slowlycloserighthand")
ear.addCommand("surrender", "python", "surrender")
ear.addCommand("picture on the right side", "python", "picturerightside")
ear.addCommand("picture on the left side", "python", "pictureleftside")
ear.addCommand("picture on both sides", "python", "picturebothside")
ear.addCommand("look on your right side", "python", "lookrightside")
ear.addCommand("look on your left side", "python", "lookleftside")
ear.addCommand("look in the middle", "python", "lookinmiddle")
ear.addCommand("before happy", "python", "beforehappy")
ear.addCommand("happy birthday", "python", "happy")
#ear.addCommand("photo", "python", "photo")
ear.addCommand("about", "python", "about")
ear.addCommand("power down", "python", "power_down")
ear.addCommand("power up", "python", "power_up")
ear.addCommand("servo", "python", "servos")
ear.addCommand("how many fingers do you have", "python", "howmanyfingersdoihave")
ear.addCommand("who's there", "python", "welcome")
ear.addCommand("start gesture", "python", "startkinect")
ear.addCommand("off gesture", "python", "offkinect")
ear.addCommand("cycle gesture one", "python", "cyclegesture1")
ear.addCommand("cycle gesture two", "python", "cyclegesture2")
ear.addCommand("cycle gesture three", "python", "cyclegesture3")
ear.addCommand("show your muscles", "python", "muscle")
ear.addCommand("shake hand", "python", "shakehand")
ear.addCommand("unhappy", "python", "unhappy")
ear.addCommand("take this", "python", "takethis")
ear.addCommand("rock paper scissors", "python", "rockpaperscissors")
ear.addCommand("ready", "python", "ready")
ear.addCommand("rock", "python", "rock")
ear.addCommand("paper", "python", "paper")
ear.addCommand("scissors", "python", "scissors")
ear.addCommand("that was fun", "python", "thatwasfun")
ear.addCommand("guess what", "python", "guesswhat")
ear.addCommand("finger right", "python", "fingerright")
ear.addCommand("finger left", "python", "fingerleft")
ear.addCommand("come here", "python", "comehere")
ear.addCommand("approach", "python", "approach")
ear.addCommand("brake", "python", "brake")
ear.addCommand("made by", "python", "madeby")
ear.addCommand("test", "python", "test1")
ear.addCommand("phone home", "python", "phonehome")
ear.addCommand("how do you feel", "python", "newyork")
ear.addCommand("play your song", "python", "playsong")
ear.addCommand("quit your action", "python", "stopit")
ear.addCommand("carry baby", "python", "carrybaby")
ear.addCommand("system check", "python", "systemcheck")
#ear.addCommand("watch out", "python", "watch out")


ear.addComfirmations("yes","correct","ya","yeah")
ear.addNegations("no","wrong","nope","nah")

ear.startListening("yes | no | very good, thank you | it's okay | no thanks | no thank you | sorry | how do you do | hello | i know | yes let's play again | i have rock | i have paper | i have scissors | look at the people | pause | can i have your attention | good morning | very good | italian hello | alessandro | bye bye | i love you | thanks | thank you | shake hand| what about star wars | where are you from | nice | what is the weather | are you hungry | do you speak hindi | go forward | go backwards | watch out | to the left | to the right | go straight")
 
# set up a message route from the ear --to--> python method "heard"
ear.addListener("recognized", "python", "heard")
#inmoov.addTextListener(i01.mouth)

def carrybaby():
    i01.moveHead(18,111,85,85,5)
    i01.moveArm("left",81,50,45,16)
    i01.moveArm("right",78,44,50,31)
    i01.moveHand("left",180,180,180,180,180,25)
    i01.moveHand("right",111,128,140,151,169,86)
    i01.moveTorso(90,90,90)


def slowlycloserighthand():
    i01.setArmSpeed("left",1.0,1.0,1.0,1.0)
    i01.setArmSpeed("right",1.0,0.8,1.0,1.0)
    i01.setHandSpeed("left",1.0,1.0,1.0,1.0,1.0,1.0)
    i01.setHandSpeed("right",1.0,0.8,0.8,0.7,1.0,1.0)
    i01.setHeadSpeed(0.8,0.8)
    i01.moveHead(30,60)
    i01.moveArm("right",5,80,30,10)
    i01.moveHand("right",176,173,175,175,2,180)

def stopit():
    lookinmiddle()
    sleep(1)
    relax()
    i01.mouth.speak("yes")
    if (data == "pause"):
        i01.mouth.speak("yes")
        
def playsong():
    data = msg_i01_ear_recognized.data[0]
    if (data == "can i have your attention"):
            i01.mouth.speak("ok you have my attention")
            stopit()
            i01.mouth.speak("electro funk inmoov")
            i01.setHeadSpeed(1.0,1.0)
            i01.setArmSpeed("left",1.0,1.0,1.0,1.0)
            i01.setArmSpeed("right",1.0,1.0,1.0,1.0)
            i01.setHandSpeed("left",1.0,1.0,1.0,1.0,1.0,1.0)
            i01.setHandSpeed("right",1.0,1.0,1.0,1.0,1.0,1.0)
            i01.setTorsoSpeed(1.0,1.0,1.0)
           #for x in range(5):
            i01.moveHead(60,90)
            sleep(2)
            i01.moveHead(110,80)
            sleep(2)
            i01.moveHead(60,90)
            sleep(2)
            i01.moveHead(110,80)
            sleep(2)
            i01.moveHead(60,90)
            sleep(2)
            i01.moveHead(110,80)
            sleep(2)
            i01.moveHead(60,90)
            sleep(2)
            i01.moveHead(110,80)
            sleep(2)
            i01.moveHead(60,90)
            sleep(2)
            i01.moveHead(110,80)
            sleep(2)
            i01.moveHead(60,90)
            sleep(2)
            i01.moveHead(110,80)
            sleep(2)
            i01.moveHead(60,90)
            fingerright()
            sleep(3)
            i01.moveHead(110,80)
            fingerleft()
            sleep(3)
            i01.moveHead(60,90)
            fingerright()
            sleep(3)
            i01.moveHead(110,80)
            fingerleft()
            sleep(3)
            i01.moveHead(60,90)
            fingerright()
            sleep(3)
            i01.moveHead(110,80)
            fingerleft()
            sleep(3)
            i01.moveHead(60,90)
            fingerright()
            sleep(3)
            i01.moveHead(110,80)
            fingerleft()
            sleep(3)
            i01.moveTorso(90,90,90)
            fullspeed()
            i01.giving()
            sleep(5)
            i01.armsFront()
            sleep(4)
            fullspeed()
            i01.daVinci()
            sleep(5)
            surrender()
            sleep(6)
            i01.giving()
            sleep(6)
            i01.moveHead(60,90)
            fingerright()
            sleep(3)
            i01.moveHead(110,80)
            fingerleft()
            sleep(3)
            i01.moveHead(60,90)
            fingerright()
            sleep(3)
            i01.moveHead(110,80)
            fingerleft()
            relax()
            i01.moveTorso(90,90,90)
            sleep(3)
            fullspeed()
            sleep(3)
            madeby()
            relax()
            sleep(5)
            i01.detach()


def newyork():
    i01.mouth.speak("robot1")
    i01.setHeadSpeed(1.0,1.0,1.0,1.0,1.0)
    i01.setArmSpeed("left",1.0,1.0,1.0,1.0)
    i01.setArmSpeed("right",1.0,1.0,1.0,1.0)
    i01.setHandSpeed("left",1.0,1.0,1.0,1.0,1.0,1.0)
    i01.setHandSpeed("right",1.0,1.0,1.0,1.0,1.0,1.0)
    i01.setTorsoSpeed(1.0,1.0,1.0)
    i01.moveHead(90,90)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(0.45)
    i01.moveHead(60,107)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(0.45)
    i01.moveHead(60,107)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(0.45)
    i01.moveHead(60,107)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(0.45)
    i01.moveHead(60,107)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(0.45)
    i01.moveHead(90,90)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,140)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(0.45)
    i01.moveHead(60,107)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(0.45)
    i01.moveHead(90,90)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,140)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(0.45)
    i01.moveHead(90,90)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",8,85,28,12)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(0.45)
    i01.moveHead(60,107)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(0.45)
    i01.moveHead(60,107)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",7,82,33,13)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(0.45)
    i01.moveHead(60,107)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(0.45)
    i01.moveHead(60,107)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",6,85,28,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(0.45)
    i01.moveHead(90,90)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,140)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(0.45)
    i01.moveHead(60,107)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",7,87,33,11)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(0.45)
    i01.moveHead(90,90)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,140)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(1.5)
    i01.setHeadSpeed(0.85,0.85)
    i01.setArmSpeed("left",0.90,0.90,0.90,0.90)
    i01.setArmSpeed("right",0.90,0.90,0.90,0.90)
    i01.setHandSpeed("left",1.0,1.0,1.0,1.0,1.0,1.0)
    i01.setHandSpeed("right",1.0,1.0,1.0,1.0,1.0,1.0)
    i01.setTorsoSpeed(1.0,1.0,1.0)
    i01.moveHead(75,97)
    i01.moveArm("left",85,106,25,18)
    i01.moveArm("right",87,107,32,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.mouth.speakBlocking("Start spreading the news")
    i01.setHeadSpeed(0.85,0.85)
    i01.setArmSpeed("left",0.80,0.80,0.80,0.80)
    i01.setArmSpeed("right",0.80,0.80,0.80,0.80)
    i01.setHandSpeed("left",0.80,0.80,0.80,0.80,0.80,0.80)
    i01.setHandSpeed("right",0.80,0.80,0.80,0.80,0.80,0.80)
    i01.setTorsoSpeed(1.0,1.0,1.0)
    i01.moveHead(160,107)
    i01.moveArm("left",5,86,30,10)
    i01.moveArm("right",86,140,83,80)
    i01.moveHand("left",99,140,173,167,130,26)
    i01.moveHand("right",135,6,170,145,168,180)
    i01.moveTorso(90,90,90)
    sleep(0.8)
    i01.mouth.speakBlocking("I am leaving today")
    i01.moveHead(160,68)
    i01.moveArm("left",5,86,30,10)
    i01.moveArm("right",86,140,83,80)
    i01.moveHand("left",99,140,173,167,130,26)
    i01.moveHand("right",135,6,170,145,168,180)
    i01.moveTorso(90,90,90)
    sleep(0.4)
    i01.mouth.speakBlocking("I want to be a part of it")
    i01.moveHead(138,86)
    i01.moveArm("left",80,112,52,34)
    i01.moveArm("right",80,122,59,54)
    i01.moveHand("left",105,76,71,98,76,90)
    i01.moveHand("right",55,0,55,48,142,93)
    i01.moveTorso(90,90,90)
    sleep(0.5)
    i01.mouth.speakBlocking("New York, New York")
    i01.moveHead(138,86)
    i01.moveArm("left",80,112,52,34)
    i01.moveArm("right",80,122,59,54)
    i01.moveHand("left",105,76,71,98,76,90)
    i01.moveHand("right",55,0,55,48,142,93)
    i01.moveTorso(90,90,90)
    sleep(0.4)
    i01.mouth.speakBlocking("If I can make it there")
    i01.moveHead(160,86)
    i01.moveArm("left",80,128,71,62)
    i01.moveArm("right",80,132,69,80)
    i01.moveHand("left",45,40,30,25,35,90)
    i01.moveHand("right",55,0,55,48,142,72)
    i01.moveTorso(90,90,90)
    sleep(0.2)
    i01.mouth.speakBlocking("I'll make it anywhere")
    i01.moveHead(160,86)
    i01.moveArm("left",80,128,71,62)
    i01.moveArm("right",80,132,69,80)
    i01.moveHand("left",45,40,30,25,35,90)
    i01.moveHand("right",55,0,55,48,142,72)
    i01.moveTorso(90,90,90)
    sleep(0.2)
    i01.moveHead(136,66)
    i01.moveArm("left",5,138,30,77)
    i01.moveArm("right",5,134,59,75)
    i01.moveHand("left",127,101,122,129,123,131)
    i01.moveHand("right",55,2,50,48,30,90)
    i01.moveTorso(90,90,90)
    sleep(0.2)
    i01.mouth.speakBlocking("It's up to you")
    i01.moveHead(160,86)
    i01.moveArm("left",46,131,30,80)
    i01.moveArm("right",71,145,36,80)
    i01.moveHand("left",45,40,30,96,107,90)
    i01.moveHand("right",55,4,50,49,114,90)
    i01.moveTorso(90,90,90)
    sleep(0.2)
    i01.mouth.speakBlocking("New York, New York")
    sleep(2)
    relax()
    
def phonehome():
    relax()
    i01.setHeadSpeed(1.0,1.0,1.0,1.0,1.0)
    i01.setArmSpeed("left",1.0,1.0,1.0,1.0)
    i01.setArmSpeed("right",1.0,1.0,1.0,1.0)
    i01.setHandSpeed("left",1.0,1.0,1.0,1.0,1.0,1.0)
    i01.setHandSpeed("right",1.0,1.0,1.0,1.0,1.0,1.0)
    i01.setTorsoSpeed(1.0,1.0,1.0)
    i01.moveHead(160,68)
    i01.moveArm("left",5,86,30,20)
    i01.moveArm("right",86,140,83,80)
    i01.moveHand("left",99,140,173,167,130,26)
    i01.moveHand("right",135,6,170,145,168,180)
    i01.moveTorso(25,80,90)
    sleep(2)
    i01.mouth.speakBlocking("E,T phone the big home of the inmoov nation")
    sleep(0.2)
    relax()
    
def test1():
    rest()
    i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(0.9, 0.9)
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(50,110)
    i01.moveArm("left",88,90,70,23)
    i01.moveArm("right",73,90,70,27)
    i01.moveHand("left",2,2,2,2,2,90)
    i01.moveHand("right",2,2,2,2,2,90)
    i01.moveTorso(90,90,90)
    sleep(2)


def madeby():
    relax()
    sleep(1)
    i01.moveHead(80,86)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",45,40,30,25,35,90)
    i01.moveHand("right",55,2,50,48,30,90)
    i01.moveTorso(90,90,90)
    sleep(3)
    #i01.mouth.speakBlocking("hello")
    i01.mouth.speakBlocking("bonjour")
    i01.moveHead(80,98)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",45,40,30,25,35,90)
    i01.moveHand("right",55,2,50,48,30,90)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.moveHead(90,89)
    i01.moveArm("left",42,104,30,10)
    i01.moveArm("right",33,116,30,10)
    i01.moveHand("left",45,40,30,25,35,120)
    i01.moveHand("right",55,2,50,48,30,40)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.moveHead(80,98)
    i01.moveArm("left",5,99,30,16)
    i01.moveArm("right",5,94,30,16)
    i01.moveHand("left",120,116,110,115,98,73)
    i01.moveHand("right",114,146,125,113,117,109)
    i01.moveTorso(90,90,90)
    #i01.mouth.speakBlocking("my name is inmoov")
    i01.mouth.speakBlocking("je m'appelle inmouv")
    i01.moveHead(68,90)
    i01.moveArm("left",5,99,30,16)
    i01.moveArm("right",85,102,38,16)
    i01.moveHand("left",120,116,110,115,98,73)
    i01.moveHand("right",114,146,161,132,168,19)
    i01.moveTorso(90,90,90)
    sleep(0.5)
    ##i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    ##i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    ##i01.setHeadSpeed(1.0, 0.90)
    ##i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(87,94)
    i01.moveArm("left",5,99,36,16)
    i01.moveArm("right",81,105,42,16)
    i01.moveHand("left",120,116,110,115,98,50)
    i01.moveHand("right",114,118,131,132,168,19)
    i01.moveTorso(90,90,90)
    sleep(1)
    #i01.mouth.speakBlocking("I am created by gael langevin")
    i01.mouth.speakBlocking("j'ai ete creer par gael langevin")
    i01.setHandSpeed("left", 0.90, 0.90, 0.90, 0.90, 0.90, 0.95)
    i01.setHandSpeed("right", 0.90, 0.90, 0.90, 0.90, 0.90, 0.95)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 0.90, 1.0, 1.0, 1.0)
    ##i01.setHeadSpeed(1.0, 0.90)
    ##i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(105,94)
    i01.moveArm("left",5,99,36,16)
    i01.moveArm("right",81,105,42,16)
    i01.moveHand("left",120,116,110,115,98,50)
    i01.moveHand("right",114,118,131,132,168,19)
    i01.moveTorso(90,90,90)
    sleep(0.2)
    i01.moveHead(80,86)
    i01.moveArm("left",5,96,25,10)
    i01.moveArm("right",5,94,26,10)
    i01.moveHand("left",110,62,56,88,81,18)
    i01.moveHand("right",78,88,101,95,81,137)
    i01.moveTorso(90,90,90)
    sleep(0.2)
    i01.moveHead(75,97)
    i01.moveArm("left",85,106,25,18)
    i01.moveArm("right",87,107,32,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.moveTorso(90,90,90)
    #i01.mouth.speakBlocking("who is a french sculptor, designer")
    i01.mouth.speakBlocking("qui est un sculpteur, designer francais")
    sleep(0.5)
    i01.moveHead(80,86)
    i01.moveArm("left",5,96,25,10)
    i01.moveArm("right",5,94,26,10)
    i01.moveHand("left",110,62,56,88,81,18)
    i01.moveHand("right",78,88,101,95,81,137)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.moveHead(75,97)
    i01.moveArm("left",6,91,22,14)
    i01.moveArm("right",87,107,32,18)
    i01.moveHand("left",110,62,56,88,81,0)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.moveTorso(90,90,90)
    i01.mouth.speakBlocking("my software is being developped by myrobtlab dot org")
    i01.mouth.speakBlocking("mon logiciel est developpe par myrobotlab point org")
    sleep(1)
    i01.moveHead(20,69)
    i01.moveArm("left",6,91,22,14)
    i01.moveArm("right",87,107,32,21)
    i01.moveHand("left",110,62,56,88,81,0)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.moveTorso(90,90,90)
    #i01.mouth.speakBlocking("I am totally build with 3 D printed parts")
    i01.mouth.speakBlocking("je suis entierement imprimer en 3 D")
    i01.moveHead(75,97)
    i01.moveArm("left",85,106,25,18)
    i01.moveArm("right",87,107,32,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.moveHead(33,110)
    i01.moveArm("left",85,104,25,18)
    i01.moveArm("right",87,41,47,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",111,75,117,125,111,143)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.moveHead(62,102)
    i01.moveArm("left",85,104,25,18)
    i01.moveArm("right",87,41,47,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",111,75,117,125,111,143)
    i01.moveTorso(90,90,90)
    #i01.mouth.speakBlocking("which means all my parts")
    i01.mouth.speakBlocking("ce qui veut dire que toutes mes pieces,")
    i01.moveHead(79,88)
    i01.moveArm("left",85,104,25,18)
    i01.moveArm("right",87,59,46,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",59,75,117,125,111,113)
    i01.moveTorso(90,90,90)
    #i01.mouth.speakBlocking("are made on a home 3 D printer")
    i01.mouth.speakBlocking("sont fabriquer sur une petite imprimante familiale")
    sleep(1)
    i01.moveHead(40,84)
    i01.moveArm("left",85,72,38,18)
    i01.moveArm("right",87,64,47,18)
    i01.moveHand("left",124,97,66,120,130,35)
    i01.moveHand("right",59,75,117,125,111,113)
    i01.moveTorso(90,90,90)
    #i01.mouth.speakBlocking("each parts are design to fit 12 centimeter cube build area")
    i01.mouth.speakBlocking("chaque piece est concu dans un format de 12 centimetre cube,")
    sleep(1)
    i01.moveHead(97,80)
    i01.moveArm("left",85,79,39,14)
    i01.moveArm("right",87,76,42,12)
    i01.moveHand("left",124,97,66,120,130,35)
    i01.moveHand("right",59,75,117,125,111,113)
    i01.moveTorso(90,90,90)
    sleep(0.5)
    i01.moveHead(75,97)
    i01.moveArm("left",85,106,25,18)
    i01.moveArm("right",87,107,32,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.moveTorso(90,90,90)
    sleep(1)
    #i01.mouth.speakBlocking("so anyone can reproduce me")
    i01.mouth.speakBlocking("de facon a ce que tout le monde puisse me reproduire")
    fullspeed()
    i01.moveHead(80,98)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",45,40,30,25,35,90)
    i01.moveHand("right",55,2,50,48,30,90)
    i01.moveTorso(90,90,90)
    sleep(1)
    #i01.mouth.speakBlocking("cool, don't you think")
    i01.mouth.speakBlocking("c'est cool, vous ne trouvez pas")
    sleep(1)
    #i01.mouth.speakBlocking("thank you for listening")
    i01.mouth.speakBlocking("merci de votre attention")
    i01.moveHead(116,80)
    i01.moveArm("left",85,93,42,16)
    i01.moveArm("right",87,93,37,18)
    i01.moveHand("left",124,82,65,81,41,143)
    i01.moveHand("right",59,53,89,61,36,21)
    i01.moveTorso(90,90,90)
    sleep(0.2)
    relax()
    


def brake():
    i01.moveHead(80,86)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",45,40,30,25,35,90)
    i01.moveHand("right",55,2,50,48,30,90)
    i01.moveTorso(90,90,90)
    sleep(3)
    i01.moveHead(20,86)
    i01.moveArm("left",21,92,49,22)
    i01.moveArm("right",38,91,43,10)
    i01.moveHand("left",45,40,30,25,35,90)
    i01.moveHand("right",89,127,123,48,30,90)
    i01.moveTorso(90,90,90)
    sleep(3)
    i01.moveHead(20,106)
    i01.moveArm("left",75,69,49,22)
    i01.moveArm("right",38,91,43,10)
    i01.moveHand("left",120,80,74,106,35,90)
    i01.moveHand("right",89,127,123,48,30,90)
    i01.moveTorso(90,90,90)
    sleep(3)
    i01.moveHead(20,93)
    i01.moveArm("left",75,69,49,22)
    i01.moveArm("right",71,66,60,10)
    i01.moveHand("left",120,80,74,106,35,90)
    i01.moveHand("right",89,127,123,48,30,146)
    i01.moveTorso(90,90,90)
    sleep(3)
    i01.moveHead(110,93)
    i01.moveArm("left",75,69,49,22)
    i01.moveArm("right",71,66,60,10)
    i01.moveHand("left",120,80,74,106,35,90)
    i01.moveHand("right",89,127,123,48,30,146)
    i01.moveTorso(90,90,90)
    sleep(3)
    i01.mouth.speakBlocking("Should I brake that")
    i01.moveHead(110,93)
    i01.moveArm("left",90,69,84,22)
    i01.moveArm("right",71,66,60,10)
    i01.moveHand("left",138,134,168,168,120,90)
    i01.moveHand("right",124,142,151,48,30,146)
    i01.moveTorso(90,90,90)

def approach():
    i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(1.0, 0.90)
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(92,80)
    i01.moveArm("left",7,76,24,16)
    i01.moveArm("right",7,79,24,15)
    i01.moveHand("left",49,43,30,28,40,80)
    i01.moveHand("right",55,7,55,48,43,108)
    i01.moveTorso(90,90,90)
    sleep(3)
    i01.moveHead(92,80)
    i01.moveArm("left",5,52,57,13)
    i01.moveArm("right",10,45,59,13)
    i01.moveHand("left",134,138,176,175,130,0)
    i01.moveHand("right",119,150,163,134,151,180)
    i01.moveTorso(90,90,90)
    sleep(3)
    i01.moveHead(92,80)
    i01.moveArm("left",14,63,71,21)
    i01.moveArm("right",14,55,77,21)
    i01.moveHand("left",49,43,30,28,40,171)
    i01.moveHand("right",55,7,55,48,43,12)
    i01.moveTorso(90,90,90)
    sleep(3)
    i01.moveHead(92,80)
    i01.moveArm("left",5,52,57,13)
    i01.moveArm("right",10,45,59,13)
    i01.moveHand("left",134,138,176,175,130,0)
    i01.moveHand("right",119,150,163,134,151,180)
    i01.moveTorso(90,90,90)
    i01.mouth.speakBlocking("please approach")
    relax()


def fingerright():
    i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setHandSpeed("right", 1.0, 0.85, 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 0.90, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(1.0, 0.90)
    i01.setTorsoSpeed(0.9, 0.5, 1.0)
    i01.moveHead(80,86)
    i01.moveArm("left",5,94,20,10)
    i01.moveArm("right",7,78,92,10)
    i01.moveHand("left",180,180,180,180,180,90)
    i01.moveHand("right",180,2,175,160,165,180)
    i01.moveTorso(60,70,90)

def fingerleft():
    i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setHandSpeed("right", 1.0, 0.85, 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 0.90, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(1.0, 0.90)
    i01.setTorsoSpeed(0.9, 0.5, 1.0)
    i01.moveHead(80,86)
    i01.moveArm("left",7,78,92,10)
    i01.moveArm("right",5,94,20,10)
    i01.moveHand("left",180,2,175,160,165,90)
    i01.moveHand("right",180,180,180,180,180,90)
    i01.moveTorso(120,110,90)


def comehere():
    fullspeed()
    relax()
##look around
    i01.setHeadSpeed(0.80, 0.80, 0.90, 0.90, 1.0)
    i01.moveHead(80,66,7,85,52)
    sleep(3)
    i01.setHeadSpeed(0.80, 0.80, 0.90, 0.90, 1.0)
    i01.moveHead(80,110,175,85,52)
    sleep(3)
##raise arm point finger
    i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setHandSpeed("right", 1.0, 0.85, 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 0.90, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(1.0, 0.90)
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(80,86,85,85,52)
    i01.moveArm("left",5,94,30,10)
    i01.moveArm("right",7,74,92,10)
    i01.moveHand("left",180,180,180,180,180,90)
    i01.moveHand("right",180,2,175,160,165,180)
    i01.moveTorso(90,90,90)
    sleep(4.5)
##move finger
    i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(1.0, 1.0)
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(80,86)
    i01.moveArm("left",5,94,30,10)
    i01.moveArm("right",48,74,92,10)
    i01.moveHand("left",180,180,180,180,180,90)
    i01.moveHand("right",180,2,175,160,165,20)
    i01.moveTorso(90,90,90)
    sleep(2)
    i01.setHeadSpeed(0.80, 0.80)
    i01.moveHead(80,80)
    i01.moveHand("right",180,164,175,160,165,20)
    sleep(1)
    i01.moveHead(80,80)
    i01.moveHand("right",180,2,175,160,165,20)
    sleep(1)
    i01.moveHead(118,80)
    i01.moveHand("right",180,164,175,160,165,20)
    sleep(1)
    i01.mouth.speak("come closer")
    i01.moveHead(60,80)
    i01.moveHand("right",180,2,175,160,165,20)
    sleep(1)
    i01.moveHead(118,80)
    i01.moveHand("right",180,164,175,160,165,20)
    sleep(1)
    i01.moveHead(60,80)
    i01.moveArm("right",90,65,10,25)
    sleep(3)
    fullspeed()
    rest()
    sleep(0.3)
    relax()
    sleep(3)
    fullspeed()
        

def guesswhat():
    i01.mouth.speak("I'm not really a human man")
    i01.mouth.speak("but I use Old spice body wash and deodorant together")
    i01.mouth.speak("and now I'm really cool")


def rockpaperscissors():
    fullspeed()
    i01.mouth.speak("lets play first to 3 points win")
    sleep(4)
    rockpaperscissors2()

def rockpaperscissors2():
    x = (random.randint(1, 3))
    if x == 1:
        ready()
        sleep(2)
        rock()
        sleep(2)
        data = msg_i01_ear_recognized.data[0]
        if (data == "i have rock"):
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("zero zero")
            if x == 2:
                i01.mouth.speak("no no")
            if x == 3:
                i01.mouth.speak("no points")
            sleep(1)
        if (data == "i have paper"):
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("paper beats rock")
            if x == 2:
                i01.mouth.speak("your point")
            if x == 3:
                i01.mouth.speak("you got this one")
            global human
            human += 1
            sleep(1)
        if (data == "i have scissors"):
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("1 point for me")
            if x == 2:
                i01.mouth.speak("going fine")
            if x == 3:
                i01.mouth.speak("rock beats scissors")
            global inmoov
            inmoov += 1
            sleep(1)
       
           
    if x == 2:
        ready()
        sleep(2)
        paper()
        sleep(2)
        data = msg_i01_ear_recognized.data[0]
        if (data == "i have rock"):
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("1 point")
            if x == 2:
                i01.mouth.speak("paper beats rock")
            if x == 3:
                i01.mouth.speak("my point")
            global inmoov
            inmoov += 1
            sleep(1)
        if (data == "i have paper"):
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("no points")
            if x == 2:
                i01.mouth.speak("ok lets try again")
                sleep(2)
            if x == 3:
                i01.mouth.speak("again")
            sleep(1)
        if (data == "i have scissors"):
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("oh no you get 1 point")
            if x == 2:
                i01.mouth.speak("this is not good for me")
            if x == 3:
                i01.mouth.speak("your point")
            global human
            human += 1
            sleep(1)
        
    if x == 3:
        ready()
        sleep(2)
        scissors()
        sleep(2)
        data = msg_i01_ear_recognized.data[0]
        if (data == "i have rock"):
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("oh no")
            if x == 2:
                i01.mouth.speak("rock beats scissors")
            if x == 3:
                i01.mouth.speak("i feel generous today")
            global human
            human += 1
            sleep(1)
        if (data == "i have paper"):
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("i've got you")
            if x == 2:
                i01.mouth.speak("my point")
            if x == 3:
                i01.mouth.speak("good")
            global inmoov
            inmoov += 1
            sleep(1)
        if (data == "i have scissors"):
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("no no")
            if x == 2:
                i01.mouth.speak("zero zero")
            if x == 3:
                i01.mouth.speak("no points")
            sleep(1)
    if inmoov == 3:
        stoprockpaperscissors()
        sleep(1)
    elif human == 3:                       # changed from if to  elif              
        stoprockpaperscissors()
        sleep(1)
    elif inmoov <= 2:                      # changed from if to  elif 
        rockpaperscissors2()
    elif human <= 2:                       # changed from if to  elif 
        rockpaperscissors2()   
  
def stoprockpaperscissors():
    rest()
    sleep(5)
    if inmoov < human:
        i01.mouth.speak("congratulations you won with" + str(human - inmoov) + "points")
        sleep(3)
        i01.mouth.speak(str(human) + "points to you and" + str(inmoov) + "points to me")
    elif inmoov > human:                                                                                                         # changed from if to  elif
        i01.mouth.speak("yes yes i won with" + str(inmoov - human) + "points")
        sleep(3)
        i01.mouth.speak("i've got " + str(inmoov) + "points and you got" + str(human) + "points")
    elif inmoov == human:                                                                                                          # changed from if to  elif
        i01.mouth.speak("none of us won we both got" + str(inmoov) + "points")
    global inmoov
    inmoov = 0
    global human
    human = 0
    i01.mouth.speak("that was fun")
    sleep(2)
    i01.mouth.speak("do you want to play again")
    sleep(10)
    data = msg_i01_ear_recognized.data[0]
    if (data == "yes let's play again"):
        rockpaperscissors2()
    elif (data == "yes"):                                                                              # changed from if to  elif
        rockpaperscissors2()
    elif (data == "no thanks"):                                                                  # changed from if to  elif
        i01.mouth.speak("maybe some other time")
        sleep(4)
        power_down()
    elif (data == "no thank you"):                                                           # changed from if to  elif
        i01.mouth.speak("maybe some other time")
        sleep(4)
        power_down()
    ##i01.mouth.speak("ok i'll find something else to do then")
    ##lookaroundyou()
    

def ready():
    i01.mouth.speak("ready")
    i01.mouth.speak("go")
    i01.moveHead(90,90)
    i01.moveArm("left",65,90,75,10)
    i01.moveArm("right",20,80,25,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    
    

def rock():
    fullspeed()
    i01.moveHead(90,90)
    i01.moveArm("left",70,90,80,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.5)
    i01.setHeadSpeed(.8,.8)
    i01.moveHead(60,107)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    
    sleep(.5)
    i01.moveArm("left",80,90,85,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.5)
    i01.setHeadSpeed(.8,.8)
    i01.moveHead(60,107)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    
    sleep(.5)
    i01.moveArm("left",90,90,90,10)
    i01.moveArm("right",20,85,10,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.5)
    i01.setHeadSpeed(.8,.8)
    i01.moveHead(60,107)
    i01.moveArm("left",45,90,75,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,80)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.3)
    x = (random.randint(1, 2))
    if x == 1:
        i01.mouth.speakBlocking("i have rock what do you have")
    if x == 2:
        i01.mouth.speakBlocking("what do you have")

def paper():
    fullspeed()
    i01.moveHead(90,90)
    i01.moveArm("left",70,90,80,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.5)
    i01.setHeadSpeed(.8,.8)
    i01.moveHead(60,107)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    
    sleep(.5)
    i01.moveArm("left",80,90,85,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.5)
    i01.setHeadSpeed(.8,.8)
    i01.moveHead(60,107)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    
    sleep(.5)
    i01.moveArm("left",90,90,90,10)
    i01.moveArm("right",20,85,10,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.5)
    i01.setHeadSpeed(.8,.8)
    i01.moveHead(90,90)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",0,0,0,0,0,165)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.3)
    x = (random.randint(1, 2))
    if x == 1:
        i01.mouth.speakBlocking("i have paper what do you have")
    if x == 2:
        i01.mouth.speakBlocking("what do you have")

def scissors():
    fullspeed()
    i01.moveHead(90,90)
    i01.moveArm("left",70,90,80,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.5)
    i01.setHeadSpeed(.8,.8)
    i01.moveHead(60,107)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    
    sleep(.5)
    i01.moveArm("left",80,90,85,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.5)
    i01.setHeadSpeed(.8,.8)
    i01.moveHead(60,107)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    
    sleep(.5)
    i01.moveArm("left",90,90,90,10)
    i01.moveArm("right",20,85,10,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.5)
    i01.moveHead(90,90)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",50,0,0,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.3)
    x = (random.randint(1, 2))
    if x == 1:
        i01.mouth.speakBlocking("i have scissors what do you have")
    if x == 2:
        i01.mouth.speakBlocking("what do you have")

def lookaroundyou(): 
    i01.setHeadSpeed(0.8, 0.8, 0.6, 0.6, 1.0)
    for y in range(0, 3):
        data = msg_i01_ear_recognized.data[0]
        if (data == "can i have your attention"):
            i01.mouth.speak("ok you have my attention")
            stopit()
            x = (random.randint(1, 6))
            if x == 1:
                i01.head.neck.moveTo(90)
                eyeslooking()
            if x == 2:
                i01.head.rothead.moveTo(80)
                eyeslooking()
            if x == 3:
                headdown()
                eyeslooking()
            if x == 4:
                headupp()
                eyeslooking()
            if x == 5:
                headright()
                eyeslooking()
            if x == 6:
                headleft()
                eyeslooking()
            sleep(1)
        x = (random.randint(1, 4))
        if x == 1:
            i01.mouth.speak("looking nice")
        if x == 2:
            i01.mouth.speak("i like it here")
        if x == 3:
            i01.mouth.speak("time just flies away")
        if x == 4:
            i01.mouth.speak("ok let's do something")
            sleep(2)
            x = (random.randint(1, 4))
            if x == 1:
                comehere()
            if x == 2:
                perfect()
                sleep(2)
                rest()
                sleep(1)
                relax()
            if x == 3:
                rest()
            if x == 4:
                fingerleft()
                sleep(3)
                relax()
 
def eyeslooking():
    for y in range(0, 5):
        data = msg_i01_ear_recognized.data[0]
        if (data == "can i have your attention"):
            i01.mouth.speak("ok you have my attention")
            stopit()
        if (data == "inmoov"):
            stopit()
        x = (random.randint(1, 6))
        if x == 1:
            i01.head.eyeX.moveTo(80)
        if x == 2:
            i01.head.eyeY.moveTo(80)
        if x == 3:
            eyesdown()
        if x == 4:
            eyesupp()
        if x == 5:
            eyesleft()
        if x == 6:
            eyesright()
        sleep(0.5)
    eyesfront()        

def thatwasfun():
  i01.mouth.speak("that was fun")
  i01.moveHead(90,90)
  i01.moveArm("left",85,106,25,18)
  i01.moveArm("right",87,107,32,18)
  i01.moveHand("left",110,62,56,88,81,145)
  i01.moveHand("right",78,88,101,95,81,27)
  i01.moveTorso(90,90,90)
  relax()

###############################################################################
  
def heard(data):
    data = msg_i01_ear_recognized.data[0]

    if (data == "it's okay"):
        i01.mouth.speak("good")

    if (data == "very good, thank you"):
        i01.mouth.speak("okay, good")
       

    if (data == "look at the people"):
        i01.setHeadSpeed(0.8, 0.8)
        for y in range(0, 10):
            x = (random.randint(1, 5))
            if x == 1:
                fullspeed()
                i01.head.neck.moveTo(90)
                eyeslooking()
                sleep(2)
                trackHumans()
                sleep(10)
                stopTracking()
            if x == 2:
                fullspeed()
                i01.head.rothead.moveTo(80)
                eyeslooking()
                sleep(2)
                trackHumans()
                sleep(10)
                stopTracking()
            if x == 3:
                fullspeed()
                headdown()
                sleep(1)
                trackHumans()
                sleep(10)
                stopTracking()
            if x == 4:
                fullspeed()
                lookrightside()
                sleep(2)
                trackHumans()
                sleep(10)
                stopTracking()
            if x == 5:
                fullspeed()
                lookleftside()
                sleep(2)
                trackHumans()
                sleep(10)
                stopTracking()
        sleep(1)
        lookinmiddle()
        sleep(3)
        i01.mouth.speak("nice to meet you all")
 
    if (data == "take a look around"):
        lookaroundyou()

    if (data == "good morning"):
        i01.mouth.speak("good morning")
        x = (random.randint(1, 4))
        if x == 1:
            i01.mouth.speak("i hope you had a good night sleep")
        if x == 2:
            i01.mouth.speak("nice to see you again")
        if x == 3:
            i01.mouth.speak("this is going to be a good day")   
 
    if (data == "very good"):
        i01.mouth.speak("thanks")
        
    if (data =="alessandro"):
        fullspeed()
        i01.setHeadSpeed(0.85, 0.80, 0.90, 0.90, 1.0)
        i01.moveHead(60,40,7,85,52)
        sleep(1)
        i01.moveHead(80,40,7,85,52)
        sleep(2)
        i01.setHeadSpeed(0.92, 0.80, 0.90, 0.90, 1.0)
        i01.moveHead(100,40,7,85,52)
        sleep(0.4)
        i01.moveArm("left",85,106,25,18)
        i01.moveArm("right",87,107,32,18)
        i01.moveHand("left",110,62,56,88,81,145)
        i01.moveHand("right",78,88,101,95,81,27)
        i01.moveTorso(90,90,90)
        i01.moveHead(80,40,7,85,52)
        i01.mouth.speakBlocking("alessandro, dove e la pizza")
        sleep(1)
        i01.moveHead(60,90,80,90,52)
        sleep(0.8)
        relax()
   

    if (data =="italian hello"):
        italianhello()

    if (data =="are you hungry"):
        fullspeed()
        i01.setHeadSpeed(0.85, 0.80, 0.90, 0.90, 1.0)
        i01.moveHead(60,40,7,85,52)
        sleep(1)
        i01.moveHead(80,40,7,85,52)
        sleep(2)
        i01.setHeadSpeed(0.92, 0.80, 0.90, 0.90, 1.0)
        i01.moveHead(100,40,7,85,52)
        sleep(0.4)
        i01.moveArm("left",85,106,25,18)
        i01.moveArm("right",87,107,32,18)
        i01.moveHand("left",110,62,56,88,81,145)
        i01.moveHand("right",78,88,101,95,81,27)
        i01.moveTorso(90,90,90)
        i01.moveHead(80,40,7,85,52)
        i01.mouth.speakBlocking("yes, i want some paneer tikka")
        sleep(1)
        i01.moveHead(60,90,80,90,52)
        sleep(0.8)
        relax()    

    if (data =="do you speak hindi"):
        i01.mouth.speak("yes, i can speak any language")
        i01.moveHead(116,80)
        i01.moveArm("left",85,93,42,16)
        i01.moveArm("right",87,93,37,18)
        i01.moveHand("left",124,82,65,81,41,143)
        i01.moveHand("right",59,53,89,61,36,21)
        i01.moveTorso(90,90,90)
        sleep(0.2)
        sleep(1)
        relax()
    

    if (data == "where are you from"):
        phonehome()
            
    if (data == "what about star wars"):
        x = (random.randint(1, 2))
        if x == 1:
            fullspeed()
            i01.moveHead(130,149,87,80,100)
            i01.mouth.speak("R2D2")
            sleep(1)
            i01.moveHead(155,31,87,80,100)
            sleep(1)
            i01.moveHead(130,31,87,80,100)
            sleep(1)
            i01.moveHead(90,90,87,80,100)
            sleep(0.5)
            i01.moveHead(90,90,87,80,70)
            sleep(1)
            relax()
        if x == 2:
            fullspeed()
            i01.mouth.speak("Hello sir, I am C3po unicyborg relations")
            i01.moveHead(138,80)
            i01.moveArm("left",79,42,23,41)
            i01.moveArm("right",71,40,14,39)
            i01.moveHand("left",180,180,180,180,180,47)
            i01.moveHand("right",99,130,152,154,145,180)
            i01.moveTorso(90,90,90)
            sleep(1)
            i01.moveHead(116,80)
            i01.moveArm("left",85,93,42,16)
            i01.moveArm("right",87,93,37,18)
            i01.moveHand("left",124,82,65,81,41,143)
            i01.moveHand("right",59,53,89,61,36,21)
            i01.moveTorso(90,90,90)
            sleep(1)
            relax()

    if (data == "i know"):
        x = (random.randint(1, 3))
        if x == 1:
            i01.mouth.speak("yes, me too")
        if x == 2:
            i01.mouth.speak("I do too")
        if x == 3:
            i01.mouth.speak("sorry about that")
            
    if (data == "sorry"):
        x = (random.randint(1, 3))
        if x == 1:
            i01.mouth.speak("no problems")
        if x == 2:
            i01.mouth.speak("it doesn't matter")
        if x == 3:
            i01.mouth.speak("it's okay")

    if (data == "nice"):
        x = (random.randint(1, 3))
        if x == 1:
            i01.mouth.speak("I know")
        if x == 2:
            i01.mouth.speak("yes, indeed")
        if x == 3:
            i01.mouth.speak("you are damn right")

    if (data == "hello"):
        hello()
        relax()    
 
    if (data == "bye bye"):
        i01.mouth.speak("see you soon")
        global helvar
        helvar = 1
        x = (random.randint(1, 2))
        if x == 1:
            i01.mouth.speak("i'm looking forward to see you again")
        if x == 2:
            i01.mouth.speak("goodbye")

    if (data == "thank you"):
        x = (random.randint(1, 3))
        if x == 1:
            i01.mouth.speak("you are welcome")
        if x == 2:
            i01.mouth.speak("my pleasure")
        if x == 3:
            i01.mouth.speak("it's okay")

    if (data == "thanks"):
        x = (random.randint(1, 2))
        if x == 1:
            i01.mouth.speak("it's okay")
        if x == 2:
            i01.mouth.speak("sure")

    if (data == "go forward"):
        forwardServo.moveTo(10)
        
    if (data == "go backwards"):
          forwardServo.moveTo(170)
          
    if (data == "watch out"):
          forwardServo.moveTo(93)
          
    if (data == "to the left"):
          directionServo.moveTo(127)
          
    if (data == "to the right"):
          directionServo.moveTo(40)
          
    if (data == "go straight"):
          directionServo.moveTo(83)
          
    #elif (data == "disconnect wheel"):
          #directionServo.detach()
          #forwardServo.detach()
    #elif (data == "attach wheel"):
          #directionServo.attach()
          #forwardServo.attach()       
 
    if (data == "how do you do"):
        if helvar <= 2:    
            i01.mouth.speak("I'm fine thank you")
            global helvar
            helvar += 1
        elif helvar == 3:
            i01.mouth.speak("you have already said that at least twice")
            i01.moveArm("left",43,88,22,10)
            i01.moveArm("right",20,90,30,10)
            i01.moveHand("left",0,0,0,0,0,119)
            i01.moveHand("right",0,0,0,0,0,119)
            sleep(2)
            relax()
            global helvar
            helvar += 1
        elif helvar == 4:
            i01.mouth.speak("what is your problem stop saying how do you do all the time")
            i01.moveArm("left",30,83,22,10)
            i01.moveArm("right",40,85,30,10)
            i01.moveHand("left",130,180,180,180,180,119)
            i01.moveHand("right",130,180,180,180,180,119)
            sleep(2)
            relax()
            global helvar
            helvar += 1
        elif helvar == 5:
            i01.mouth.speak("i will ignore you if you say how do you do one more time")
            unhappy()
            sleep(4)
            relax()
            global helvar
            helvar += 1
 
    if (data == "i love you"):
        i01.mouth.speak("i love you too")
        i01.moveHead(116,80)
        i01.moveArm("left",85,93,42,16)
        i01.moveArm("right",87,93,37,18)
        i01.moveHand("left",124,82,65,81,41,143)
        i01.moveHand("right",59,53,89,61,36,21)
        i01.moveTorso(90,90,90)
        sleep(0.2)
        sleep(1)
        relax()

    data = msg_i01_ear_recognized.data[0]
    if (data == "what is the weather"):
        if weathervar <= 2:    
            i01.mouth.speak("I have no idea, I am not connected to internet")
            global weathervar
            weathervar += 1
        elif weathervar == 3:
            i01.mouth.speak("Sorry, I told you, I am not connected to internet")
            i01.moveArm("left",43,88,22,10)
            i01.moveArm("right",20,90,30,10)
            i01.moveHand("left",0,0,0,0,0,119)
            i01.moveHand("right",0,0,0,0,0,119)
            sleep(2)
            relax()
            global weathervar
            weathervar += 1
        elif weathervar == 4:
            i01.mouth.speak("Gael, you are annoying, stop asking me the weather")
            i01.moveArm("left",30,83,22,10)
            i01.moveArm("right",40,85,30,10)
            i01.moveHand("left",130,180,180,180,180,119)
            i01.moveHand("right",130,180,180,180,180,119)
            sleep(2)
            relax()
            global weathervar
            weathervar += 1
        elif weathervar == 5:
            i01.setHeadSpeed(0.95, 0.95, 0.90, 0.90, 1.0)
            i01.moveHead(80,66)
            sleep(1)
            i01.setHeadSpeed(0.95, 0.95, 0.90, 0.90, 1.0)
            i01.moveHead(80,110)
            sleep(1)
            i01.setHeadSpeed(0.95, 0.95, 0.90, 0.90, 1.0)
            i01.moveHead(80,66)
            sleep(1)
            i01.setHeadSpeed(0.95, 0.95, 0.90, 0.90, 1.0)
            i01.moveHead(80,110)
            sleep(1)
            i01.setHeadSpeed(0.95, 0.95, 0.90, 0.90, 1.0)
            i01.moveHead(80,66)
            sleep(1)
            i01.mouth.speak("Well, well, Humans are worst than robots, they never learn")
            fullspeed()
            i01.moveArm("left",85,106,25,18)
            i01.moveArm("right",87,107,32,18)
            i01.moveHand("left",110,62,56,88,81,145)
            i01.moveHand("right",78,88,101,95,81,27)
            i01.moveTorso(90,90,90)
            sleep(4)
            relax()
            global weathervar
            weathervar += 1 


             

     
def startkinect():
    i01.leftArm.shoulder.map(0,180,-25,105)
    i01.rightArm.shoulder.map(0,180,-30,100)
    i01.copyGesture(True)


def offkinect():
    i01.leftArm.shoulder.map(0,180,0,180)
    i01.rightArm.shoulder.map(0,180,0,180)
    i01.copyGesture(False)
    rest()

     
def trackHumans():
     i01.headTracking.faceDetect()
     i01.eyesTracking.faceDetect()
     fullspeed()

def trackPoint():
     i01.headTracking.startLKTracking()
     i01.eyesTracking.startLKTracking()
     fullspeed()

def stopTracking():
     i01.headTracking.stopTracking()
     i01.eyesTracking.stopTracking()

def takethis():
  fullspeed()
  i01.moveHead(58,96)
  i01.moveArm("left",13,45,95,10)
  i01.moveArm("right",5,90,30,10)
  i01.moveHand("left",2,2,2,2,2,15)
  i01.moveHand("right",81,66,82,60,105,113)
  i01.moveTorso(79,90,90)
  sleep(3)
  closelefthand()
  sleep(2)
  isitaball()

def fistHips():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(1.0, 1.0, 1.0)
  i01.moveHead(138,80)
  i01.moveArm("left",79,42,23,41)
  i01.moveArm("right",71,40,14,39)
  i01.moveHand("left",180,180,180,180,180,47)
  i01.moveHand("right",99,130,152,154,145,180)
  i01.moveTorso(90,90,90)

def unhappy():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(1.0, 1.0, 1.0)
  i01.moveHead(85,40)
  i01.moveArm("left",79,42,23,41)
  i01.moveArm("right",71,40,14,39)
  i01.moveHand("left",180,180,180,180,180,47)
  i01.moveHand("right",99,130,152,154,145,180)
  i01.moveTorso(90,90,90)

def rest():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(1.0, 1.0, 1.0)
  i01.moveHead(80,86,82,78,76)
  i01.moveArm("left",5,90,30,10)
  i01.moveArm("right",5,90,30,10)
  i01.moveHand("left",2,2,2,2,2,90)
  i01.moveHand("right",2,2,2,2,2,90)
  i01.moveTorso(90,90,90)
  
def fullspeed():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setTorsoSpeed(1.0, 1.0, 1.0)
 
def delicategrab():
  i01.setHandSpeed("left", 0.70, 0.60, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.75)
  i01.moveHead(21,98)
  i01.moveArm("left",30,72,77,10)
  i01.moveArm("right",0,91,28,17)
  i01.moveHand("left",180,130,4,0,0,180)
  i01.moveHand("right",86,51,133,162,153,180)
 
def perfect():
  i01.setHandSpeed("left", 0.80, 0.80, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 0.85, 0.85, 0.85, 0.95)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.75)
  i01.moveHead(88,79)
  i01.moveArm("left",89,75,93,11)
  i01.moveArm("right",0,91,28,17)
  i01.moveHand("left",130,160,83,40,0,34)
  i01.moveHand("right",86,51,133,162,153,180)

def fisthips():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.75)
  i01.moveHead(138,80)
  i01.moveArm("left",79,45,23,41)
  i01.moveArm("right",71,40,14,39)
  i01.moveHand("left",180,180,180,180,180,47)
  i01.moveHand("right",99,130,152,154,145,180)
  i01.moveTorso(90,90,90)
 
def releasedelicate():
  i01.setHandSpeed("left", 0.60, 0.60, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 0.75, 0.75, 0.75, 0.95)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.75)
  i01.moveHead(20,98)
  i01.moveArm("left",30,72,64,10)
  i01.moveArm("right",0,91,28,17)
  i01.moveHand("left",101,74,66,58,44,180)
  i01.moveHand("right",86,51,133,162,153,180)
 
def grabthebottle():
  i01.setHandSpeed("left", 1.0, 0.80, 0.80, 0.80, 1.0, 0.80)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.90, 0.80)
  i01.setTorsoSpeed(1.0,1.0,1.0)
  i01.moveHead(20,88)
  i01.moveArm("left",77,85,45,20)
  i01.moveArm("right",5,90,30,10)
  i01.moveHand("left",180,138,140,164,180,60)
  i01.moveHand("right",0,0,0,0,0,90)
  i01.moveTorso(70,90,90)
 
def grabtheglass():
  i01.setHandSpeed("left", 0.60, 0.60, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 0.60, 0.60, 1.0, 1.0, 0.80)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.65)
  i01.setTorsoSpeed(1.0,1.0,1.0)
  i01.moveHead(20,68)
  i01.moveArm("left",77,85,45,15)
  i01.moveArm("right",48,91,72,20)
  i01.moveHand("left",180,138,140,164,180,50)
  i01.moveHand("right",140,112,127,105,143,140)
  i01.moveTorso(105,90,90)
 
def poorbottle():
  i01.setHandSpeed("left", 0.60, 0.60, 0.60, 0.60, 0.60, 0.60)
  i01.setHandSpeed("right", 0.60, 0.80, 0.60, 0.60, 0.60, 0.60)
  i01.setArmSpeed("left", 0.60, 0.60, 0.60, 0.60)
  i01.setArmSpeed("right", 0.60, 0.60, 0.60, 0.60)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(0,92)
  i01.setTorsoSpeed(1.0,1.0,1.0)
  i01.moveArm("left",55,40,92,55)
  i01.moveArm("right",90,66,34,10)
  i01.moveHand("left",180,140,150,164,180,0)
  i01.moveHand("right",145,112,127,105,143,150)
  i01.moveTorso(90,90,90)
 
def givetheglass():
  sleep(2)
  i01.setHandSpeed("left", 0.60, 0.60, 0.60, 0.60, 0.60, 0.60)
  i01.setHandSpeed("right", 0.60, 0.80, 0.60, 0.60, 0.60, 0.60)
  i01.setArmSpeed("left", 0.60, 1.0, 0.60, 0.60)
  i01.setArmSpeed("right", 0.60, 0.60, 0.60, 0.60)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(84,79)
  i01.moveArm("left",77,75,45,17)
  i01.moveArm("right",21,80,77,10)
  i01.moveHand("left",109,138,180,164,180,60)
  i01.moveHand("right",102,86,105,105,143,133)
  i01.mouth.speakBlocking("Hello please take the glass")
  sleep(1)
 
def takeball():
  rest()
  i01.setHandSpeed("right", 0.85, 0.75, 0.75, 0.75, 0.85, 0.75)
  i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
  i01.setHeadSpeed(0.9, 0.9)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(30,70)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,76,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,140,140,3,0,11)
  i01.moveTorso(120,100,90)

def getball():
  rest()
  i01.setHandSpeed("right", 0.85, 0.75, 0.75, 0.75, 0.85, 0.75)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 0.85)
  i01.setHeadSpeed(0.9, 0.9)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(45,65)
  i01.moveArm("left",5,90,16,15)
  i01.moveArm("right",6,85,110,22)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",0,0,0,3,0,11)
  i01.moveTorso(101,100,90)
  sleep(2.5)
  i01.moveHand("right",180,140,140,3,0,11)
 
def keepball():
  i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setHandSpeed("right", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(0.9, 0.9)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(20,70)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",54,77,55,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,140,140,3,0,11)
  i01.moveTorso(90,90,90)
 

def approachlefthand():
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.25, 0.25, 0.25, 0.25)
  i01.setHeadSpeed(0.65, 0.65)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(20,84)
  i01.moveArm("left",67,52,62,23)
  i01.moveArm("right",55,61,45,16)
  i01.moveHand("left",130,0,40,10,10,0)
  i01.moveHand("right",180,145,145,3,0,11)
  i01.moveTorso(90,85,90)
  sleep(4)

def uselefthand():
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.25, 0.25, 0.25, 0.25)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(10,80)
  i01.moveArm("left",64,52,59,23)
  i01.moveArm("right",75,61,50,16)
  i01.moveHand("left",130,0,40,10,10,0)
  i01.moveHand("right",180,140,145,3,0,11)
  sleep(4)

def more():
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 0.85, 0.80, 0.85, 0.95)
  i01.setArmSpeed("right", 0.75, 0.65, 0.65, 0.65)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(13,80)
  i01.moveArm("left",64,52,59,23)
  i01.moveArm("right",75,60,50,16)
  i01.moveHand("left",140,148,140,10,10,0)
  i01.moveHand("right",80,114,114,3,0,11)
  sleep(3)

def handdown():
  i01.setHandSpeed("left", 0.75, 0.75, 0.75, 0.75, 0.75, 0.75)
  i01.setHandSpeed("right", 0.70, 0.70, 0.70, 0.70, 0.70, 1.0)
  i01.setArmSpeed("right", 0.85, 0.65, 0.65, 0.65)
  i01.moveHead(18,75)
  i01.moveArm("left",66,52,59,23)
  i01.moveArm("right",59,60,50,16)
  i01.moveHand("left",140,148,140,10,10,0)
  i01.moveHand("right",54,95,66,0,0,11)
  sleep(2)

def isitaball():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 0.8, 0.8, 0.90)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 0.95, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.90, 0.85)
  i01.setHeadSpeed(0.65, 0.75)
  i01.moveHead(70,82)
  i01.moveArm("left",70,59,95,15)
  i01.moveArm("right",12,74,33,15)
  i01.moveHand("left",170,150,180,180,180,164)
  i01.moveHand("right",105,81,78,57,62,105)

 
def putitdown():
  i01.setHandSpeed("left", 0.90, 0.90, 0.90, 0.90, 0.90, 0.90)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(0.75, 0.75)
  i01.moveHead(20,99)
  i01.moveArm("left",5,45,87,31)
  i01.moveArm("right",5,82,33,15)
  i01.moveHand("left",147,130,135,34,34,35)
  i01.moveHand("right",20,40,40,30,30,72)
 
def dropit():
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 1.0, 0.85)
  i01.setHeadSpeed(0.75, 0.75)
  i01.moveHead(20,99)
  i01.moveArm("left",5,45,87,31)
  i01.moveArm("right",5,82,33,15)
  sleep(3)
  i01.moveHand("left",60,61,67,34,34,35)
  i01.moveHand("right",20,40,40,30,30,72)
 
 
def removeleftarm():
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.95, 0.65, 0.75, 0.75)
  i01.setHeadSpeed(0.75, 0.75)
  i01.moveHead(20,100)
  i01.moveArm("left",71,94,41,31)
  i01.moveArm("right",5,82,28,15)
  i01.moveHand("left",60,43,45,34,34,35)
  i01.moveHand("right",20,40,40,30,30,72)
  

def relax():
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setArmSpeed("right", 0.75, 0.85, 0.65, 0.85)
  i01.setArmSpeed("left", 0.95, 0.65, 0.75, 0.75)
  i01.setHeadSpeed(0.85, 0.85)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(79,100)
  i01.moveArm("left",5,84,28,15)
  i01.moveArm("right",5,82,28,15)
  i01.moveHand("left",92,33,37,71,66,25)
  i01.moveHand("right",81,66,82,60,105,113)
  i01.moveTorso(90,90,90)

def armsUp():
    i01.setHeadSpeed(1.0,1.0)
    i01.moveHead(180,86)
    sleep(1)
    i01.setHandSpeed("left",0.90,0.90,0.90,0.90,0.90,1.0)
    i01.setHandSpeed("right",0.90,0.90,0.90,0.90,0.90,1.0)
    i01.moveHand("left",170,170,170,170,170,33)
    i01.moveHand("right",170,170,170,170,170,180)
    sleep(3)
    i01.setArmSpeed("left",1.0,1.0,1.0,1.0)
    i01.setArmSpeed("right",1.0,1.0,1.0,1.0)
    i01.setTorsoSpeed(1.0,1.0,1.0)
    i01.moveArm("left",90,90,170,20)
    i01.moveArm("right",90,90,173,20)
    sleep(9)
    i01.setHandSpeed("left",1.0,1.0,1.0,1.0,1.0,1.0)
    i01.setHandSpeed("right",1.0,1.0,1.0,1.0,1.0,1.0)
    i01.moveHead(180,86)
    i01.moveArm("left",5,90,170,10)
    i01.moveArm("right",5,90,173,10)
    i01.moveHand("left",2,2,2,2,2,33)
    i01.moveHand("right",2,2,2,2,2,180)
    i01.moveTorso(90,90,90)
 
def handopen():
  i01.moveHand("left",0,0,0,0,0)
  i01.moveHand("right",0,0,0,0,0)

def handclose():
  i01.moveHand("left",180,180,180,180,180)
  i01.moveHand("right",180,180,180,180,180)
 
def openlefthand():
  i01.moveHand("left",0,0,0,0,0)
 
 
def openrighthand():
  i01.moveHand("right",0,0,0,0,0)

def closelefthand():
  i01.moveHand("left",180,180,180,180,180)
 
 
def closerighthand():
  i01.moveHand("right",180,180,180,180,180)
 
 
def surrender():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(90,90)
  i01.moveArm("left",90,139,15,79)
  i01.moveArm("right",90,145,37,79)
  i01.moveHand("left",50,28,30,10,10,76)
  i01.moveHand("right",10,10,10,10,10,139)
 
def pictureleftside():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(109,90)
  i01.moveArm("left",90,105,24,75)
  i01.moveArm("right",5,82,28,15)
  i01.moveHand("left",50,86,97,74,106,119)
  i01.moveHand("right",81,65,82,60,105,113)
 
def picturerightside():
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(109,90)
  i01.moveArm("left",5,94,28,15)
  i01.moveArm("right",90,115,23,68)
  i01.moveHand("left",42,58,87,55,71,35)
  i01.moveHand("right",10,112,95,91,125,45)
 
def picturebothside():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(109,90)
  i01.moveJaw(50)
  i01.moveArm("left",90,105,24,75)
  i01.moveArm("right",90,115,23,68)
  i01.moveHand("left",50,86,97,74,106,119)
  i01.moveHand("right",10,112,95,91,125,45)

def lookrightside():
  i01.setHeadSpeed(0.70, 0.70)
  i01.moveHead(85,40)

def lookleftside():
  i01.setHeadSpeed(0.70, 0.70)
  i01.moveHead(85,140)

def lookinmiddle():
  i01.setHeadSpeed(0.70, 0.70)
  i01.moveHead(85,86)

def eyesfront():
    i01.head.eyeX.moveTo(85)
    i01.head.eyeY.moveTo(85)
    
def eyesdown():
    i01.head.eyeY.moveTo(180)
    
def eyesupp():
    i01.head.eyeY.moveTo(0)
 
def eyesright():
    i01.head.eyeX.moveTo(0)
 
def eyesleft():
    i01.head.eyeX.moveTo(180)
    
def headfront():
    i01.head.neck.moveTo(90)
    i01.head.rothead.moveTo(90)
 
def headdown():
    i01.head.neck.moveTo(0)
 
def headupp():
    i01.head.neck.moveTo(180) 

def headright():
    i01.head.rothead.moveTo(0)
 
def headleft():
    i01.head.rothead.moveTo(180)    

def Torso():
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveTorso(60,90,90)
    sleep(2)
    i01.moveTorso(120,90,90)
    sleep(2)
    i01.moveTorso(90,90,90)
    sleep(2)     

def muscle():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(0.65, 0.65)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(90,129)
  i01.moveArm("left",90,139,48,75)
  i01.moveArm("right",71,40,14,43)
  i01.moveHand("left",180,180,180,180,180,148)
  i01.moveHand("right",99,130,152,154,145,180)
  i01.moveTorso(120,100,90)
  sleep(4)
  i01.mouth.speakBlocking("Looks good, doesn't it")
  sleep(2)
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.85, 0.85)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(90,45)
  i01.moveArm("left",44,46,20,39)
  i01.moveArm("right",90,145,58,74)
  i01.moveHand("left",180,180,180,180,180,83)
  i01.moveHand("right",99,130,152,154,145,21)
  i01.moveTorso(60,75,90)
  sleep(3)
  i01.mouth.speakBlocking("not bad either, don't you think")
  sleep(4)
  relax()
  sleep(1)

def shakehand():
  data = msg_i01_ear_recognized.data[0]
##rest
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(1.0, 1.0, 1.0)
  i01.moveHead(80,86)
  i01.moveArm("left",5,90,30,10)
  i01.moveArm("right",5,90,30,10)
  i01.moveHand("left",2,2,2,2,2,90)
  i01.moveHand("right",2,2,2,2,2,90)
  i01.moveTorso(90,90,90)
  sleep(1)
##move arm and hand
  i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setHandSpeed("right", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(39,70)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,65,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",50,50,40,20,20,90)
  i01.moveTorso(101,100,90)
  sleep(1)
##close the hand
  i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.75, 0.85)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(39,70)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,62,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,126,120,145,168,77)
  i01.moveTorso(101,100,90)
  sleep(3)
##shake hand up
  i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(85,90)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,70,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,126,120,145,168,77)
  i01.moveTorso(101,100,90)
  sleep(1)
##shake hand down
  if (data == "shake hand"):
       x = (random.randint(1, 4))
       if x == 1:
            i01.mouth.speak("please to meet you")
       if x == 2:
            i01.mouth.speak("carefull my hand is made out of plastic")
       if x == 3:
            i01.mouth.speak("I am happy to shake a human hand")
       if x == 4:
            i01.mouth.speak("it is a pleasure to meet you")
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.75, 0.75, 0.95, 0.85)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(1.0, 1.0, 1.0)
  i01.moveHead(85,90)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,60,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,126,120,145,168,77)
  i01.moveTorso(101,100,90)
  sleep(1)
##shake hand up
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.75, 0.75, 0.95, 0.85)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(1.0, 1.0, 1.0)
  i01.moveHead(85,90)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,75,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,126,120,145,168,77)
  i01.moveTorso(101,100,90)
  sleep(1)
##shake hand down
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.75, 0.75, 0.95, 0.85)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(1.0, 1.0, 1.0)
  i01.moveHead(82,88)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,62,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,126,120,145,168,77)
  i01.moveTorso(101,100,90)
  sleep(2)
## release hand  
  i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.95, 0.95, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(39,70)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,62,16)
  i01.moveHand("left",50,50,40,20,20,77)
  i01.moveHand("right",20,50,40,20,20,90)
  i01.moveTorso(101,100,90)
  sleep(1)
##relax
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 0.85)
  i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
  i01.setArmSpeed("left", 0.95, 0.65, 0.75, 0.75)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(79,100)
  i01.moveArm("left",5,84,28,15)
  i01.moveArm("right",5,90,30,10)
  i01.moveHand("left",92,33,37,71,66,25)
  i01.moveHand("right",10,50,40,20,20,113)
  i01.moveTorso(90,90,90)  

  
def power_down():
        relax()
        i01.powerDown()
        ##sleep(2)       
        ##ear.pauseListening()
        ##relax()
        ##i01.mouth.speakBlocking()
        ##sleep(2)
        ##i01.moveHead(40, 85);
        ##sleep(4)
        ##rightSerialPort.digitalWrite(53, Arduino.LOW)
        ##leftSerialPort.digitalWrite(53, Arduino.LOW)
        ear.lockOutAllGrammarExcept("power up")
        sleep(2)
        ear.resumeListening()
 
def power_up():
        ##sleep(2)        
        ##ear.pauseListening()
        ##rightSerialPort.digitalWrite(53, Arduino.HIGH)
        ##leftSerialPort.digitalWrite(53, Arduino.HIGH)
        i01.mouth.speakBlocking("I was sleeping")
        lookrightside()
        sleep(2)
        lookleftside()
        sleep(4)
        relax()
        ear.clearLock()
        sleep(2)
        ear.resumeListening()
 
def hello():
     i01.setHandSpeed("left", 0.60, 0.60, 1.0, 1.0, 1.0, 1.0)
     i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
     i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
     i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
     i01.setHeadSpeed(0.65, 0.75)
     i01.moveHead(105,78)
     i01.moveArm("left",78,48,37,11)
     i01.moveArm("right",90,144,60,75)
     i01.moveHand("left",112,111,105,102,81,10)
     i01.moveHand("right",0,0,0,50,82,180)
     ear.pauseListening()
     sleep(1)
 
     for w in range(0,3):
          i01.setHandSpeed("left", 0.60, 0.60, 1.0, 1.0, 1.0, 1.0)
          i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 0.60)
          i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
          i01.setArmSpeed("right", 0.60, 1.0, 1.0, 1.0)
          i01.setHeadSpeed(0.65, 0.75)
          i01.moveHead(83,98)
          i01.moveArm("left",78,48,37,11)
          i01.moveArm("right",90,157,47,75)
          i01.moveHand("left",112,111,105,102,81,10)
          i01.moveHand("right",3,0,62,41,117,94)
          
 
          if w==1:
                     i01.setHandSpeed("left", 0.60, 0.60, 1.0, 1.0, 1.0, 1.0)
                     i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 0.60)
                     i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
                     i01.setArmSpeed("right", 0.65, 1.0, 1.0, 1.0)
                     i01.setHeadSpeed(0.65, 0.75)
                     i01.moveHead(83,70)
                     i01.mouth.speakBlocking("hello, my name is inmov")
                     i01.moveArm("left",78,48,37,11)
                     i01.moveArm("right",57,145,50,68)
                     i01.moveHand("left",100,90,85,80,71,15)
                     i01.moveHand("right",3,0,31,12,26,45)
                     sleep(1)
                     i01.moveHead(83,98)
                     i01.moveArm("left",78,48,37,11)
                     i01.moveArm("right",90,157,47,75)
                     i01.moveHand("left",112,111,105,102,81,10)
                     i01.moveHand("right",3,0,62,41,117,94)
                     sleep(1)
                     i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
                     i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
                     i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
                     i01.setArmSpeed("left", 0.95, 0.65, 0.75, 0.75)
                     i01.setHeadSpeed(0.75, 0.75)
                     i01.moveHead(79,100)
                     i01.moveArm("left",5,94,28,15)
                     i01.moveArm("right",5,82,28,15)
                     i01.moveHand("left",42,58,42,55,71,35)
                     i01.moveHand("right",81,50,82,60,105,113)
                     ear.resumeListening()

def italianhello():
     i01.setHandSpeed("left", 0.60, 0.60, 1.0, 1.0, 1.0, 1.0)
     i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
     i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
     i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
     i01.setHeadSpeed(0.65, 0.75)
     i01.moveHead(105,78)
     i01.moveArm("left",78,48,37,11)
     i01.moveArm("right",90,144,60,75)
     i01.moveHand("left",112,111,105,102,81,10)
     i01.moveHand("right",0,0,0,50,82,180)
     ear.pauseListening()
     sleep(1)
 
     for w in range(0,3):
          i01.setHandSpeed("left", 0.60, 0.60, 1.0, 1.0, 1.0, 1.0)
          i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 0.60)
          i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
          i01.setArmSpeed("right", 0.60, 1.0, 1.0, 1.0)
          i01.setHeadSpeed(0.65, 0.75)
          i01.moveHead(83,98)
          i01.moveArm("left",78,48,37,11)
          i01.moveArm("right",90,157,47,75)
          i01.moveHand("left",112,111,105,102,81,10)
          i01.moveHand("right",3,0,62,41,117,94)
          
 
          if w==1:
                     i01.setHandSpeed("left", 0.60, 0.60, 1.0, 1.0, 1.0, 1.0)
                     i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 0.60)
                     i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
                     i01.setArmSpeed("right", 0.65, 1.0, 1.0, 1.0)
                     i01.setHeadSpeed(0.65, 0.75)
                     i01.moveHead(83,70)
                     i01.mouth.speakBlocking("ciao , il mio nome e inmoov one")
                     i01.moveArm("left",78,48,37,11)
                     i01.moveArm("right",57,145,50,68)
                     i01.moveHand("left",100,90,85,80,71,15)
                     i01.moveHand("right",3,0,31,12,26,45)
                     sleep(1)
                     i01.moveHead(83,98)
                     i01.moveArm("left",78,48,37,11)
                     i01.moveArm("right",90,157,47,75)
                     i01.moveHand("left",112,111,105,102,81,10)
                     i01.moveHand("right",3,0,62,41,117,94)
                     sleep(1)
                     i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
                     i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
                     i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
                     i01.setArmSpeed("left", 0.95, 0.65, 0.75, 0.75)
                     i01.setHeadSpeed(0.75, 0.75)
                     i01.moveHead(79,100)
                     i01.moveArm("left",5,94,28,15)
                     i01.moveArm("right",5,82,28,15)
                     i01.moveHand("left",42,58,42,55,71,35)
                     i01.moveHand("right",81,50,82,60,105,113)
                     ear.resumeListening()
                     
def photo():    
        i01.moveHead(87,60)
        i01.moveArm("left",78,48,37,11)
        i01.moveArm("right",46,147,5,75)
        i01.moveHand("left",138,52,159,106,120,90)
        i01.moveHand("right",80,65,94,63,70,140)
 
def beforehappy():
        i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 1.0)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(84,88)
        i01.moveArm("left",5,82,36,11)
        i01.moveArm("right",74,112,61,29)
        i01.moveHand("left",0,88,135,94,96,90)
        i01.moveHand("right",81,79,118,47,0,90)
 
def happy():
     for w in range(0,3):
         sleep(1)
         i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
         i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
         i01.setArmSpeed("right", 0.85, 0.85, 0.85, 1.0)
         i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
         i01.setHeadSpeed(0.65, 0.65)
         i01.moveHead(84,88)
         i01.moveArm("left",5,82,36,10)
         i01.moveArm("right",74,112,61,29)
         i01.moveHand("left",0,88,135,94,96,90)
         i01.moveHand("right",81,79,118,47,0,90)
         sleep(1)
         if w==1:
                     i01.mouth.speakBlocking("happy birthday grog")
                     i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
                     i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
                     i01.setArmSpeed("right", 0.85, 0.85, 0.85, 1.0)
                     i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
                     i01.setHeadSpeed(0.65, 0.65)
                     i01.moveHead(42,76)
                     i01.moveArm("left",5,90,30,10)
                     i01.moveArm("right",74,70,61,10)
                     i01.moveHand("left",0,0,0,0,0,90)
                     i01.moveHand("right",81,79,118,47,0,90)
                     sleep(5)
                     ear.resumeListening()
 
def about():
        sleep(2)        
        ear.pauseListening()
        sleep(2)
        i01.setArmSpeed("right", 0.1, 0.1, 0.2, 0.2);
        i01.setArmSpeed("left", 0.1, 0.1, 0.2, 0.2);
        i01.setHeadSpeed(0.2,0.2)
        i01.moveArm("right", 64, 94, 10, 10);
 
 
        i01.mouth.speakBlocking("I am the first life size humanoid robot you can 3D print and animate")
        i01.moveHead(65,66)
        i01.moveArm("left", 64, 104, 10, 11);
        i01.moveArm("right", 44, 84, 10, 11);
        i01.mouth.speakBlocking("my designer creator is Gael Langevin a French sculptor, model maker")
        i01.moveHead(75,86)
        i01.moveArm("left", 54, 104, 10, 11);
        i01.moveArm("right", 64, 84, 10, 20);
        i01.mouth.speakBlocking("who has released my files  to the opensource 3D world.")
        i01.moveHead(65,96)
        i01.moveArm("left", 44, 94, 10, 20);
        i01.moveArm("right", 54, 94, 20, 11);
        i01.mouth.speakBlocking("this is where my builder downloaded my files.")
 
        i01.moveHead(75,76)
        i01.moveArm("left", 64, 94, 20, 11);
        i01.moveArm("right", 34, 94, 10, 11);
        i01.mouth.speakBlocking("after five hundred hours of printing, four kilos of plastic, twenty five hobby servos, blood and sweat.I was brought to life") # should be " i was borght to life."
        i01.moveHead(65,86)
        i01.moveArm("left", 24, 94, 10, 11);
        i01.moveArm("right", 24, 94, 10, 11);  
        i01.mouth.speakBlocking("so if You have a 3D printer, some building skills, then you can build your own version of me") # mabe add in " alot of money"
        i01.moveHead(85,86)
        i01.moveArm("left", 5, 94, 20, 30);
        i01.moveArm("right", 24, 124, 10, 20);
        i01.mouth.speakBlocking("and if enough people build me, some day my kind could take over the world") # mabe add in " alot of money"
        i01.moveHead(75,96)
        i01.moveArm("left", 24, 104, 10, 11);
        i01.moveArm("right", 5, 94, 20, 30);
        i01.mouth.speakBlocking("I'm just kidding. i need some legs to get around, and i have to over come my  pyro-phobia, a fear of fire") # mabe add in " alot of money"
        i01.moveHead(75,96)
        i01.moveArm("left", 5, 94, 10, 11)
        i01.moveArm("right", 4, 94, 10, 11);
        i01.mouth.speakBlocking("so, until then. i will be humankind's humble servant")
 
        i01.rest()
        i01.setArmSpeed("right", 1, 1, 1, 1);
        i01.setArmSpeed("left", 1, 1, 1, 1);
        i01.setHeadSpeed(1,1)
        sleep(2)
        ear.resumeListening()
 
def servos():  
        ear.pauseListening()
        sleep(2)
        i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(79,100)
        i01.moveArm("left",5,119,28,15)
        i01.moveArm("right",5,111,28,15)
        i01.moveHand("left",42,58,87,55,71,35)
        i01.moveHand("right",81,20,82,60,105,113)
        i01.mouth.speakBlocking("I currently have twenty five  hobby servos installed in my body to give me life")
        i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(124,90)
        i01.moveArm("left",89,94,91,35)
        i01.moveArm("right",20,67,31,22)
        i01.moveHand("left",106,41,161,147,138,90)
        i01.moveHand("right",0,0,0,54,91,90)
        i01.mouth.speakBlocking("there's one servo  for moving my mouth up and down")
        sleep(1)
        i01.setHandSpeed("left", 0.85, 0.85, 1.0, 0.85, 0.85, 0.85)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(105,76);
        i01.moveArm("left",89,106,103,35);
        i01.moveArm("right",35,67,31,22);
        i01.moveHand("left",106,0,0,147,138,7);
        i01.moveHand("right",0,0,0,54,91,90);
        i01.mouth.speakBlocking("two for my eyes")
        sleep(0.2)
        i01.setHandSpeed("left", 0.85, 0.85, 1.0, 1.0, 1.0, 0.85)
        i01.moveHand("left",106,0,0,0,0,7);
        i01.mouth.speakBlocking("and two more for my head")
        sleep(0.5)
        i01.setHandSpeed("left", 0.85, 0.9, 0.9, 0.9, 0.9, 0.85)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(90,40);
        i01.moveArm("left",89,106,103,35);
        i01.moveArm("right",35,67,31,20);
        i01.moveHand("left",106,140,140,140,140,7);
        i01.moveHand("right",0,0,0,54,91,90);
        i01.mouth.speakBlocking("so i can look around")
        sleep(0.5)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(105,125);
        i01.setArmSpeed("left", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("left",60,100,85,30);
        i01.mouth.speakBlocking("and see who's there")
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(40,56);
        sleep(0.5)
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0);
        i01.setArmSpeed("right", 0.5, 0.6, 0.5, 0.6);
        i01.moveArm("left",87,41,64,11)
        i01.moveArm("right",5,95,40,11)
        i01.moveHand("left",98,150,160,160,160,104)
        i01.moveHand("right",0,0,50,54,91,90);
        i01.mouth.speakBlocking("there's three servos  in each shoulder")
        i01.moveHead(40,67);
        sleep(2)
        i01.setHandSpeed("left", 0.8, 0.9, 0.8, 0.8, 0.8, 0.8)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.8, 0.8)
        i01.moveHead(43,69)
        i01.moveArm("left",87,41,64,11)
        i01.moveArm("right",5,95,40,42)
        i01.moveHand("left",42,0,100,80,113,35)
        i01.moveHand("left",42,10,160,160,160,35)
        i01.moveHand("right",81,20,82,60,105,113)
        i01.mouth.speakBlocking("here is the first servo movement")
        sleep(1)
        i01.moveHead(37,60);
        i01.setHandSpeed("left", 1.0, 1.0, 0.9, 0.9, 1.0, 0.8)
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
        i01.moveArm("right",5,95,67,42)
        i01.moveHand("left",42,10,10,160,160,30)
        i01.mouth.speakBlocking("this is the second one")
        sleep(1)
        i01.moveHead(43,69);
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
        i01.moveArm("right",5,134,67,42)
        i01.moveHand("left",42,10,10,10,160,35)
        i01.mouth.speakBlocking("now you see the third")
        sleep(1)
        i01.setArmSpeed("right", 0.8, 0.8, 0.8, 0.8)
        i01.moveArm("right",20,90,45,16)
        i01.mouth.speakBlocking("they give me a more human like movement")
        sleep(1)
        i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0);
        i01.moveHead(43,72)
        i01.moveArm("left",90,44,66,11)
        i01.moveArm("right",90,100,67,26)
        i01.moveHand("left",42,80,100,80,113,35)
        i01.moveHand("right",81,0,82,60,105,69)
        i01.mouth.speakBlocking("but, i have only  one servo, to move each elbow")
        i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.8, 0.8)
        i01.moveHead(45,62)
        i01.moveArm("left",72,44,90,11)
        i01.moveArm("right",90,95,68,15)
        i01.moveHand("left",42,0,100,80,113,35)
        i01.moveHand("right",81,0,82,60,105,0)
        i01.mouth.speakBlocking("that, leaves me, with one servo per wrist")
        i01.moveHead(40,60)
        i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("left",72,44,90,9)
        i01.moveArm("right",90,95,68,15)
        i01.moveHand("left",42,0,100,80,113,35)
        i01.moveHand("right", 10, 140,82,60,105,10)
        i01.mouth.speakBlocking("and one servo for each finger.")
        sleep(0.5)
        i01.moveHand("left",42,0,100,80,113,35)
        i01.moveHand("right", 50, 51, 15,23, 30,140);
        i01.mouth.speakBlocking("these servos are located in my forearms")
        i01.setHandSpeed("left", 0.8, 0.8, 0.8, 0.8,0.8, 0.8)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.moveHand("left", 36, 52, 8,22, 20);
        i01.moveHand("right", 120, 147, 130,110, 125);
        removeleftarm()
        sleep(1)
        i01.mouth.speakBlocking("they are hooked up, by the use of tendons")
        i01.moveHand("left",10,20,30,40,60,150);
        i01.moveHand("right",110,137,120,100,105,130);
        i01.setHeadSpeed(1,1)
        i01.setArmSpeed("right", 1.0,1.0, 1.0, 1.0);
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0);
        relax()
        sleep(2)
        ear.resumeListening()
 
def howmanyfingersdoihave():
     ear.pauseListening()
     sleep(1)
     fullspeed()
     i01.moveHead(49,74)
     i01.moveArm("left",75,83,79,24)
     i01.moveArm("right",65,82,71,24)
     i01.moveHand("left",74,140,150,157,168,92)
     i01.moveHand("right",89,80,98,120,114,0)
     sleep(2)
     i01.moveHand("right",0,80,98,120,114,0)
     i01.mouth.speakBlocking("ten")
 
     sleep(.1)
     i01.moveHand("right",0,0,98,120,114,0)
     i01.mouth.speakBlocking("nine")
 
     sleep(.1)
     i01.moveHand("right",0,0,0,120,114,0)
     i01.mouth.speakBlocking("eight")
 
     sleep(.1)
     i01.moveHand("right",0,0,0,0,114,0)
     i01.mouth.speakBlocking("seven")
 
     sleep(.1)
     i01.moveHand("right",0,0,0,0,0,0)
     i01.mouth.speakBlocking("six")
 
     sleep(.5)
     i01.setHeadSpeed(.70,.70)
     i01.moveHead(40,105)
     i01.moveArm("left",75,83,79,24)
     i01.moveArm("right",65,82,71,24)
     i01.moveHand("left",0,0,0,0,0,180)
     i01.moveHand("right",0,0,0,0,0,0)
     sleep(0.1)
     i01.mouth.speakBlocking("and five makes eleven")
 
     sleep(0.7)
     i01.setHeadSpeed(0.7,0.7)
     i01.moveHead(40,50)
     sleep(0.5)
     i01.setHeadSpeed(0.7,0.7)
     i01.moveHead(49,105)
     sleep(0.7)
     i01.setHeadSpeed(0.7,0.8)
     i01.moveHead(40,50)
     sleep(0.7)
     i01.setHeadSpeed(0.7,0.8)
     i01.moveHead(49,105)
     sleep(0.7)
     i01.setHeadSpeed(0.7,0.7)
     i01.moveHead(90,85)
     sleep(0.7)
     i01.mouth.speakBlocking("eleven")
     i01.moveArm("left",70,75,70,20)
     i01.moveArm("right",60,75,65,20)
     sleep(1)
     i01.mouth.speakBlocking("that doesn't seem right")
     sleep(2)
     i01.mouth.speakBlocking("I think I better try that again")
 
     i01.moveHead(40,105)
     i01.moveArm("left",75,83,79,24)
     i01.moveArm("right",65,82,71,24)
     i01.moveHand("left",140,168,168,168,158,90)
     i01.moveHand("right",87,138,109,168,158,25)
     sleep(2)
 
     i01.moveHand("left",10,140,168,168,158,90)
     i01.mouth.speakBlocking("one")
     sleep(.1)
 
 
     i01.moveHand("left",10,10,168,168,158,90)
     i01.mouth.speakBlocking("two")
     sleep(.1)
 
     i01.moveHand("left",10,10,10,168,158,90)
     i01.mouth.speakBlocking("three")
     sleep(.1)
     i01.moveHand("left",10,10,10,10,158,90)
 
     i01.mouth.speakBlocking("four")
     sleep(.1)
     i01.moveHand("left",10,10,10,10,10,90)
 
     i01.mouth.speakBlocking("five")
     sleep(.1)
     i01.setHeadSpeed(0.65,0.65)
     i01.moveHead(53,65)
     i01.moveArm("right",48,80,78,11)
     i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
     i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
     i01.moveHand("left",10,10,10,10,10,90)
     i01.moveHand("right",10,10,10,10,10,25)
     sleep(1)
     i01.mouth.speakBlocking("and five makes ten")
     sleep(.5)
     i01.mouth.speakBlocking("there that's better")
     i01.moveHead(95,85)
     i01.moveArm("left",75,83,79,24)
     i01.moveArm("right",40,70,70,10)
     sleep(0.5)
     i01.mouth.speakBlocking("inmoov has ten fingers")
     sleep(0.5)
     i01.moveHead(90,90)
     i01.setHandSpeed("left", 0.8, 0.8, 0.8, 0.8, 0.8, 0.8)
     i01.setHandSpeed("right", 0.8, 0.8, 0.8, 0.8, 0.8, 0.8)
     i01.moveHand("left",140,140,140,140,140,60)
     i01.moveHand("right",140,140,140,140,140,60)
     sleep(1.0)
     i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
     i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
     i01.moveArm("left",5,90,30,11)
     i01.moveArm("right",5,90,30,11)
     sleep(0.5)
     relax()
     sleep(0.5)
 
     ear.resumeListening()


def studyball():
##keepball():
  i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setHandSpeed("right", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(0.9, 0.9)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(20,70)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",54,77,55,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,145,145,3,0,11)
  i01.moveTorso(90,90,90)
  sleep(3)
##approachlefthand():
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.25, 0.25, 0.25, 0.25)
  i01.setHeadSpeed(0.65, 0.65)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(20,84)
  i01.moveArm("left",67,52,62,23)
  i01.moveArm("right",55,61,45,16)
  i01.moveHand("left",130,0,40,10,10,0)
  i01.moveHand("right",180,145,145,3,0,11)
  i01.moveTorso(90,85,90)
  sleep(4)
##uselefthand():
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.25, 0.25, 0.25, 0.25)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(10,80)
  i01.moveArm("left",64,52,59,23)
  i01.moveArm("right",75,61,50,16)
  i01.moveHand("left",130,0,40,10,10,0)
  i01.moveHand("right",180,140,145,3,0,11)
  sleep(4)
##more():
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 0.85, 0.80, 0.85, 0.95)
  i01.setArmSpeed("right", 0.75, 0.65, 0.65, 0.65)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(13,80)
  i01.moveArm("left",64,52,59,23)
  i01.moveArm("right",75,60,50,16)
  i01.moveHand("left",140,148,140,10,10,0)
  i01.moveHand("right",80,114,114,3,0,11)
  sleep(3)
##handdown():
  i01.setHandSpeed("left", 0.75, 0.75, 0.75, 0.75, 0.75, 0.75)
  i01.setHandSpeed("right", 0.70, 0.70, 0.70, 0.70, 0.70, 1.0)
  i01.setArmSpeed("right", 0.85, 0.65, 0.65, 0.65)
  i01.moveHead(18,75)
  i01.moveArm("left",66,52,59,23)
  i01.moveArm("right",59,60,50,16)
  i01.moveHand("left",140,148,140,10,10,0)
  i01.moveHand("right",54,95,66,0,0,11)
  sleep(2)
#isitaball():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 0.8, 0.8, 0.90)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 0.95, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.90, 0.85)
  i01.setHeadSpeed(0.65, 0.75)
  i01.moveHead(70,82)
  i01.moveArm("left",70,59,95,15)
  i01.moveArm("right",12,74,33,15)
  i01.moveHand("left",170,150,180,180,180,164)
  i01.moveHand("right",105,81,78,57,62,105)
  i01.mouth.speakBlocking("I will start tracking the object")
  sleep(2)
  i01.mouth.speakBlocking("you need to set the point")
  fullspeed()
  i01.headTracking.startLKTracking()
  i01.eyesTracking.startLKTracking()
  sleep()

def welcome():
  sleep(1)
  i01.setHandSpeed("left", 0.60, 0.60, 0.60, 0.60, 0.60, 0.60)
  i01.setHandSpeed("right", 0.60, 0.80, 0.60, 0.60, 0.60, 0.60)
  i01.setArmSpeed("left", 0.60, 0.60, 0.60, 0.60)
  i01.setArmSpeed("right", 0.60, 0.60, 0.60, 0.60)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(80,90)
  i01.moveArm("left",26,105,30,25)
  i01.moveArm("right",37,124,30,27)
  i01.moveHand("left",2,2,2,2,2,90)
  i01.moveHand("right",2,2,2,2,2,90)
  sleep(1)
  i01.mouth.speakBlocking("Welcome to the inmoov nation")
  sleep(1)


def cyclegesture1():
    welcome()
    sleep(1)
    relax()
    servos()

def cyclegesture2():
  ##for x in range(5):
    welcome()
    sleep(1)
    relax()
    sleep(2)
    fingerright()
    sleep(1)
    isitaball()
    sleep(2)
    removeleftarm()
    sleep(2)
    handdown()
    sleep(1)
    fullspeed()
    i01.giving()
    sleep(5)
    removeleftarm()
    sleep(4)
    takeball()
    sleep(1)
    surrender()
    sleep(6)
    isitaball()
    sleep(6)
    dropit()
    sleep(2)
    removeleftarm()
    sleep(5)
    relax()
    sleep()
    fullspeed()
    sleep(5)
    madeby()
    relax()
    sleep(5)
    i01.detach()

def cyclegesture3():
    ##for x in range(3):
    rest()
    i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(0.9, 0.9)
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(50,110)
    i01.moveArm("left",88,90,70,23)
    i01.moveArm("right",73,90,70,27)
    i01.moveHand("left",2,2,2,2,2,90)
    i01.moveHand("right",2,2,2,2,2,90)
    i01.moveTorso(90,90,90)
    sleep(2)
    i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(0.9, 0.8)
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(50,70)
    i01.moveArm("left",88,90,75,28)
    i01.moveArm("right",80,90,76,21)
    i01.moveHand("left",180,180,180,180,180,90)
    i01.moveHand("right",180,180,180,180,180,90)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.setHandSpeed("left", 0.95, 0.95, 0.95, 0.95, 0.95, 1.0)
    i01.setHandSpeed("right", 0.95, 0.95, 0.95, 0.95, 0.95, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(0.9, 0.8)
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(40,70)
    i01.moveArm("left",90,82,70,23)
    i01.moveArm("right",80,82,68,27)
    i01.moveHand("left",2,2,2,2,2,90)
    i01.moveHand("right",2,2,2,2,2,90)
    i01.moveTorso(90,90,90)
    sleep(2)
    i01.moveHead(50,100)
    i01.moveArm("left",88,90,70,28)
    i01.moveArm("right",75,90,76,21)
    i01.moveHand("left",180,180,180,180,180,10)
    i01.moveHand("right",180,180,180,180,180,170)
    i01.moveTorso(90,90,90) 
    sleep(2)
    i01.moveHead(50,70)
    i01.moveArm("left",88,90,75,28)
    i01.moveArm("right",80,90,76,21)
    i01.moveHand("left",180,180,180,180,180,170)
    i01.moveHand("right",180,180,180,180,180,10)
    i01.moveTorso(90,90,90)   
    sleep(3)
    i01.setHandSpeed("left", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
    i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(0.9, 0.9)
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(79,160)
    i01.moveArm("left",5,84,32,80)
    i01.moveArm("right",87,82,123,74)
    i01.moveHand("left",0,0,0,0,0,25)
    i01.moveHand("right",0,0,0,0,0,113)
    i01.moveTorso(170,90,90)
    sleep(6)
    i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(0.8, 0.8)
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(79,100)
    i01.moveArm("left",18,84,55,71)
    i01.moveArm("right",65,82,118,15)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",81,66,82,60,105,113)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setArmSpeed("left", 0.9,  0.9,  0.9,  0.9)
    i01.setArmSpeed("right",  0.9,  0.9,  0.9,  0.9)
    i01.setHeadSpeed(0.8, 0.8)
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(60,50)
    i01.moveArm("left",18,84,54,69)
    i01.moveArm("right",65,82,118,13)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",180,180,180,180,180,113)
    i01.moveTorso(40,90,90)
    sleep(2)
    i01.moveHead(79,100)
    i01.moveArm("left",33,84,136,80)
    i01.moveArm("right",34,82,160,13)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",180,180,180,180,180,113)
    i01.moveTorso(90,90,90)
    sleep(2)
    ##arm right up
    i01.moveHead(100,100)
    i01.moveArm("left",33,84,136,80)
    i01.moveArm("right",34,82,160,20)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",92,33,37,71,66,113)
    i01.moveTorso(90,90,90)
    sleep(3)
    i01.moveHead(110,120)
    i01.moveArm("left",33,140,136,80)
    i01.moveArm("right",34,82,170,30)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",92,33,37,71,66,113)
    i01.moveTorso(90,90,90)
    sleep(2)
    i01.moveHead(125,140)
    i01.moveArm("left",33,90,36,60)
    i01.moveArm("right",34,80,170,40)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",92,33,37,71,66,113)
    i01.moveTorso(30,90,90)
    sleep(2)
    ##arm left up
    i01.moveHead(120,130)
    i01.moveArm("left",33,90,36,60)
    i01.moveArm("right",34,65,160,40)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",92,33,37,71,66,113)
    i01.moveTorso(50,90,90)
    sleep(2)
    i01.moveHead(79,100)
    i01.moveArm("left",18,84,54,69)
    i01.moveArm("right",65,78,118,13)
    i01.moveHand("left",92,33,37,71,66,30)
    i01.moveHand("right",180,180,180,180,180,113)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.moveHead(79,100)
    i01.moveArm("left",18,84,55,71)
    i01.moveArm("right",75,80,120,45)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",81,66,82,60,105,113)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 0.85)
    i01.setHeadSpeed(0.9, 0.9)
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(79,160)
    i01.moveArm("left",24,84,32,74)
    i01.moveArm("right",87,82,123,74)
    i01.moveHand("left",0,0,0,0,0,25)
    i01.moveHand("right",0,0,0,0,0,113)
    i01.moveTorso(130,90,90)
    sleep(3)
    i01.moveHead(60,20)
    i01.moveArm("left",87,82,123,74)
    i01.moveArm("right",5,84,32,80)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",81,66,82,60,105,113)
    i01.moveTorso(30,90,90)
    sleep(6)
    i01.setHeadSpeed(1.0,1.0)
    i01.setArmSpeed("left",1.0,1.0,1.0,1.0)
    i01.setArmSpeed("right",1.0,1.0,1.0,1.0)
    i01.moveHead(80,86)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveTorso(90,90,90)
    sleep(2)
    i01.mouth.speakBlocking("wow, I feel good, I love this")
    sleep(2)
    rest()
    sleep(1)
    relax()

def systemcheck():
     sleep(2)
     i01.setHeadSpeed(.75,.75)
     i01.moveHead(90,90)
     sleep(1)
     i01.moveHead(72,64)
 
     sleep(2)
     i01.moveHead(155,94)
     sleep(2)
 
     i01.moveHead(90,138)
     sleep(2)
 
     i01.moveHead(29,95)
     sleep(2)
     i01.moveHead(90,90)
     sleep(1.5)
     i01.mouth.speakBlocking("Head, neck and mouth,   check")
     sleep(1)
     i01.setHeadSpeed(.9,.9)
     i01.moveHead(25,61)
     i01.moveArm("left",0,90,30,10)
     i01.setArmSpeed("right",.75,.75,.75,.75)
     i01.moveArm("right",24,62,52,45)
     i01.moveHand("left",0,0,0,0,0,90)
     i01.moveHand("right",0,0,0,0,0,90)
     sleep(2)
     i01.moveHead(90,90)
     i01.setHeadSpeed(.9,.9)
     sleep(1)
     i01.mouth.speakBlocking("right arm and right shoulder,    check")
     sleep(1)
     i01.setHeadSpeed(.9,.9)
     i01.moveHead(20,122)
     i01.setArmSpeed("left",.75,.75,.75,.75)
     i01.moveArm("left",24,62,52,45)
     sleep(2)
     i01.moveHead(90,90)
     i01.setHeadSpeed(.9,.9)
     sleep(1)
     i01.mouth.speakBlocking("left arm and left shoulder,    check")
     sleep(1)
     i01.setHeadSpeed(.9,.9)
     i01.moveHead(20,120)
 
     i01.moveArm("left",75,123,52,45)
     i01.moveArm("right",75,123,52,45)
     i01.moveHand("left",180,180,180,180,180,30)
     i01.moveHand("right",180,180,180,180,180,170)
     sleep(3)
     i01.setHeadSpeed(.9,.9)
     i01.moveHead(59,67)
 
     i01.moveHand("right",0,0,0,0,0,19)
     i01.moveHand("left",0,0,0,0,0,170)
     sleep(1)
     i01.moveHand("left",180,180,180,180,180,30)
     i01.moveHand("right",180,180,180,180,180,170)
     sleep(1.5)
     i01.moveHead(90,90)
     i01.setHeadSpeed(.9,.9)
     sleep(1)
     i01.mouth.speakBlocking(" hands and Wrists,    check")
     sleep(1)
 
     i01.moveHead(90,90)
     i01.moveArm("left",0,90,30,10)
     i01.moveArm("right",0,90,30,10)
     i01.moveHand("left",0,0,0,0,0,90)
     i01.moveHand("right",0,0,0,0,0,90)
     i01.mouth.speakBlocking("all servos are functioning properly")
     sleep(1.5)
     i01.mouth.speakBlocking("awaiting your commands")
     sleep()
     relax()    
