# Weather API CI/CD

This is a simple Flask API that returns mock weather data. It's containerized using Docker and integrated with GitHub Actions for CI/CD.

## Run Locally

```bash
docker build -t weather-api .
docker run -p 5000:5000 weather-api
