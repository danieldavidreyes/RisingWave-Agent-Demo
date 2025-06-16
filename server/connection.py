import os
from risingwave import RisingWave, RisingWaveConnOptions
from dotenv import load_dotenv
import pathlib

print("\nDebug: Environment Loading")
print(f"Current working directory: {os.getcwd()}")
print(f"Looking for .env file in: {pathlib.Path().absolute()}")
print(f"Does .env exist? {pathlib.Path('.env').exists()}")

load_dotenv()

print("\nEnvironment variables after loading:")
print(f"RISINGWAVE_HOST: {os.getenv('RISINGWAVE_HOST')}")
print(f"RISINGWAVE_USER: {os.getenv('RISINGWAVE_USER')}")
print(f"RISINGWAVE_PASSWORD: {os.getenv('RISINGWAVE_PASSWORD')}")
print(f"RISINGWAVE_PORT: {os.getenv('RISINGWAVE_PORT')}")
print(f"RISINGWAVE_DATABASE: {os.getenv('RISINGWAVE_DATABASE')}")

connection_str = os.getenv("RISINGWAVE_CONNECTION_STR")


def check_environment_variables():
    global connection_str
    if connection_str is None:
        risingwave_host = os.getenv("RISINGWAVE_HOST")
        risingwave_user = os.getenv("RISINGWAVE_USER")
        risingwave_password = os.getenv("RISINGWAVE_PASSWORD")
        risingwave_port = os.getenv("RISINGWAVE_PORT", "4566")
        risingwave_database = os.getenv("RISINGWAVE_DATABASE", "dev")
        risingwave_sslmode = os.getenv("RISINGWAVE_SSLMODE", "require")
        risingwave_timeout = os.getenv("RISINGWAVE_TIMEOUT", "30")

        if not risingwave_host or not risingwave_user or not risingwave_password:
            raise ValueError(
                "RISINGWAVE_HOST, RISINGWAVE_USER, and RISINGWAVE_PASSWORD must be set in environment variables")

        connection_str = f"postgresql://{risingwave_user}:{risingwave_password}@{risingwave_host}:{risingwave_port}/{risingwave_database}?sslmode={risingwave_sslmode}&connect_timeout={risingwave_timeout}"

    return connection_str


def setup_risingwave_connection() -> RisingWave:
    """Set up a connection to the RisingWave database."""
    try:
        rw = RisingWave(
            RisingWaveConnOptions(check_environment_variables())
        )
        return rw
    except Exception as e:
        raise ValueError(f"Failed to connect to RisingWave: {str(e)}")
