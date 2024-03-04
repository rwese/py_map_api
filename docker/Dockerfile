FROM --platform=$BUILDPLATFORM python:3.12

# add app-user
RUN useradd -ms /bin/bash app

COPY . /app
WORKDIR /app

USER app
RUN pip install --no-cache-dir -r requirements.txt

ENV PATH="${PATH}:/home/app/.local/bin"
# Allow IPS for RFC1918 ranges
ENV FORWARDED_ALLOW_IPS="10.*,172.16.*,192.168.*"

CMD ["python", "/app/src/main.py"]

EXPOSE 8000/TCP