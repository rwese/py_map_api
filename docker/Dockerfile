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

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl --head --request GET http://localhost:8000/docs |& grep "200 OK" > /dev/null || exit 1

EXPOSE 8000/TCP