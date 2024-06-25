import json
from kafka import KafkaConsumer
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

# Kafka consumer configuration
consumer = KafkaConsumer(
    'topic-1',
    bootstrap_servers='13.53.41.31:9092',
    group_id='my-group',
    auto_offset_reset='earliest'
)

# Set up the plot
fig, ax = plt.subplots()
x_data = deque(maxlen=20)  # Store up to 20 data points for the x-axis (time)
y_data = deque(maxlen=20)  # Store up to 20 data points for the y-axis (stock prices)
line, = ax.plot([], [], 'r-', lw=2)

def init():
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 1000)  # Adjust based on expected stock price range
    line.set_data([], [])
    return line,

def update(frame):
    try:
        message = next(consumer)
        stock_data = json.loads(message.value.decode('utf-8'))
        current_time = len(x_data) if x_data else 0
        stock_price = float(stock_data.get('05. price', 0))

        x_data.append(current_time)
        y_data.append(stock_price)

        line.set_data(range(len(x_data)), y_data)
        ax.set_xlim(0, len(x_data))

        print(f"Received message: Key={message.key.decode('utf-8')}, Value={stock_data}")
    except StopIteration:
        pass

    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, init_func=init, blit=True, interval=1000)

plt.xlabel('Time (minutes)')
plt.ylabel('Stock Price')
plt.title('Real-Time Stock Price')
plt.show()
