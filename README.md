# Discord push rank bot

Simple self-bot for pushing discord rank on any discord server

**Please note that self-bot is against Discord T&C.**

**I am not responsible if your account getting banned or some shit, so do it with your own risk**

## Quick start

### Installation

1. Download project
   ```console
   git clone https://github.com/bayy420-999/Discord-push-rank-bot.git
   ```
2. Go to project directory
   ```console
   cd Discord-push-rank-bot
   ```
3. Install Python dependencies
   ```console
   pip install -r requirements.txt
   ```
4. Preparation done. Now you need to setup the bot configuration

### Setup bot

Get your discord token, different ways:

**First method:**
1. Open your browser and activate developer mode
2. Login your discord account
3. Go to developer mode and click on XHR tab
4. Find `login` request and click
5. Go to `Responses` tab and find token value
6. Copy that token

**Second method:**
1. Make sure that you already login into your discord account
2. Go to `Developers tool` in your browser
3. Find javascript console, and paste code below:
   ```javascript
   (
       webpackChunkdiscord_app.push(
           [
               [''],
               {},
               e => {
                   m=[];
                   for(let c in e.c)
                       m.push(e.c[c])
               }
           ]
       ),
       m
   ).find(
       m => m?.exports?.default?.getToken !== void 0
   ).exports.default.getToken()
   ```
4. Copy the result from console, that's your discord token

Edit `config.ini` file:

1. Open config.ini file with your favorites text editor
2. Find `TOKEN` variable and paste token value that you got earlier
3. The rest of configuration is self-explanatory so i don't need to reiterate it here

> Note: you can go to wordlist directory and change the message that you want to send, each of the message should be separated by double enter

### Run the bot

To run the bot, just type this command in your terminal:

```console
python dc.py
```

Then go to the server that you want to run the bot in, type `gm` to start the bot

> Note: You can change `START_WORD` value inside config.ini file
