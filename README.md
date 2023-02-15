### Development

Uses the default Django development server.

1. Rename _.env.dev-sample_ to _.env.dev_.
1. Update the environment variables in the _docker-compose.yml_ and _.env.dev_ files.
1. Build the images and run the containers:

   ```sh
   $ docker-compose up -d --build
   ```

   Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.

### Production

Uses gunicorn + nginx.

1. Rename _.env.prod-sample_ to _.env.prod_ and _.env.prod.db-sample_ to _.env.prod.db_. Update the environment variables.
1. Build the images and run the containers:

   ```sh
   $ docker-compose -f docker-compose.prod.yml up -d --build
   ```

   Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.
