FROM python:3.11.4

ARG UNAME
ARG UID
ARG GID

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ Asia/Tokyo

RUN useradd --shell /bin/bash --uid $UID --non-unique --create-home $UNAME
RUN groupmod --gid $GID --non-unique $UNAME

RUN apt update && apt install -y \
    libmpc-dev \
    expect \
    && apt clean

# set alias
COPY ./.bashrc.local /workspace/.bashrc.local
RUN cat /workspace/.bashrc.local >> /etc/bash.bashrc

USER ${UNAME}
COPY --chown=${UNAME}:${UNAME} ./template.json /workspace/template.json
COPY --chown=${UNAME}:${UNAME} ./template.py /workspace/template.py
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash && \
    export NVM_DIR="$HOME/.nvm" && \
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" && \
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" && \
    nvm install 20 && \
    npm install -g atcoder-cli && \
    ACC_CONFIG_DIR=$(acc config-dir) && \
    mkdir -p $ACC_CONFIG_DIR && \
    mkdir -p $ACC_CONFIG_DIR/py && \
    cp /workspace/template.json $ACC_CONFIG_DIR/py/template.json && \
    cp /workspace/template.py $ACC_CONFIG_DIR/py/main.py && \
    acc config default-template py && \
    acc config default-task-choice all


RUN echo 'export PATH=$HOME/.local/bin:$PATH' >> $HOME/.bashrc && \
    . $HOME/.bashrc
WORKDIR /workspace
