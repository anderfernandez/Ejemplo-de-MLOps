FROM tiangolo/uvicorn-gunicorn-fastapi
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./api api/
COPY ./outputs outputs/
EXPOSE 8080
CMD ["uvicorn", "api.api:app", "--host", "0.0.0.0", "--port", "8080"]
