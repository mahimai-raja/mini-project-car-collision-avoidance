import jetson.inference
import jetson.utils

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0")
display = jetson.utils.videoOutput()

while True :
    img = camera.Capture()
    detections = net.Detect(img)

    for detection in detections:
        print(net.GetClassDesc(detections[0].ClassID))
        with open('readme.txt', 'w') as f:
            f.write(net.GetClassDesc(detections[0].ClassID))
    display.Render(img)
    display.SetStatus("Object Detection | Network {:.0f}FPS".format(net.GetNetworkFPS()))