FROM python:3.10.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN groupadd -r user && useradd -r -g user user

RUN mkdir /home/my_cv && chown -R user:user /home/my_cv

RUN mkdir /home/my_cv/static && chown -R user:user /home/my_cv/static

WORKDIR /home/my_cv

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=user:user my_cv/ /home/my_cv

RUN sed -i 's/\r$//g'  /home/my_cv/entrypoint.sh
RUN chmod +x /home/my_cv/entrypoint.sh

USER user