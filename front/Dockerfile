FROM node:21

WORKDIR /app

COPY package.json pnpm-lock.yaml /app/

RUN npm install -g pnpm
RUN pnpm install
RUN pnpm build

EXPOSE 3000

CMD [ "pnpm", "preview", "--host", "3000"]
