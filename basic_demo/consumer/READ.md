### What is RabbitMQ (Simple Explanation)
Think of RabbitMQ like a post office 📮
* Producer (Sender) → Sends message (like a letter)
* Queue (Mailbox) → Stores messages
* Consumer (Receiver) → Reads messages
👉 Instead of apps talking directly, they communicate via RabbitMQ.


🏗️ Core Concepts
1. Producer
    Sends messages
    Example: Your backend app sending order data
2. Queue
    Temporary storage
    Messages wait here until processed
3. Consumer
    Reads messages from queue
    Example: Payment service processing orders
4. Exchange (Important)
    Routes messages to queues
    -Types:
        Direct
        Fanout
        Topic


################################################

🛠️ Hands-on POC (Linux Mint)

* Step 1: Install RabbitMQ
    sudo apt update
    sudo apt install rabbitmq-server -y

Start service:

    sudo systemctl start rabbitmq-server
    sudo systemctl enable rabbitmq-server

Check status:

    sudo systemctl status rabbitmq-server
* Step 2: Enable Web UI (Very Useful 🔥)
    sudo rabbitmq-plugins enable rabbitmq_management

Access in browser:
    http://localhost:15672

Default login:
    username: guest
    password: guest

* Step 3: Install Python Library

    We’ll simulate producer & consumer.

        sudo apt install python3-pip -y
        pip3 install pika


🧪 Demo 1: Simple Queue (Producer → Consumer)

📤 Producer Script

Create file: vim producer.py
    Code is mentioned in repo

📥 Consumer Script

Create file: vim consumer.py
    Code is mentioned in repo


▶️ Run Demo

Terminal 1:
python3 consumer.py
Terminal 2:
python3 producer.py

👉 Output:

[x] Sent 'Hello RabbitMQ!'
[x] Received b'Hello RabbitMQ!'

