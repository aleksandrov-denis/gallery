# About
This is a personal website running on a Raspberry Pi 3

# Features
* Displays system stats
* Showcases some of my software projects

# Setup
You need the following set up in order to run the systemd services used in this project.

## Dependencies

```sudo dnf install python3-pip make; pip3 install flask psutil;```

## Systemd service setup

For system_stats.py, do the following:

```sudo vim /etc/systemd/system/flaskapp.service```

Add the following:

```
[Unit]
Description=Flask App for System Stats
After=network.target

[Service]
User=your_username
WorkingDirectory=path_to_gallery
ExecStart=/usr/bin/python3 path_to_system_stats.py

[Install]
WantedBy=multi-user.target
```
Then enable the service by doing the following:

```sudo systemctl enable flaskapp; sudo systemctl start flaskapp```

For stats_collector.py, do the following:

```sudo vim /etc/systemd/system/stats_collector.service```

Add the following:

```
[Unit]
Description=Background Stats Collection Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 path_to_stats_collector.py
Restart=always
User=your_username

[Install]
WantedBy=multi-user.target
```

Then enable the service by doing the following:

```sudo systemctl enable stats_collector; sudo systemctl start stats_collector```
