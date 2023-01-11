# Payload Actions

This GitHub Actions workflow allows you to automatically extract and release specific files from a ROM URL.

## Inputs
The following inputs are required when triggering the workflow:

- `ROM_URL`: The URL of the ROM file to be extracted and released. (default : "https://github.com/TheStrechh/thestrechh_builds/releases/download/20221220-0147/lineage-20.0-20221220-UNOFFICIAL-spes.zip")
- `DEVICE_NAME`: The name of the device for which the ROM is intended.
- `ROM_NAME`: The name of the ROM.
- `EXTRACTED_FILES`: A comma-separated list of files to be extracted and released. (default : "boot.img, dtbo.img, product.img, system.img, system_ext.img")

## Steps
The workflow is composed of the following steps:

1. Checkout code: check out the repository code.
2. Download file: download the file specified by the ROM_URL input.
3. Unzip file: unzip the downloaded file to a directory named "extracted_files/".
4. Setup Python: set up a version of Python.
5. Install OTA Extractor: download and install the OTA Extractor package.
6. Extract Payload: extract payload from the downloaded file and output it to the "extracted_files/" directory.
7. Upload to Release: upload the specified files (EXTRACTED_FILES input) to a GitHub release with a name that includes the DEVICE_NAME and run_id, a tag with the run_id, and a body that includes information about the device, ROM, and extracted files.

## Usage
To use this workflow, create a new GitHub Actions workflow in your repository and copy the contents of [main.yml](https://github.com/your-repo/main.yml) into the file. Update the inputs with your desired values, and configure any necessary secrets. You can then trigger the workflow manually using the "workflow_dispatch" event.

## Note
The OTA Extractor package that is used in this workflow is taken from https://github.com/sakshiagrwal/OTAExtractor, it is cloned, a specific version of protobuf library is installed, and `HEAD~1` is reset to avoid breaking changes. So you can be sure that the package version you are using is compatible with the script.

Additionally, it is important to note that in order to use the `Upload to Release` step, you need to have the `GITHUB_TOKEN` available as a secret in your repository.
