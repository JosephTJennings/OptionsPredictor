import json
import os
import shutil
import csv

#DATA SOURCE: https://drive.google.com/drive/folders/1a7afPF3k-I0kjA3aybJWR1-rIQTNK_ef

homePath = ""
jsonPath = "./JSON-Raw"
destinationPath = "./AAPL-data-JSON"


def recursiveScan():
    for folder in os.listdir(jsonPath):
        if(os.path.isdir(os.path.join(jsonPath, folder)) and folder != "AAPL-data-JSON"):
            print(folder)
            for files in os.listdir(os.path.join(jsonPath, folder)):
                if files == "AAPL.json":
                    print("file: " + folder + "_" + files)
                    #save
                    filename =  folder + "_" + files
                    destination = os.path.join(destinationPath, filename)
                    source = os.path.join(os.path.join(jsonPath, folder), files)
                    shutil.copy(source, destination)

def parseJSON():
    for file in os.listdir(destinationPath):
        with open(os.path.join(destinationPath, file), 'r') as json_file:
            json_data = json.load(json_file)
            date = file.split("_")[0]
            expiration_date = list(json_data.keys())[0]
            print(date)
            for data in json_data[expiration_date]:
                row = ""

                #Greeks
                delta = data["OptionGreeks"]["delta"]
                gamma = data["OptionGreeks"]["gamma"]
                iv = data["OptionGreeks"]["iv"]
                rho = data["OptionGreeks"]["rho"]
                theta = data["OptionGreeks"]["theta"]
                vega = data["OptionGreeks"]["vega"]

                #Other
                ask = data["ask"]
                bid = data["bid"]
                inTheMoney = data["inTheMoney"]
                optionType = data["optionType"]
                strikePrice = data["strikePrice"]
                volume = data["volume"]
                
                #date, expiration_date, inTheMoney, optionType, strikePrice, volume, delta, gamma, iv, rho, theta, vega
                row = (date + "," + str(expiration_date)  + "," + str(inTheMoney) + "," + str(optionType) + "," + str(strikePrice) + "," + 
                    str(volume) + "," + str(delta) + "," + str(gamma) + "," + str(iv) + "," + str(rho) + "," + str(theta) + "," + str(vega))
                writeCSVData(row)
                #print(row)

def writeCSVHeader():
    with open('AAPL_main.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # write the header row
        header = ["date", "expiration_date", "inTheMoney", "optionType", "strikePrice", "volume", "delta", "gamma", "iv", "rho", "theta", "vega"]
        writer.writerow(header)

def writeCSVData(optionsData):
    row = optionsData.split(",")
    with open('AAPL_main.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)

def main():
    writeCSVHeader()
    parseJSON()

if __name__ == "__main__":
    main()