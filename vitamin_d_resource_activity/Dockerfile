# syntax=docker/dockerfile:1

# Set base image
FROM node:16-slim

# Create app directory
WORKDIR /usr/src/app

# Copy dependencies
COPY package*.json ./

# Install dependencies
RUN npm install
# For production
# RUN npm ci --only=production

# Bundle app
COPY . .

# Start app
CMD ["npm", "start"]
