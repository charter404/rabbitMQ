🧪 RabbitMQ + FastAPI Integration


⚙️ Step 1: Setup Project
mkdir rabbitmq-fastapi
cd rabbitmq-fastapi

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install fastapi uvicorn pika


📤 Step 2: FastAPI Producer (API Service)

Create file:
nano app.py


▶️ Run FastAPI
uvicorn app:app --reload

Open:

http://127.0.0.1:8000/docs

👉 Use /send API to push messages

📥 Step 3: Worker (Consumer Service)

Create:

nano worker.py


▶️ Run Worker
python worker.py
🔥 Test Flow

* Start RabbitMQ
* Start worker
* Start FastAPI

Send request:

curl -X POST "http://127.0.0.1:8000/send" \
-H "Content-Type: application/json" \
-d '{"task":"process order","id":1}'

👉 You’ll see worker processing it asynchronously 🎯
