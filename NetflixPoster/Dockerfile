FROM python
ADD . /app
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /app
WORKDIR /app
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]