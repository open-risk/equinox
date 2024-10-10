FROM python:3.10-slim
LABEL author="Open Risk <www.openriskmanagement.com>"
LABEL version="0.8.0"
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

COPY locale/ /equinox/locale/
COPY equinox/ /equinox/equinox/
COPY start/ /equinox/start/
COPY portfolio/ /equinox/portfolio/
COPY policy/ /equinox/policy/
COPY reference/ /equinox/reference/
COPY reporting/ /equinox/reporting/
COPY risk/ /equinox/risk/
COPY visualization/ /equinox/visualization/
COPY templates/ /equinox/templates/
COPY static/ /equinox/static/

COPY manage.py /equinox/
COPY createadmin.py /equinox/
COPY createcategories.py /equinox/
COPY createsectors.py /equinox/
COPY loadfixtures.sh /equinox/

RUN python /equinox/manage.py makemigrations start
RUN python /equinox/manage.py makemigrations portfolio
RUN python /equinox/manage.py makemigrations policy
RUN python /equinox/manage.py makemigrations reference
RUN python /equinox/manage.py makemigrations reporting
RUN python /equinox/manage.py makemigrations risk
RUN python /equinox/manage.py migrate
RUN python /equinox/createadmin.py
RUN python /equinox/createcategories.py
RUN python /equinox/createsectors.py
RUN bash loadfixtures.sh
RUN python /equinox/manage.py collectstatic --no-input
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8080"]