# Docker + MLOps: Real-World Practice Example

This project demonstrates how to containerize a basic data science training script using Docker as part of an MLOps pipeline. The script loads a dataset, performs basic processing, and can be deployed as a Docker image.

---

## 📁 Project Structure

mlops-project/
├── data/
│ └── sample.csv
├── app.py
├── requirements.txt
└── Dockerfile


---

## 🐍 Step 1: `app.py` – Minimal Training Script

```python
import pandas as pd

df = pd.read_csv("data/sample.csv")
print("Rows:", len(df))
print("Summary:")
print(df.describe(include='all'))


---

## 🐍 Step 1: `app.py` – Minimal Training Script

```python
import pandas as pd

df = pd.read_csv("data/sample.csv")
print("Rows:", len(df))
print("Summary:")
print(df.describe(include='all'))

📦 Step 2: requirements.txt
pandas==2.2.2
🐳 Step 3: Dockerfile
FROM python:3.10-slim

WORKDIR /mlapp

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
🚀 Step 4: Build, Run, and Push Docker Image
🔨 Build Docker Image
docker build -t srinathk/mlops-dataset-app .
Run the Container Locally
docker run srinathk/mlops-dataset-app
☁️ Push Image to Docker Hub
docker push srinathk/mlops-dataset-app
📌 Notes
Make sure Docker is installed and running on your machine.

Use GitHub to store your project files (excluding large datasets).

Version your Docker images with tags like :v1, :v2, etc., for better control.
👨‍💻 Author
MLOps Specialist
GitHub: srinathk
Docker Hub: srinathk


---

✅ Just create a file named `README.md` in your project folder and paste this entire content.

Let me know if you want me to generate a sample `.gitignore` or GitHub Actions workflow file next!



