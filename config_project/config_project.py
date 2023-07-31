import subprocess


def generate_env_file():
    """create environment file"""
    env_data = {
        "DATABASE_NAME": "company",
        "DATABASE_USER": "docker",
        "DATABASE_PASSWORD": "docker",
        "DATABASE_HOST": "localhost",
        "DATABASE_PORT": "5433",
        "PORT": "3333",
    }

    with open(".env", "w", encoding="utf-8") as env_file:
        for key, value in env_data.items():
            env_file.write(f"{key}={value}\n")


def start_postgres():
    """Start PostgreSQL"""
    subprocess.run(
        ["docker-compose", "-f", "config_project/docker-compose.yml", "up", "-d"],
        check=True,
    )


if __name__ == "__main__":
    generate_env_file()
    start_postgres()
