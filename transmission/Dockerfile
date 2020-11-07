FROM arm64v8/python:alpine
LABEL maintainer="kh.grandi@gmail.com"

RUN apk update && apk upgrade &&  apk --update --no-cache add transmission-daemon

COPY app /
RUN mkdir /downloads && mkdir /incomplete-downloads && mkdir -p /var/log/transmission


VOLUME /downloads
VOLUME /incomplete-downloads
VOLUME /app
VOLUME /var/log/transmission
VOLUME /etc/transmission-daemon

EXPOSE 9091 51413/tcp 51413/udp

CMD ["python", "/app/transmission.py"]