#FROM node:14-alpine
FROM docker:dind

#RUN npm i

CMD [ "tail", "-f", "/dev/null"]


