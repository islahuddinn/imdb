# Use an official Node.js image as the base
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the working directory
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the entire project to the working directory
COPY . .

# Build the React app
RUN npm run build

# Set the environment variable for the backend API endpoint
ENV REACT_APP_API_URL=http://0.0.0.0:8000

# Expose port 80 (you can change it to the appropriate port)
EXPOSE 3000

# Start the React app
CMD ["npm", "start"]
