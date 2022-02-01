import os

from bln.client import Client


def main():
    """Upload the provided files to biglocalnews.org."""

    # Get env variables
    api_key = os.getenv("api-key")
    project_id = os.getenv("project-id")
    path = os.getenv("path")
    print(f"Uploading {path}")

    # Upload files
    client = Client(api_key)

    if path.endswith("/"):
        # Upload directory
    else:
        # Upload file
        client.upload_file(project_id, files)


if __name__ == '__main__':
    main()
