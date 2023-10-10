# Use Ubuntu 22.04 as the parent image
FROM ubuntu:22.04

# Avoid prompts with apt-get
ENV DEBIAN_FRONTEND=noninteractive

# Install required tools and dependencies
RUN apt-get update && \
    apt-get install -y software-properties-common gcc-11 g++-11 python3.11 python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Link gcc and g++ to the newer versions
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 60 --slave /usr/bin/g++ g++ /usr/bin/g++-11

# Set Python3.11 as the default python version
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Python packages specified in requirements.txt (if present)
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Define the default command to run when starting the container
CMD ["bash"]
