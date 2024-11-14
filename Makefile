FLASKAPP = flaskapp
STATS_COLLECTOR = stats_collector

# Restart both services
restart:
	sudo systemctl restart $(FLASKAPP) $(STATS_COLLECTOR)

# Restart flaskapp
restart-flaskapp:
	sudo systemctl restart $(FLASKAPP)

# Restart dtats collector
restart-collector:
	sudo systemctl restart $(STATS_COLLECTOR)

# Check status of both services
status:
	sudo systemctl status $(FLASKAPP) $(STATS_COLLECTOR)
