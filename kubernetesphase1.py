#how to use this script
#Just Say Bismillah before start to get Barokah
#and then type python3 kubernetes.py
#this script help CLI user who hate typing manual :)
#Creator Steven Humam
#Must Be Root :)

import os
os.system("apt-get update && apt-get install -y transport-https")
os.system("apt install docker.io")
os.system("systemctl start docker")
os.system("systemctl enable docker")
os.system(" apt-get update \ ")
os.system("&& apt-get install -y apt-transport-https \ ")
os.system("&& curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -")
os.system("echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" \ ")
os.system("|  tee -a /etc/apt/sources.list.d/kubernetes.list \ ")
os.system("&&  apt-get update")
os.system("apt-get update")
os.system(" apt-get update \ ")
os.system("&&  apt-get install -y \ ")
os.system("kubelet \ ")
os.system("kubeadm \ ")
os.system("kubernetes-cni")
os.system("curl -sL https://gist.githubusercontent.com/alexellis/7315e75635623667c32199368aa11e95/raw/b025dfb91b43ea9309ce6ed67e24790ba65d7b67/kube.sh | sh")
os.system("swapoff -a")
print("################################################# \n")
print("## After That You can run kubernetesphase2.py #### \n")
print("#################################################")
