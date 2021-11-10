import json
import argparse
import pandas as pd

parser = argparse.ArgumentParser()

parser.add_argument("--modelName", required=True, help="Name of the Model")
parser.add_argument("--modelVersion", required=True, help="Version of the Model")
parser.add_argument("--dataLocation", required=True, help="Complete path of the training file (.csv)")
parser.add_argument("--configFile", required=True, help="Path of the AION configuration file")

args = parser.parse_args()

aionConfigFile = args.configFile
trainCsvFile = args.dataLocation

# check arguments 
if not aionConfigFile.endswith('.json'):
    print(f"--configFile: {aionConfigFile} is not json")
    exit()

if not trainCsvFile.endswith('.csv'):
    print(f"--dataLocation: {trainCsvFile} is not csv")
    exit()

# read json file 
with open(aionConfigFile, 'r') as f:
    jsonConfigFile = json.load(f)

print("existing values:")
print(jsonConfigFile['basic']['modelName'])
print(jsonConfigFile['basic']['modelVersion'])
print(jsonConfigFile['basic']['dataLocation'])

jsonConfigFile['basic']['modelName'] = args.modelName
jsonConfigFile['basic']['modelVersion'] = args.modelVersion
jsonConfigFile['basic']['dataLocation'] = aionConfigFile

df = pd.read_csv(trainCsvFile)
featureList = list(df.columns)
trainingFeatures = ",".join(featureList[:-2])
targetFeature = featureList[-1]

print(jsonConfigFile['basic']['featureList'])
print(jsonConfigFile['basic']['trainingFeatures'])
print(jsonConfigFile['basic']['targetFeature'])

jsonConfigFile['basic']['featureList'] = featureList
jsonConfigFile['basic']['trainingFeatures'] = trainingFeatures
jsonConfigFile['basic']['targetFeature'] = targetFeature

# write json file
with open("new_aion_config.json", 'w') as outFile:
    json.dump(jsonConfigFile, outFile)
    print("new config file generated")