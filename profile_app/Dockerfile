FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /src
COPY requirements.txt /src/
RUN pip3 install -r requirements.txt
COPY . /src/
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
