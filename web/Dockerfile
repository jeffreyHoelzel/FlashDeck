FROM node:20.18.1

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY ./src/styles/ /app/src/styles/
COPY ./src/components/ /app/src/components/

RUN npm config set cache /app/.npm-cache

COPY . .

EXPOSE 3000
CMD ["npm", "start"]