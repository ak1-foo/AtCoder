FROM python:3.11.4

ARG UNAME
ARG UID
ARG GID

ENV DEBIAN_FRONTEND=noninteractive

RUN useradd --shell /bin/bash --uid $UID --non-unique --create-home $UNAME
RUN groupmod --gid $GID --non-unique $UNAME

RUN apt update && apt install -y \
    libmpc-dev \
    && apt clean

USER ${UNAME}
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash && \
    export NVM_DIR="$HOME/.nvm" && \
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" && \
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" && \
    nvm install 20 && \
    npm install -g atcoder-cli

RUN echo 'export PATH=$HOME/.local/bin:$PATH' >> $HOME/.bashrc && \
    . $HOME/.bashrc
WORKDIR /workspace
