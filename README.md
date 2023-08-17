Upload comma-delimited files to [biglocalnews.org](https://biglocalnews.org) in your GitHub Action

## Inputs

* `api-key`: Your biglocalnews.org API token.
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
        uses: actions/checkout@v3

      - name: Upload file to biglocalnews.org
        uses: biglocalnews/upload-files@v2
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
        uses: actions/checkout@v3

      - name: Upload folder to biglocalnews.org
        uses: biglocalnews/upload-files@v2
        with:
          api-key: ${{ secrets.BLN_API_KEY }}
          project-id: ${{ secrets.BLN_PROJECT_ID }}
          path: your-folder/
```

## About

The project is sponsored by [Big Local News](https://biglocalnews.org/#/about), a program at Stanford University that collects data for impactful journalism. The code is maintained by [Ben Welsh](https://palewi.re/who-is-ben-welsh/), a visiting data journalist from the Los Angeles Times.
