# Use an official MongoDB image as the base
FROM mongo

# Set the environment variable to initialize the database
ENV MONGO_INITDB_DATABASE=demo

# Copy the MongoDB initialization script to the container
COPY init-mongo.js /docker-entrypoint-initdb.d/
