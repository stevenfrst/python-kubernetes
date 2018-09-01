#How To Use This script
#Run python3 kubernetesphase2.py
#You Must Done With kubernetesphase1.py
import os
os.system("apt install telnetd -y")
os.system("/etc/init.d.open-bsd-inetd restart")
print("IP YANG DIAMBIL ADALAH IP \n")
print("KAU SAMBUNGKAN UNTUK MEMBUKA DASHOARD \n")
print("Good Luck Have Fun \n")
apiserverip = input("Enter Your IP for Your API apiserver   : ")
os.system("sudo kubeadm init --pod-network-cidr=10.244.0.0/16 --apiserver-advertise-address=",(apiserverip))
print("You Must Copy The Output From kubeadm init")
print("Good Luck Have Fun")
