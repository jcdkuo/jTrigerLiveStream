# -*- coding: UTF-8 -*-
import sys
import getopt
import paho.mqtt.client as mqtt   # pip3 install paho-mqtt
from config import Config
from topic  import Topic
from youtubelive import YoutubeLive
import threading as td
#from facebooklive import FacebookLive

# Initialization
conf    = Config()
topic   = Topic()
youtube = YoutubeLive()
#facebook = FacebookLive()


def on_connect(client, userdata, flags, rc):
    print("Connected to {0} with result code {1}".format(conf.Host, rc))
    # Subscribe to LiveStream topics
    client.subscribe(topic.AllLiveStream)


def on_message(client, userdata, msg):
    print("Message received on topic {0}: {1}".format(msg.topic, msg.payload))
    if (msg.topic.startswith(topic.YoutubeTopics) == True):
        print("livestream = YoutubeLive()")
        #youtube.process(msg.topic)
        t1 = td.Thread(target=youtube.process, args=(msg.topic,))
        print ('Thread start .') 		
        t1.start()
        print ('Thread start ..')
        t1.join()  
        print ('Thread after join ...')
    elif (msg.topic.startswith(topic.FacebookTopics) == True):
        #facebook.process(msg.topic)
        print("livestream = FacebookLive()")
    else:
        print("The topic doesn't support")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect(conf.Host, conf.Port, conf.Timeout)
client.loop_forever()
