#!/usr/bin/env python3

import rospy
from ogretici_paket.srv import GecenZaman
def gecenZamanFonkisyonu(istek):
    robot_hiz = 0.5
    sure = istek.hedef_konum/robot_hiz
    return sure
    
    
def cevapGonder():
    rospy.init_node("servis_dugumu")
    rospy.Service("zaman",GecenZaman,gecenZamanFonkisyonu)
    rospy.spin()
cevapGonder()