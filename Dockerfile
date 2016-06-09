FROM aexea/aexea-base:py3.5

EXPOSE 8042

USER root

ADD requirements.txt /opt/code/requirements.txt
WORKDIR /opt/code
RUN pip3 install --find-links=http://pypi.qax.io/wheels/ --trusted-host pypi.qax.io -Ur requirements.txt
ADD . /opt/code

RUN chown -R uid1000: /opt

WORKDIR /opt/code/channelsexample

USER uid1000
