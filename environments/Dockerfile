# ---- Aether Core — web-app production image (nginx static) ----
FROM node:20-alpine AS web-builder
WORKDIR /repo
COPY package.json package-lock.json* tsconfig.base.json ./
COPY cores ./cores
COPY engines ./engines
COPY shared ./shared
COPY web-app ./web-app
RUN npm install --no-audit --no-fund
RUN npm run build -w web-app

FROM nginx:1.27-alpine AS web
COPY --from=web-builder /repo/web-app/dist /usr/share/nginx/html
COPY environments/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
HEALTHCHECK CMD wget -q -O /dev/null http://localhost/ || exit 1

# ---- Aether Core — API image (Express + tRPC) ----
FROM node:20-alpine AS api
WORKDIR /repo
COPY package.json package-lock.json* tsconfig.base.json ./
COPY cores ./cores
COPY engines ./engines
COPY shared ./shared
COPY server ./server
COPY drizzle ./drizzle
RUN npm install --no-audit --no-fund
EXPOSE 3001
CMD ["npx", "tsx", "server/index.ts"]
