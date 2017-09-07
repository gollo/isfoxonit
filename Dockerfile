FROM python:3.6-slim
# Use an official Python runtime as a base image

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="isfoxonit" \
      org.label-schema.description="Telegram webhook-based bot to see if fox is drinking." \
      org.label-schema.url="https://github.com/gollo/isfoxonit" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/gollo/isfoxonit" \
      org.label-schema.vendor="Dacrebreeze LTD" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="2.0"

# Run app.py when the container launches
CMD ["python", "isfoxonitbot.py"]
