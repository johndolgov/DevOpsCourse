IS_READY=True
docker build --build-arg IS_READY=$IS_READY -t server .
docker run -p 8080:8080 -v $(pwd)/content:/content server
