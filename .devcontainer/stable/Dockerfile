FROM texlive/texlive:latest-full

# Install Pandoc dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gpg \
    latex2rtf

# Install Pandoc
RUN curl -fsSL https://github.com/jgm/pandoc/releases/download/2.14.1/pandoc-2.14.1-1-amd64.deb -o pandoc.deb
RUN dpkg -i pandoc.deb

# Clean up
RUN rm pandoc.deb
RUN apt-get clean && rm -rf /var/lib/apt/lists/

# Test Pandoc installation
RUN pandoc --version

# Additional commands for your LaTeX document or any other setup
