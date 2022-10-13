FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /metashark_test_task
RUN pip install --upgrade pip

COPY requirements.txt /metashark_test_task/
COPY car_supply /metashark_test_task/

RUN python -m pip install -r /metashark_test_task/requirements.txt

WORKDIR /metashark_test_task

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]