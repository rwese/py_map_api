FROM --platform=$BUILDPLATFORM python:3.8

# add app-user
RUN useradd -ms /bin/bash app

COPY . /app
WORKDIR /app

USER app
RUN pip install --no-cache-dir -r requirements.txt

ENV PATH="${PATH}:/home/app/.local/bin"
# Allow IPS for RFC1918 ranges
ENV FORWARDED_ALLOW_IPS="10.*,172.16.*,192.168.*"

CMD ["uvicorn", "--app-dir", "/app/src", "main:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000/TCP