FROM node:14-alpine AS development
ENV NODE_ENV development
# Add a work directory
WORKDIR /client
# Cache and Install dependencies
COPY ./package.json /client
COPY ./package-lock.json /client
RUN npm install
# Copy app files
COPY . /client
# Expose port
EXPOSE 3000
# Start the app
CMD [ "npm", "start" ]
