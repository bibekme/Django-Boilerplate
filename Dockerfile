FROM python:3.9

ENV PYTHONUNBUFFERED=1
WORKDIR /app


# Upgrade pip
RUN pip install --upgrade pip 

# Install application dependencies
COPY requirements.txt /app/
# We use the --system flag so packages are installed into the system python
# and not into a virtualenv. Docker containers don't need virtual environments. 
RUN pip install -r requirements.txt

# Copy the application files into the image
COPY . /app/

# Expose port 8000 on the container
EXPOSE 8000