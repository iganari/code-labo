FROM node:16.9-alpine3.14

WORKDIR /app

# RUN apk update && \
#     npm install && \
#     npm install -g npm && \
#     npm install -g vue-cli

RUN apk update
RUN apk add git openssh
# RUN npm install
RUN npm install -g npm
RUN npm install -g vue@next
RUN npm install -g @vue/cli
