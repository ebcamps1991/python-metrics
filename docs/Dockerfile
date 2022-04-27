FROM python:3.7

RUN apt update \
    && apt install -y default-jre fonts-font-awesome python-pydot

RUN mkdir -p /opt/docs \
    && chmod a+w -R /opt/docs

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /opt/docs

# Getting the plantuml binary
RUN mkdir -p /bin \
    && wget https://github.com/plantuml/plantuml/releases/download/v1.2022.4/plantuml-1.2022.4.jar -O /bin/plantuml.jar

CMD ["sphinx"]