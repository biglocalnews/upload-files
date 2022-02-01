import os

from bln.client import Client


def main():
    """Upload the provided files to biglocalnews.org."""
    api_key = os.getenv("api-key")
    project_id = os.getenv("project-id")
    files = os.getenv("files")
    client = Client(api_key)
    client.upload_files(project_id, files)


if __name__ == '__main__':
    main()
