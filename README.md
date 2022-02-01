Upload comma-delimited files to [biglocalnews.org](https://biglocalnews.org) in your GitHub Action

## Inputs

* `api-key`: our biglocalnews.org API key.
* `project-id`: The identifier of the biglocalnews.org project where the files will be uploaded.
* `path`: The file or folder path inside the action's filesystem to upload.

## Usage

Upload a single CSV file.

```yaml
name: Example action
jobs:
  job:
    name: Upload file
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Upload file to biglocalnews.org
        uses: biglocalnews/upload-files@v1
        with:
          api-key: ${{ secrets.BLN_API_KEY }}
          project-id: ${{ secrets.BLN_PROJECT_ID }}
          path: your-file.csv
```

Upload a directory of CSV files.

```yaml
name: Example action
jobs:
  job:
    name: Upload directory
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Upload folder to biglocalnews.org
        uses: biglocalnews/upload-files@v1
        with:
          api-key: ${{ secrets.BLN_API_KEY }}
          project-id: ${{ secrets.BLN_PROJECT_ID }}
          path: your-folder/
```
