#!/bin/bash
if [ -z "$1" ]; then
	echo "Pass repo, isfoxonit tag and nginx-proxy tag."
	exit 1
fi
docker build -t $1/$2 .
cd nginx-proxy
docker build -t $1/${3} .
cd ../
docker push $1/$2
docker push $1/$3
cat deployment.yaml.tokens | sed "s/%%ISFOXONIT_TAG%%/${1}\/${2}/g" | sed "s/%%NGINX_PROXY_TAG%%/${1}\/${3}/g" > deployment.yaml
kubectl replace -f deployment.yaml
kubectl delete -f service.yaml
kubectl create -f service.yaml
./firewall-rules.gce
