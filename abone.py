#!/usr/bin/env python3
import rospy
from ogretici_paket.msg import BataryaDurum

def bataryaFonksiyonu(mesaj):
    rospy.loginfo("Batarya durumu:%s"%mesaj.batarya)
    

def mesajYakala():
    rospy.init_node("abone_dugumu")
    rospy.Subscriber("batarya_konusu",BataryaDurum,bataryaFonksiyonu)
    rospy.spin()

mesajYakala()