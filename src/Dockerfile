# Use the TensorFlow GPU base image
FROM tensorflow/tensorflow:latest-gpu

# Set the working directory
WORKDIR /src

# Install any additional dependencies if needed
RUN apt-get update && apt-get install -y

# Copy your project files into the container (assuming you have local project files)
COPY . /src

# Start a bash shell on container launch
CMD ["/bin/bash"]
