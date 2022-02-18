from convert import ConvertManufFile
from download import downloadManuf
from cleanup import cleanup

downloadedFileName = "../manuf"
csvFileName = "../manuf.csv"

def main() -> None:

    # Download file.
    downloadManuf(downloadedFileName)

    # Create CSV file.
    ConvertManufFile(downloadedFileName, csvFileName).start()

    # Cleanup delete orignal file.
    cleanup(downloadedFileName)

if __name__ == "__main__":
    main()
