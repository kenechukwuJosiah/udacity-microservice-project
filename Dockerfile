FROM public.ecr.aws/docker/library/python:3.10-alpine

# Create a work directory
WORKDIR /src

# Copy the current directory contents to the container at /src
COPY ./analytics/ /src

# Dependencies are installed during build time in the container itself so we don't have OS mismatch
RUN pip install --no-cache-dir -r /src/requirements.txt

# Expose port 5153
EXPOSE 5153

CMD python app.py
