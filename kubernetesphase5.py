import os
os.system("kubectl create -f https://git.io/kube-dashboard kubectl proxy")
os.system("ssh -L 8001:127.0.0.1:8001 -N")
