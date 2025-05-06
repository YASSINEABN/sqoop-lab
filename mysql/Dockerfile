FROM mysql:8.0

# Set environment variables
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=employees
ENV MYSQL_USER=sqoop
ENV MYSQL_PASSWORD=sqoop123

# Copy initialization scripts
COPY init/*.sql /docker-entrypoint-initdb.d/

# Set permissions for initialization scripts
RUN chmod -R 644 /docker-entrypoint-initdb.d/*

# Use native password authentication
CMD ["--default-authentication-plugin=mysql_native_password"]
