from flask import Flask, render_template, request
import time
import random
from datetime import datetime

vazhas = Flask(__name__)

excuses = [
    "I needed to check if my plants were thriving.",
    "My pet wanted to have a deep conversation.",
    "I was practicing my skills in avoiding responsibility.",
    "I lost track of time while reorganizing my bookshelf.",
    "I had to take a moment to meditate on my life choices.",
    "I'll start tomorrow.",
    "I work better under pressure.",
    "I don't have enough time.",
    "I'm waiting for the right moment.",
    "I need to do more research first.",
    "I'll do it when I feel inspired.",
    "It's not a priority right now.",
    "I can't find the right resources."
]

distractions = [
    "Scrolling through social media.",
    "Watching cat videos.",
    "Reading random Wikipedia articles.",
    "Getting lost in YouTube rabbit holes.",
    "Contemplating the meaning of life.",
    "Social media and notification.",
    "Phone calls and text messages.",
    "Frequently checking emails.",
    "Noise and environmental factors."
]

class ProcrastinationTracker:
    def __init__(self):
        self.procrastination_log = []
        self.start_time = None

    def start_procrastination(self):
        self.start_time = time.time()
        return "Procrastination started!"

    def stop_procrastination(self):
        if self.start_time is None:
            return "You haven't started procrastinating yet!"
        
        end_time = time.time()
        duration = end_time - self.start_time
        self.procrastination_log.append({
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'duration': duration
        })
        self.start_time = None
        return f"You procrastinated for {duration:.2f} seconds."

    def generate_excuse(self):
        return random.choice(excuses)

    def log_distraction(self):
        return random.choice(distractions)

    def view_log(self):
        return self.procrastination_log

tracker = ProcrastinationTracker()

@vazhas.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'start':
            message = tracker.start_procrastination()
        elif action == 'stop':
            message = tracker.stop_procrastination()
        elif action == 'excuse':
            message = tracker.generate_excuse()
        elif action == 'distraction':
            message = tracker.log_distraction()
        elif action == 'view_log':
            log_entries = tracker.view_log()
            return render_template('log.html', log_entries=log_entries)
        
    return render_template('index.html', message=message)

if __name__ == '__main__':
    vazhas.run(debug=True)  # Fixed this line
