FROM node:21

WORKDIR /app

COPY package.json pnpm-lock.yaml /app/

RUN npm install -g pnpm
RUN pnpm install

EXPOSE 3000

CMD [ "pnpm", "serve:docker" ]
