install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black *.py 

lint:
	ruff check *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

# Build Docker container and deploy it (this is just an example for Docker)
deploy:
	@echo "Deploying application..."
	docker build -t my-app .
	docker run -d -p 80:80 my-app

# If you're deploying using Heroku, you can uncomment and use this
# deploy:
# 	@echo "Pushing to Heroku..."
# 	git push heroku main

# This command runs all the essential checks and tests before deployment
all: install lint test format

# If you want to combine multiple tasks for deployment
pre-deploy: install refactor test

# A combined rule that runs all necessary tasks before deployment
deploy-all: pre-deploy deploy
