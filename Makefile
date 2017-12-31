default: docker_build

deploy:
	curl -X GET https://seangollschewsky.me/hosts -o hosts
	ansible-playbook -i hosts playbook.yml --ask-sudo-pass --extra-vars "{ "version": "`cat VERSION`" }"

push:
	docker push gollo/isfoxonit:`cat VERSION`

docker_build:
	docker build \
		--build-arg VCS_REF=`git rev-parse --short HEAD` \
		--build-arg BUILD_DATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` \
		--build-arg VERSION=`cat VERSION` -t gollo/isfoxonit:`cat VERSION` .
	curl -X POST https://hooks.microbadger.com/images/gollo/isfoxonit/mIPyied0w7E9leHdxeBZO98rsvc=

