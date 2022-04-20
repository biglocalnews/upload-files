import glob
import logging
import os

from bln import Client


def main():
    """Upload the provided files to biglocalnews.org."""

    # Get env variables
    api_key = os.getenv("api-key")
    project_id = os.getenv("project-id")
    path = os.getenv("path")

    # Set the logger
    logging.basicConfig(
        level="DEBUG",
        format="%(asctime)s - %(name)s - %(message)s"
    )
    logger = logging.getLogger(__name__)

    # Upload files
    client = Client(api_key)

    # If the path is a directory ...
    if path.endswith("/"):
        # Get all the CSV files in the directory
        file_list = glob.glob(path + "**/*.csv", recursive=True)

        # Make sure we have at least one
        if not file_list:
            raise ValueError("No CSV file found in directory.")

        # Upload the files
        logger.debug(f"Uploading {len(file_list)} files")
        client.upload_files(project_id, file_list)

    # If a single file ...
    else:
        # Make sure it's a CSV
        if not path.lower().endswith("csv"):
            raise ValueError("Files must be CSVs")

        # Make sure the path exists
        if not os.path.exists(path):
            raise ValueError(f"File path does not exist {path}")

        # Upload the file
        logger.debug(f"Uploading {path}")
        client.upload_file(project_id, path)


if __name__ == '__main__':
    main()
