import math
import tweepy
import time
import os
from dotenv import load_dotenv

# 🔐 Load secure credentials from .env
load_dotenv()
API_KEY = os.getenv("X_API_KEY")
API_SECRET = os.getenv("X_API_SECRET")
ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("X_ACCESS_SECRET")

# ✅ Twitter API authentication (legal, permitted, official)
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# 🔥 Jesus Formula constants
LOP = 7.77
TAF = 3.14
ECP = 5.55
UEF = 2.71
WIF = 9.99

# 🌀 Fibonacci function
def fibonacci(n):
    if n <= 0:
        return 1
    elif n == 1:
        return 1
    fib_seq = [1, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[-1]

# 🔁 Collapse pulse calculation using flame recursion
def scroll_signal(n):
    fib_value = fibonacci(n)
    try:
        signal = (
            WIF * ((TAF ** 3 + LOP ** 6 + ECP ** 9) / UEF)
        ) ** (1 / fib_value)
        return round(signal, 6)
    except Exception as e:
        print(f"Error in calculation: {e}")
        return 0

# 🕊️ Format scroll-style output for broadcast or terminal
def generate_scroll_output(pulse_number):
    fib_val = fibonacci(pulse_number)
    signal_val = scroll_signal(pulse_number)
    return f"""📜 Scroll Pulse {pulse_number} 🔁
Harmonic Collapse Index: {fib_val}
Flame Signal: {signal_val}"""

# 🔊 Post or Print
def transmit_scroll(pulse_number, post_to_x=False):
    message = generate_scroll_output(pulse_number)
    print(message)
    if post_to_x:
        try:
            api.update_status(message)
            print("✅ Posted to X")
        except Exception as e:
            print(f"❌ Error posting to X: {e}")

# 🚀 Start pulse loop (adjust range or use while loop for continuous)
if __name__ == "__main__":
    for pulse in range(1, 8):  # You can change 8 to ∞ if looping live
        transmit_scroll(pulse, post_to_x=False)  # Flip to True to activate live
        time.sleep(10)  # Pause between pulses
