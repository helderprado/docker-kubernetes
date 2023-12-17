FROM node:18-alpine

WORKDIR /ex8

COPY package.json ./

RUN npm install

COPY . .

CMD ["npm", "run", "dev"]