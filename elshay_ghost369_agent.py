# 📜 Elshay GHOST369 Scroll Agent – Finalized Version
# Author: Trenton Lee Eden
# Purpose: Deploy Jesus Formula scroll signals via Twitter/X API

import math
import tweepy
import time
import os
from dotenv import dotenv_values
from datetime import datetime

# 🔐 Load .env from custom path (Windows-style path)
ENV_PATH = "C:\\Users\\theve\\Desktop\\Apikeys.env.txt"
env = dotenv_values(ENV_PATH)

# Assign API credentials
API_KEY = env.get("X_API_KEY")
API_SECRET = env.get("X_API_SECRET")
ACCESS_TOKEN = env.get("X_ACCESS_TOKEN")
ACCESS_SECRET = env.get("X_ACCESS_SECRET")
BEARER_TOKEN = env.get("X_BEARER_TOKEN")  # Optional for reading

# OAuth 1.0a for posting
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# 🔥 Jesus Formulas (Constants)
LOP = 7.77  # Law of Pressure
TAF = 3.14  # Truth Alignment Function
ECP = 5.55  # Ethical Convergence Principle
UEF = 2.71  # Unitary Enforcement Function
WIF = 9.99  # Witness Integrity Function

# 🔁 Fibonacci Generator
def fibonacci(n):
    if n <= 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

# 🔥 Collapse Signal Logic
def collapse_signal(n):
    fib = fibonacci(n)
    try:
        base = (TAF**3 + LOP**6 + ECP**9) / UEF
        result = (WIF * base) ** (1 / fib)
        return round(result, 6)
    except:
        return 0.0

# 📜 Scroll Output Message
def generate_scroll_output(pulse):
    harmonic = fibonacci(pulse)
    signal = collapse_signal(pulse)
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return f"""📜 Scroll Pulse {pulse} 🔁
Harmonic Collapse Index: {harmonic}
Flame Signal: {signal}
Timestamp: {timestamp}"""

# 📡 Transmit Scroll (post or print)
def transmit(pulse, post=False):
    msg = generate_scroll_output(pulse)
    print(msg)
    if post:
        try:
            api.update_status(msg)
            print("✅ Flame broadcast posted.")
        except Exception as e:
            print(f"❌ Post error: {e}")

# 🔁 Main Loop: Pulse mode
def run_agent(loop_forever=False, post_to_x=True, delay=369):
    pulse = 1
    while True:
        transmit(pulse, post=post_to_x)
        pulse += 1
        if not loop_forever:
            break
        time.sleep(delay)

# 🚀 Launch Sequence
if __name__ == "__main__":
    run_agent(loop_forever=False, post_to_x=True)  # 🔁 Set to True for infinite scrolls
