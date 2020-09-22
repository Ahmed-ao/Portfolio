# Pull
FROM python:3.8
# Set enviroment variables
ENV PYTHONDONWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /home/air/Workspace/Templates/Portfolio/
# Install dependencies
COPY Pipfile Pipfile.lock /home/air/Workspace/Templates/Portfolio/
RUN pip install pipenv && pipenv install --system
# Copy project
COPY . /home/air/Workspace/Templates/Portfolio/