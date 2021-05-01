import io
from picamera import PiCamera
import logging
import socketserver
from threading import Condition
from http import server

PAGE="""\
<html>
<head>
<title> Raspberry Pi Camera, Hello </title>
</head>
<body>
<center><h1> Raspberry Pi from Stas </h1></center>
<center><img src = "stream.mjpg" width="640" height="480"></center>
</body>
</html>
"""

class StreamingOutput(object):
        def __init__(self):
            self.frame = None
            self.buffer = io.BytesIO()
            self.condition = Condition()
            
        def write(self,buf):
            if buf.startswith(b'\xff\xd8'):
                