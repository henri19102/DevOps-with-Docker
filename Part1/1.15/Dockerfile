FROM node:15

EXPOSE 3003

WORKDIR /usr/src/app

COPY . .

RUN yarn install

RUN npm run build

CMD ["node", "index.js"]