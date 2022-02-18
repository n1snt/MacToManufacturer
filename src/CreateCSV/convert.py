"""
This module will convert the manuf file to csv file.
"""
import csv


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

        with open(self.outputPath, 'w', encoding="utf8", newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(text)

    def start(self) -> None:

        # Remove header & comments.
        cleanedText = self.cleanText()

        # Convert to csv.
        self.convertToCsv(cleanedText[6:])