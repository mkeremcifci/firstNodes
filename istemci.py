#!/usr/bin/env python3

import rospy
from ogretici_paket.srv import GecenZaman

def istekteBulunma(x):
    print("Servis bekleniyor")
    rospy.wait_for_service("zaman")
    print("Servise bağlanıldı")
    try:
        servis = rospy.ServiceProxy("zaman",GecenZaman)
        cevap = servis(x)
        return cevap.gecen_sure
    except rospy.ServiceException:
        print("Serviste hata oluştu !!!")

hedef = int(input("Hedef konum giriniz:"))
t = istekteBulunma(hedef)
print("Hedefe varana kadar geçen süre: ",t)
