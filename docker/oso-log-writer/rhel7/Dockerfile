# /usr/local/bin/start.sh will start the service

FROM openshifttools/oso-rhel7-ops-base:latest

# Pause indefinitely if asked to do so.
ARG OO_PAUSE_ON_BUILD
RUN test "$OO_PAUSE_ON_BUILD" = "true" && while sleep 10; do true; done || :

ADD scripts/ /usr/local/bin/

RUN yum install -y golang \
                   gcc \
                   git \
                   systemd-libs \
                   systemd-devel && \
    yum clean all

ENV GOBIN=/bin \
    GOPATH=/go

RUN go get github.com/rhdedgar/log-writer && \
    cd /go/src/github.com/rhdedgar/log-writer && \
    go install && \
    cd && \
    rm -rf /go

EXPOSE 8080

# Start processes
CMD /usr/local/bin/start.sh
