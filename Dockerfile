ARG PYTHON_VERSION=3.12-slim
FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex \
    && pip install --upgrade pip \
    && pip install -r /tmp/requirements.txt \
    && rm -rf /root/.cache/

COPY . /code

# collectstatic needs SECRET_KEY; HF provides it via Secrets/Variables.
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "Inventory_Management_System.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "1", "--threads", "2", "--timeout", "120"]