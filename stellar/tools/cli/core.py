import subprocess
import os
import time
import sys
import glob
import docker
from docker.errors import DockerException
from cli.utils import getLogger, update_docker_host_env
from cli.consts import (
    stellarGW_DOCKER_IMAGE,
    stellarGW_DOCKER_NAME,
    KATANEMO_LOCAL_MODEL_LIST,
    MODEL_SERVER_LOG_FILE,
    ACCESS_LOG_FILES,
)
from huggingface_hub import snapshot_download
from dotenv import dotenv_values


log = getLogger(__name__)


def start_stellar_docker(client, stellar_config_file, env):
    logs_path = "~/stellar_logs"
    logs_path_abs = os.path.expanduser(logs_path)

    return client.containers.run(
        name=stellarGW_DOCKER_NAME,
        image=stellarGW_DOCKER_IMAGE,
        detach=True,  # Run in detached mode
        ports={
            "10000/tcp": 10000,
            "10001/tcp": 10001,
            "11000/tcp": 11000,
            "12000/tcp": 12000,
            "9901/tcp": 19901,
        },
        volumes={
            f"{stellar_config_file}": {
                "bind": "/app/stellar_config.yaml",
                "mode": "ro",
            },
            "/etc/ssl/cert.pem": {"bind": "/etc/ssl/cert.pem", "mode": "ro"},
            logs_path_abs: {"bind": "/var/log"},
        },
        environment={
            "OTEL_TRACING_HTTP_ENDPOINT": "http://host.docker.internal:4318/v1/traces",
            "MODEL_SERVER_PORT": os.getenv("MODEL_SERVER_PORT", "51000"),
            **env,
        },
        extra_hosts={"host.docker.internal": "host-gateway"},
        healthcheck={
            "test": ["CMD", "curl", "-f", "http://localhost:10000/healthz"],
            "interval": 5000000000,  # 5 seconds
            "timeout": 1000000000,  # 1 seconds
            "retries": 3,
        },
    )


def stream_gateway_logs(follow):
    """
    Stream logs from the stellar  gateway service.
    """
    log.info("Logs from stellar  gateway service.")

    options = ["docker", "logs", "stellar"]
    if follow:
        options.append("-f")
    try:
        # Run `docker-compose logs` to stream logs from the gateway service
        subprocess.run(
            options,
            check=True,
            stdout=sys.stdout,
            stderr=sys.stderr,
        )

    except subprocess.CalledProcessError as e:
        log.info(f"Failed to stream logs: {str(e)}")


def stream_access_logs(follow):
    """
    Get the stellar access logs
    """
    log_file_pattern_expanded = os.path.expanduser(ACCESS_LOG_FILES)
    log_files = glob.glob(log_file_pattern_expanded)

    stream_command = ["tail"]
    if follow:
        stream_command.append("-f")

    stream_command.extend(log_files)
    subprocess.run(
        stream_command,
        check=True,
        stdout=sys.stdout,
        stderr=sys.stderr,
    )


def start_stellar (stellar_config_file, env, log_timeout=120, foreground=False):
    """
    Start Docker Compose in detached mode and stream logs until services are healthy.

    Args:
        path (str): The path where the prompt_config.yml file is located.
        log_timeout (int): Time in seconds to show logs before checking for healthy state.
    """
    log.info("Starting stellar  gateway")

    try:
        try:
            client = docker.from_env()
        except DockerException as e:
            # try setting up the docker host environment variable and retry
            update_docker_host_env()
            client = docker.from_env()

        try:
            container = client.containers.get("stellar")
            log.info("stellar container found in docker, stopping and removing it")
            # ensure that previous docker container is stopped and removed
            container.stop()
            container.remove()
            log.info("Stopped and removed stellar container")
        except docker.errors.NotFound as e:
            pass

        container = start_stellar_docker(client, stellar_config_file, env)

        start_time = time.time()

        while True:
            container = client.containers.get(container.id)
            current_time = time.time()
            elapsed_time = current_time - start_time

            # Check if timeout is reached
            if elapsed_time > log_timeout:
                log.info(f"Stopping log monitoring after {log_timeout} seconds.")
                break

            container_status = container.attrs["State"]["Health"]["Status"]

            if container_status == "healthy":
                log.info("Container is healthy!")
                break
            else:
                log.info(f"Container health status: {container_status}")
                time.sleep(1)

        if foreground:
            for line in container.logs(stream=True):
                print(line.decode("utf-8").strip("\n"))

    except KeyboardInterrupt:
        log.info("Keyboard interrupt received, stopping stellar  gateway service.")
        stop_stellar ()
    except docker.errors.APIError as e:
        log.info(f"Failed to start stellar: {str(e)}")


def stop_stellar ():
    """
    Shutdown all Docker Compose services by running `docker-compose down`.

    Args:
        path (str): The path where the docker-compose.yml file is located.
    """
    log.info("Shutting down stellar  gateway service.")

    try:
        subprocess.run(
            ["docker", "stop", "stellar"],
        )
        subprocess.run(
            ["docker", "remove", "stellar"],
        )

        log.info("Successfully shut down stellar  gateway service.")

    except subprocess.CalledProcessError as e:
        log.info(f"Failed to shut down services: {str(e)}")


def download_models_from_hf():
    for model in KATANEMO_LOCAL_MODEL_LIST:
        log.info(f"Downloading model: {model}")
        snapshot_download(repo_id=model)


def start_stellar _modelserver(foreground):
    """
    Start the model server. This assumes that the stellar_modelserver package is installed locally

    """
    try:
        log.info("stellar_modelserver restart")
        if foreground:
            subprocess.run(
                ["stellar_modelserver", "start", "--foreground"],
                check=True,
            )
        else:
            subprocess.run(
                ["stellar_modelserver", "start"],
                check=True,
            )
    except subprocess.CalledProcessError as e:
        log.info(f"Failed to start server. Please check stellar_modelserver logs")
        sys.exit(1)


def stop_stellar _modelserver():
    """
    Stop the model server. This assumes that the stellar_modelserver package is installed locally

    """
    try:
        subprocess.run(
            ["stellar_modelserver", "stop"],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        log.info(f"Failed to start server. Please check stellar_modelserver logs")
        sys.exit(1)
