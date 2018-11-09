# /usr/local/bin/start.sh will start the service

FROM openshifttools/oso-centos7-ops-base:latest

# Pause indefinitely if asked to do so.
ARG OO_PAUSE_ON_BUILD
RUN test "$OO_PAUSE_ON_BUILD" = "true" && while sleep 10; do true; done || :

#RUN yum install -y golang && \
#    yum clean all
#
#ENV GOLANG_VERSION=1.9 \
#    GOPATH=/go
#
#ENV PATH=$GOPATH/bin:/usr/local/go/bin:$PATH
#
#COPY go-wrapper /usr/local/bin/
#
#RUN go get -u github.com/openshift/sre-dashboard
#WORKDIR /go/src/github.com/openshift/sre-dashboard
#
#RUN go-wrapper download && go-wrapper install
#
EXPOSE 8080

USER 1001

COPY dashboard/ /usr/local/bin/

# Start processes
#CMD ["go-wrapper", "run"]
#CMD ["/usr/local/bin/sre-dashboard"]
CMD /usr/local/bin/start.sh
