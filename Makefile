FLASK_APP = app/routes
FLASK_PORT = 8000
FLASK_DEBUG = --debug
PROXY_PORT = 8080

run_flask:
	@echo "Запуск Flask приложения..."
	FLASK_APP=$(FLASK_APP) flask run --port $(FLASK_PORT) $(FLASK_DEBUG)

run_proxy:
	@echo "Запуск mitmproxy..."
	mitmproxy -s proxy.py -p $(PROXY_PORT)