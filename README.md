# Instagram post commenter

An automated bot to participate in Instagram giveaways. This script facilitates interaction with giveaway posts, allowing you to automatically comment on a specific post with random intervals between 1 and 15 minutes.

## ⚠️ Warning

This bot:
- May violate Instagram's terms of service
- May result in account restrictions or blocking
- Should be used at your own risk
- It's recommended to use longer intervals to avoid detection

## 🔧 Prerequisites

- Linux operating system (Ubuntu/Debian)
- Python 3.x installed
- Instagram account

## 📦 Installation

1. Install required system packages:
```bash
sudo apt install python3-venv python3-full
```

2. Clone the repository:
```bash
git clone https://github.com/your-username/Instagram-post-commenter.git
cd Instagram-post-commenter
```

3. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Configure your credentials:
```bash
cp src/config.py.example src/config.py
```
   - Edit `src/config.py` with your data:
     - USERNAME: Your Instagram username
     - PASSWORD: Your Instagram password
     - POST_URL: URL of the post where you want to comment
     - COMMENT_TEXT: The comment you want to post

## 🚀 Usage

1. Activate the virtual environment (if not already activated):
```bash
source venv/bin/activate
```

2. Run the script:
```bash
python src/main.py
```

### Background Execution

To run the bot in the background and save logs:
```bash
nohup python src/main.py > instagram_bot.log 2>&1 &
```

To stop the bot:
```bash
ps aux | grep main.py
kill <PID>
```

## 🛠️ Features

- Automatic login with two-factor authentication support
- Random intervals between comments (1-15 minutes)
- Safety pauses every 10 comments
- Error handling and automatic reconnection
- Detailed activity logging

## 📝 Logs

The bot generates detailed logs including:
- Time of each comment
- Counter of comments made
- Errors and reconnections
- Wait times

## 🤝 Contributing

Contributions are welcome:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⭐ Support

If this project has been helpful to you, consider giving it a star on GitHub.
```

</rewritten_file>
```
