FROM python:3.7.9-stretch
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg
COPY . .
CMD ["python", "./transcoder.py"]