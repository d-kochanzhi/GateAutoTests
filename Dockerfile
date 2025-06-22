FROM joyzoursky/python-chromedriver


WORKDIR /usr/workspace   

COPY ./requirements.txt /usr/workspace

RUN pip3 install -r requirements.txt

