ARG IS_READY
FROM python:3.8
ARG IS_READY
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD ["mkdir", "content"]
COPY ./ ./

ENV IS_READY_ENV=$IS_READY

WORKDIR "/server"
CMD ["sh", "-c", "python main.py --is_ready $IS_READY_ENV"]