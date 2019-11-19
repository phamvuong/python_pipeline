FROM python:3

WORKDIR /usr/src/app
ENV JENKINS_ID admin
ENV JENKINS_TOKEN 11976eafd2cf8d453d8f0e88e2d31eef9d
ENV JENKINS_ADDR jenkins.devops.internal.com:8080

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["tail", "-f", "/dev/null"]
#CMD ["python", "main.py"]
