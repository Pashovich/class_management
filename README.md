# Project README

This README provides instructions for setting up and running the project.

## Configuration

1. To create a configuration file, run the following command. Then place your MongoDB connection URI to `CONNECTION_URL = connection_url` without any brackets:
   ```shell
   cp .env.example .env
    ```

2. Install all dependencies
    ```shell
    pip install -r requirements.txt
    ```

3. Run app
    ```shell
    python main.py
    ```
