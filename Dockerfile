# Use a lightweight NGINX image
FROM nginx:1.25-alpine

# Set metadata
LABEL maintainer="Prawjal Jogi"

# Remove default nginx static files
RUN rm -rf /usr/share/nginx/html/*

# Copy the static web application files from the src directory
COPY ./src /usr/share/nginx/html

# Expose port 80 for HTTP traffic
EXPOSE 80

# Add a healthcheck to ensure the container is running properly
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD wget -q -O - http://localhost/ || exit 1

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]