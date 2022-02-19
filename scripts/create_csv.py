"""
This script downloads & parses the manuf file and converts
it to csv file.
"""
import urllib.request
import csv
import os

downloadedFileName = "../manuf"
csvFileName = "../manuf.csv"

def downloadManuf(fileName):
    urllib.request.urlretrieve("https://gitlab.com/wireshark/wireshark/-/raw/master/manuf", fileName)

class ConvertManufFile():

    def __init__(self, manufPath, outputPath) -> None:
        self.manufPath = manufPath
        self.outputPath = outputPath

    def cleanText(self) -> None:
        """
        This method removes the header of the manuf
        file & saves it.

        Every line in header starts with a '#' so this
        method saves all the lines which do not start
        with '#'.
        """

        cleanedText = []

        with open(self.manufPath, "r", encoding="utf8") as f:
            lines = f.readlines()

            for line in lines:
                if not (line.startswith("#")):

                    # Now remove comments from the line.
                    if "#" in line:
                        newLine = line.split("#", 1)[0] + "\n"

                    else:
                        newLine = line.split("#", 1)[0]

                    newList = newLine.split("\t", 1)

                    if len(newList) > 1:
                        newList[1] = newList[1].replace('\t', ' ').strip()
                    cleanedText.append(newList)

        return cleanedText

    def convertToCsv(self, text) -> None:
        """
        This method converts the cleaned manuf file to
        csv file.
        """

        with open(self.outputPath, 'w', encoding="utf8", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(text)

    def start(self) -> None:

        # Remove header & comments.
        cleanedText = self.cleanText()

        # Convert to csv.
        self.convertToCsv(cleanedText[6:])

def main() -> None:

    # Download file.
    downloadManuf(downloadedFileName)

    # Create CSV file.
    ConvertManufFile(downloadedFileName, csvFileName).start()

    # Cleanup delete orignal file.
    os.remove(downloadedFileName)

if __name__ == "__main__":
    main()