
# Simple Web Application with Docker, Nginx Reverse Proxy, and Docker Compose

This project demonstrates a simple web application using **Flask**, managed with **Docker Compose**, and served through an **Nginx** reverse proxy.

### How to Build the Image:

To build the Docker image for the Flask application, use the following command:

```bash
docker build -t roshan-task:v1 -f ./Docker/Dockerfile . --no-cache
```

This will build the Docker image without using any cached layers, ensuring a fresh build.

---

### How to Run the Application:

Once the image is built, run the application using **Docker Compose** with this command:

```bash
docker compose --file Docker/docker-compose.yaml up
```

This will start the Flask application and the Nginx reverse proxy as containers, as defined in the `docker-compose.yaml` file.

