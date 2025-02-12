FROM httpd:2.4

RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN echo "Include conf/vhosts.conf" >> /usr/local/apache2/conf/httpd.conf

ARG CONFIG_FILE

COPY ${CONFIG_FILE} /usr/local/apache2/conf/vhosts.conf