FROM alpine:3.21 AS assets
WORKDIR /assets
COPY site/ .
FROM nginxinc/nginx-unprivileged:1.27-alpine
COPY --from=assets /assets/ /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080
HEALTHCHECK --interval=15s --timeout=3s --start-period=5s --retries=3 CMD wget -qO- http://127.0.0.1:8080/healthz || exit 1
