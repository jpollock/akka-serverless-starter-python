FROM python:3.8.0-slim

#COPY ./dist /dist
#RUN pip install -i https://test.pypi.org/simple/ akkaserverless

WORKDIR /app
COPY ./ ./
RUN pip install -r requirements.txt
RUN pip install -i https://test.pypi.org/simple/ akkaserverless
ENV PYTHONPATH=/app
ENTRYPOINT python ./service.py