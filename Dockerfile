FROM python:3.12.1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_ROOT_USER_ACTION=ignore
WORKDIR /saucedo_com_testing
COPY requirements.txt /saucedo_com_testing
RUN pip install -r requirements.txt && apt-get install -y wget &&  \
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
&& apt-get update && apt-get -y install google-chrome-stable
COPY . .
CMD ["pytest", "-v", "-s", "/saucedo_com_testing/tests/test_order.py"]