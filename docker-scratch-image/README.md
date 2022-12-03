# Build an image from scatch


1. You should follow this guide on the Docker docs website https://docs.docker.com/build/building/base-images/
2. The key will be to pull this [repo](https://github.com/docker-library/hello-world) and run the `./update.sh --static` command
3. Once built you can cd into the architecture of your choice and run `docker build --tag hello .`
4. Then run `docker run --rm hello`


