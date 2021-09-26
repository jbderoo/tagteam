FROM ubuntu

RUN apt-get update && \
    apt-get install -y \
    zip unzip \
    tmux \
    python3-venv \
    vim \
    wget \
    git

#RUN mkdir -p /root/projects/tagteam
RUN git init /root/projects/tagteam
RUN git config --global user.email "jderoo@rams.colostate.edu"
RUN git config --global user.name "Jacob DeRoo"

WORKDIR /root/projects/tagteam


RUN python3 -m venv .venv

COPY . .
COPY .ssh/* /root/.ssh/

CMD ["/bin/bash"]
