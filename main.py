import json
import detector


camerawindow = { "height": 600, "width": 800}

colors = json.load(open("colors.json"))

#window, player1colors, player2colors
# detector.cameraLoop(camerawindow, colors["pink"], colors["orange"])
detector.cameraLoop(camerawindow, colors["pink"], None)

