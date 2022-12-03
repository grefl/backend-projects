# Build an image from scatch

Follow these instructions here -> https://docs.docker.com/build/building/base-images/ 

But a cheat sheet would be as follows:

1. Git pull this [repo](https://github.com/docker-library/hello-world) and run the `./update.sh --static` command
2. Once the build is complete, you can cd into the architecture of your choice (example, `cd amd64/hello-world`) and run `docker build --tag hello .`
3. Then run `docker run --rm hello`

That's it


