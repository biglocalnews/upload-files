import glob
import os

from bln.client import Client


def main():
    """Upload the provided files to biglocalnews.org."""

    # Get env variables
    api_key = os.getenv("api-key")
    project_id = os.getenv("project-id")
    path = os.getenv("path")

    # Upload files
    client = Client(api_key)

    # If the path is a directory ...
    if path.endswith("/"):
        # Get all the CSV files in the directory
        file_list = glob.glob(path + "*.csv")

        # Make sure we have at least one
        if not file_list:
            raise ValueError("No CSV file found in directory.")

        # Upload the files
        for f in file_list:
            print(f"Uploading {f}")
            client.upload_file(project_id, f)

    # If a single file ...
    else:
        # Make sure it's a CSV
        if not path.lower().endswith("csv"):
            raise ValueError("Files must be CSVs")

        # Make sure the path exists
        if not os.path.exists(path):
            raise ValueError(f"File path does not exist {path}")

        # Upload the file
        print(f"Uploading {path}")
        client.upload_file(project_id, path)


if __name__ == '__main__':
    main()
