pip install gunicorn psycopg2-binary python-dotenv
pip freeze > requirements.txt
# Manually remove the python-dotenv line from requirements.txt (Render injects env vars directly)