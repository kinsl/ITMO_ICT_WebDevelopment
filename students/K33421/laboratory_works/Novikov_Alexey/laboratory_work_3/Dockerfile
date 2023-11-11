FROM python:3.11.6-slim-bookworm as base

WORKDIR /src
COPY requirements.txt /src/

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

FROM base as installer

RUN apt update && apt install --no-install-recommends -y build-essential libpq-dev
RUN pip wheel --no-cache-dir --wheel-dir /src/wheels -r requirements.txt

FROM base as runtime

RUN apt update && \
    apt install --no-install-recommends -y libpq-dev locales && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

RUN echo "ru_RU.UTF-8 UTF-8" >> /etc/locale.gen && locale-gen

COPY --from=installer /src/wheels/ /wheels/
RUN pip install --no-cache /wheels/*

COPY ./src/ .

CMD ["gunicorn", "-c", "delivery/gunicorn.conf.py", "delivery.wsgi:application"]