# 🚀 Simple Web Application with Docker, Nginx Reverse Proxy, and Docker Compose  

This project demonstrates a simple web application using **Flask**, managed with **Docker Compose**, and served through an **Nginx** reverse proxy. It's designed to showcase a scalable and efficient deployment setup with modern containerization tools.  

---

## 🌐 Live Preview  

Check out the live version here:  
[**Project Demo**](http://demo.radinpirouz.ir)  

---

## ⚙️ Deploying with Ansible  

You can easily deploy this application using **Ansible**. Follow these steps:  

1. Clone the repository:  
    ```bash
    git clone https://github.com/RadinPirouz/roshan-challenge.git
    cd roshan-challenge/Ansible
    ```
2. Edit `group_vars` to configure DNS and project root directory.  
3. Add your server's IP address to `inventory.ini`.  
4. Run the Ansible playbook:  
    ```bash
    ansible-playbook main.yaml -i inventory.ini -v --become
    ```

---

## 🐳 Docker Version  

This project uses **Docker** to containerize the application and **Nginx** as a reverse proxy to handle traffic efficiently.  

### 🔨 Building the Docker Image  

To build the Docker image for the Flask application, use the following command:  

```bash
docker build -t roshan-task:v1 -f ./Docker/Dockerfile . --no-cache
```

This command builds the Docker image without using cached layers, ensuring a fresh build.  

---

### ▶️ Running the Application  

After building the image, start the application using **Docker Compose**:  

```bash
docker compose --file Docker/docker-compose.yaml up
```

This command will:  
- Start the **Flask** application container.  
- Launch the **Nginx** reverse proxy container.  
- Link them together as defined in the `docker-compose.yaml` file.  

---
