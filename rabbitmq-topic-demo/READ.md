i🎯 🧠 Project Goal

We simulate logs/events:

app.error
app.info
db.error
db.info
payment.success
payment.failed

And route them to different consumers based on patterns.



🏗️ Project Structure
rabbitmq-topic-demo/
│
├── docker-compose.yml
├── producer/
│   └── producer.py Dockerfile
├── consumer_error/
│   └── consumer_error.py Dockerfile
├── consumer_all/
│   └── consumer_all.py Dockerfile
├── consumer_payment/
│   └── consumer_payment.py Dockerfile


🚀 Run Project
docker-compose up --build
