FROM python:3.9-slim

WORKDIR /src
COPY . /src
COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# EXPOSE 9004

# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9004"]

