# Reincarnation of a once popular and now deceased project https://github.com/CryptoSignal/Crypto-Signal
Since that project is dead but is was great, there is a need in support. In the last period of time all pull requests there were not checked and merged - the owner forgot about his project.
In this repo we'll try to re-born it and its community.

For now there is nothing to add/modify in the readme of the project, so you can read about it here:

https://github.com/CryptoSignal/Crypto-Signal

https://github.com/w1ld3r/crypto-signal (as for me the best fork for now)

# Contact
If there is a problem related with the project first you can try the official discord of original project: 
https://discord.gg/MWTJVFf

Otherwise you can create an issue here with your questions. I'm active in github.

# Installation
I changed a lot of things in the first commit and the part of are docker related changes.
The installation and script running were  simplified. In the past if you made small change in the code or even in the config you had to rebuild the whole project. Now you just build, up the container and just run the script in/outside of the container using makefile.

1. ```git clone git@github.com:krypt0ra/station.git```
2. ```cd station```
3. ```make start # sudo if you on linux```
4. ```make run # sudo if you on linux```

You can set which exchanges to handle with **make run** command by: ``` make run exchanges=binance,bybit ```. This is useful if you want to parse data from tens of exchanges but want to use different station instances connected with one redis pubsub. REMEMBER to enable that exchanges from config.yml AND THEN to filter.
For example you can enable binance, bybit and bingx in config.yml and run 3 different **make run** commands like: ```make run exchanges=binance``` and ```make run exchanges=bybit``` and ```make run exchanges=bingx```
By this way you will have faster data parsing and publishing into redis

That's it. If you changed something in the code or in config - just restart the **make run** command (if it's usefull - feel free to push it here :) )

# Versioning
There are 3 segments of the version tag X.Y.Z where X represents major releases, Y minor changes - features, Z minor changes - bugfixes

# New features this child-project has
- Fully optimized and fixed dockerization. Run this project just by once command.
- Started since 02 Oct 2024 Redis pubsub notifier is available. You can create multiple connections and use RedisNotifier as a publisher to the channel which was set in config.yml
- Filterable exchanges from command line such as: ```make run exchanges=binance,bingx```. Useful when you want parse from tens of exchanges but in parallel

# TODOs

## These are FIXED!
As you know from the lines above (or if you found this repo probably you already know) that the original project has a lot of, dozens of bugs, git conflicts and much more. 
So what I fixed was:
1. ichimoku indicator (pandas error)
2. bollinger_bands informant (pandas error)
3. vwap informant (pandas error)
4. telegram notifier (multiple files)
5. dockerization (multiple files)

But since there are still a lot of bugs you may find them. Feel free to push your fixes here. Unlike the author of the original project, I'll support this one.
