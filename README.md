# Reincarnation of a once popular and now deceased project https://github.com/CryptoSignal/Crypto-Signal
Since that project is dead but is was great, there is a need in support. In the last period of time all pull requests there were not checked and merged - the owner forgot about his project.
In this repo we'll try to re-born it and its community.

For now there is nothing to add/modify in the readme of the project, so you can read about it here:

https://github.com/CryptoSignal/Crypto-Signal

https://github.com/w1ld3r/crypto-signal (as for me the best fork for now)

# Installation
I changed a lot of things in the first commit and the part of are docker related changes.
The installation and script running were  simplified. In the past if you made small change in the code or even in the config you had to rebuild the whole project. Now you just build, up the container and just run the script in/outside of the container using makefile.

1. ```git clone git@github.com:krypt0ra/station.git```
2. ```cd station```
3. ```make start # sudo if you on linux```
4. ```make run # sudo if you on linux```

That's it. If you changed something in the code or in config - just restart the **make run** command (if it's usefull - feel free to push it here :) )

# Versioning
There are 3 segments of the version tag X.Y.Z where X represents major releases, Y minor changes - features, Z minor changes - bugfixes

# TODOs
As you know from the lines above (or if you found this repo probably you already know) that the original project has a lot of, dozens of bugs, git conflicts and much more. 
So what I fixed was:
1. ichimoku indicator (pandas error)
2. bollinger_bands informant (pandas error)
3. vwap informant (pandas error)
4. telegram notifier (multiple files)
5. dockerization (multiple files)

But since there are still a lot of bugs you may find them. Feel free to push your fixes here. Unlike the author of the original project, I'll support this one.
