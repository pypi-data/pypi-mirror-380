FROM python:3.11

WORKDIR /app

# copy project
COPY . .
RUN make deps

RUN FLIT_ROOT_INSTALL=1 make install

ENTRYPOINT ["udata-search-service", "run", "--host=0.0.0.0"]
