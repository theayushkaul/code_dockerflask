# Flask CSV Upload App in Docker

This repository contains a simple Flask application that allows users to upload CSV files. The app is containerized using Docker for easy setup and deployment.

## Features
- Upload CSV files via a web interface.
- Run the app locally using Docker and Docker Compose.

---

## Prerequisites

Before you start, ensure that you have the following installed on your system:
- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## Setup Instructions

Follow these steps to get the application running:

### 1. Clone the Repository
First, clone this repository to your local machine:

```bash
git clone https://github.com/theayushkaul/code_dockerflask.git
```
Navigate into the directory 
```bash
cd code_dockerflask
```
### 2. Build and Run the Application

#### Step 1: Build the Docker image
```bash
docker build -t flask-app .
```
#### Step 2: Run the Docker Container
```bash
docker run -p 5000:5000 flask-app
```
This command will:
- Build the Docker image for the Flask application.
- Start the application and expose it on port 5000.
### 3. Access the Application
Once the containers are running, open your browser and go to:
```bash
http://localhost:5000
```
You should see the file upload form. Use it to upload CSV files.