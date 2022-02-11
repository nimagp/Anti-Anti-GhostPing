# Anti-Anti-GhostPing
## What it is
A simple (may be ridiculous too) bot to delete messages that Discord Security bot sends when someone mention other member in a message that contains NQN (Not Quite Nitro bot) emotes.  
## Install&Setup
First, get a token from Discord Developer Portal.See this [post](https://realpython.com/how-to-make-a-discord-bot-python/) if you don't know how,Bot needs Manage Messages permission to delete messages.
### Install on your computer
1. Download and install the latest version of Python from [here](https://www.python.org/downloads/).
2. Clone the repository with `git clone https://github.com/nimagp/Anti-Anti-GhostPing.git`.
3. Open the `Anti-Anti-GhostPing` folder and run `pip install -r requirements.txt`.
4. Create '.env' file in the root directory of the project. It should contain the following lines:
```
DISCORD_TOKEN=<your_token>
```
5. Run 'python main.py' in the root directory of the project.
### Heroku/RailWay or Replit
For deploy to these platforms you only need to click on the 'Deploy' or 'Run' button of your platform or if you prefer, deploy project yourself. Then set the `DISCORD_TOKEN` variable in Secrets in Replit or Variables in RailWay and Heroku.

### Deploy badges
[![Run on Repl.it](https://repl.it/badge/github/nimagp/Anti-Anti-GhostPing)](https://repl.it/github/nimagp/Anti-Anti-GhostPing)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Fnimagp%2FAnti-Anti-GhostPing)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

