# Setting Things Up

The following steps are a quick and dirty way to get things started. 
This will launch our containerized app inside a kubernetes cluster using
minikube.

### 1. Pre-Requisites: 
- MacOS Big Sur (or later)
- Docker Desktop v4.11.0+
  - Download: https://docs.docker.com/desktop/install/mac-install/
- Minikube v1.28.0+
  - Run: `brew install minikube`
- Helm v3.10.0+
  - Run: `brew install helm`

<br>

### 2. Quick Setup Steps:
From your project root, follow the steps below:
1. Start Minikube:
   - `minikube start`
1. Build a local image inside minikube:
   - `minikube image build -t glia-image ./app` 
1. Use Helm to build manifest files needed to deploy our app:
   - `helm install glia-helm ./helm`
1. Get the URL to the service connecting to our app  
 (Command should open up your default browser)
   - `minikube service glia-app`
1. Append `/docs` to the URL to get access to the swagger-ui to play around APIs.
1. (Optional) To Clean up:
   - `minikube stop`
