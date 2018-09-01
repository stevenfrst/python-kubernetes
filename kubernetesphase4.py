#How To Use This script
#Run python3 kubernetesphase4.py
#You Must Done With kubernetesphase1.py,kubernetesphase2.py,kubernetesphase4.py
import os
import getpass
os.system("mkdir -p $HOME/.kube")
password = getpass.getpass()
os.system("sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config")
password = getpass.getpass()
os.system("sudo chown $(id -u):$(id -g) $HOME/.kube/config")
password = getpass.getpass()
os.system("kubectl apply -f https://raw.githubusercontent=.com/coreos/flannel/master/Documentation/kube-flannel.yml")
os.system("kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/k8s-manifests/kube-flannel-rbac.yml")
print("##################### Important ######################")
print("After This script done you must change this to root")
print("To watch the command for join to cluster from node")
print("you can use this command")
print("kubeadm token create --print-join-command")
print("copy the output from kubeadm token create --print-join-command")
print("Good Luck Have Fun")
print("#########################################")
print("Creator : t.me/stevenfrst")
