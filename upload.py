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

    if path.endswith("/"):
        # Upload directory
        file_list = glob.glob(path + "*.csv")
        if not file_list:
            raise ValueError("No CSV file found in directory.")
        for f in file_list:
            print(f"Uploading {f}")
        client.upload_files(project_id, file_list)
    else:
        # Upload file
        if not path.lower().endswith("csv"):
            raise ValueError("Files must be CSVs")
        if not os.path.exists(path):
            raise ValueError(f"File path does not exist {path}")
        print(f"Uploading {path}")
        client.upload_file(project_id, path)


if __name__ == '__main__':
    main()
