import picamera
from time import sleep
from subprocess import call

time = 5
indidentNumber = 0
videoFolder = "Desktop/Projet3/Camera"

# Fonction to create a video file name
def createVideoFileName():
    incidentNumber += 1
	newFileName = ("Incident_", str(lastVideoFile))
    Print ("New file name is", str(lastVideoFile))
    return newFileName

# Fonction to capture a video
def videoCapture(time):
    # Setup the camera
    with picamera.Picamera() as camera:
        # Create new file name
        fileName = createVideoFileName()
        # Start recording
    	camera.start_recording("pythonVideo.h264")
    	Sleep (time)
    	# Stop recording
    	camera.stop_recording()
    # The camera is now closed.
    Print ("New incident no.", str(lastVideoFile), " as been saved to ", videoFolder, " as ", newFileName, ".h264")
    #Conversion to MP4
    h264ToMp4(fileName)

# Fonction to convert the video file to MP4
def h264ToMp4(fileName):
    command = ("MP4Box -add ", fileName, ".h264 ", fileName, ".mp4")
    call ([command], shell = True)
    print ("Video converted")

videoCapture(time)
