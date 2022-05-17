FROM python:3.9-slim
MAINTAINER Open Risk <www.openriskmanagement.com>
LABEL version="0.4"
LABEL description="Equinox: Open Source Sustainable Porfolio Management"
LABEL maintainer="info@openrisk.eu"
EXPOSE 8080
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DJANGO_SETTINGS_MODULE equinox.settings
ENV DJANGO_ALLOWED_HOSTS localhost 127.0.0.1 [::1]
RUN apt-get update && apt-get install -y \
    gdal-bin \
    proj-bin \
    libgdal-dev \
    libproj-dev \
    spatialite-bin\
    libsqlite3-mod-spatialite
RUN mkdir /equinox
WORKDIR /equinox
COPY requirements.txt /equinox/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /equinox/
RUN rm -f /equinox/db.sqlite3
RUN python /equinox/manage.py makemigrations
RUN python /equinox/manage.py migrate
RUN python /equinox/createadmin.py
RUN python /equinox/createcategories.py
RUN python /equinox/createsectors.py
RUN bash loadfixtures.sh
RUN python /equinox/manage.py collectstatic --no-input
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8080"]