FROM nginx:latest
COPY nginx.conf /etc/nginx/nginx.conf
COPY seangollschewsky.me /etc/nginx/sites-enabled/
COPY www/seangollschewsky.me /var/www/seangollschewsky.me
COPY isfoxonit.duckdns.org /etc/nginx/sites-enabled/
COPY www/isfoxonit.duckdns.org /var/www/isfoxonit.duckdns.org
COPY gollo.me /etc/nginx/sites-enabled/
COPY www/gollo.me /var/www/gollo.me
COPY default /etc/nginx/sites-enabled/
COPY www/html /var/www/html
COPY letsencrypt/ /etc/letsencrypt
