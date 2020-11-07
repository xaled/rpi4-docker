FROM arm64v8/python:alpine
LABEL maintainer="kh.grandi@gmail.com"

RUN pip install --no-cache-dir pyftpdlib

RUN mkdir /data
RUN mkdir /var/log/pyftpd

# COPY run_pyftpd.py /usr/bin/

VOLUME /data
VOLUME /app
VOLUME /var/log/pyftpd

EXPOSE 20 21 21100-21110

#CMD ["python","/usr/bin/run_pyftpd.py" ]
CMD ["python","/app/run_pyftpd.py" ]