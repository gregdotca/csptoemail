CSP to Email
------------

## What is CSP to Email?

A simple web application that allows you to send Content Security Policy (CSP) reports to an email address. It is designed to be easy to set up and use, with minimal configuration required. There's no UI or reporting, just an endpoint that will take your CSP Reports and emails them to you as they come in.

**NOTE: This is a work in progress and is not yet ready for production use. It is currently being tested and developed, so please use it at your own risk.**

## Installation (Docker Compose)

- Copy the below contents into a docker-compose.yml file (or just copy the existing docker-compose.yml file)
- Update the environment variables with your details
- Run docker compose up -d (or docker-compose up -d)
- CSP to Email will now be running on http://localhost:5000

````
services:
  csptoemail:
    image: csptoemail/csptoemail:latest
    container_name: csp_to_email
    ports:
      - "5000:5000"
    restart: unless-stopped
    environment:
      - CSP2E_SERVER=mail.example.com
      - CSP2E_PROTOCOL=tls
      - CSP2E_PORT=587
      - CSP2E_USERNAME=user
      - CSP2E_PASSWORD=pass
      - CSP2E_SENDER=sender@example.com
      - CSP2E_RECEIVER=receiver@example.com
````

## Installation (Docker)

If you don't want to run Docker Compose, you can run the container directly.

````
docker run -d \
  --name csp_to_email \
  -p 5000:5000 \
  --restart unless-stopped \
  -e CSP2E_SERVER=mail.example.com \
  -e CSP2E_PROTOCOL=tls \
  -e CSP2E_PORT=587 \
  -e CSP2E_USERNAME=user \
  -e CSP2E_PASSWORD=pass \
  -e CSP2E_SENDER=sender@example.com \
  -e CSP2E_RECEIVER=receiver@example.com \
  csptoemail/csptoemail:latest
````


## License

MIT License

Copyright (c) 2025 Greg Chetcuti <greg@greg.ca>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
