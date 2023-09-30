from etl.extract_engines.strategies.growth_extract_website import GrowthExtractWebsite
from etl.transform_engines.strategies.growth_transform_data import GrowthTransformData

if __name__ == "__main__":
    growthExtract = GrowthExtractWebsite()
    growthTransform = GrowthTransformData()
    for data in growthExtract.extract():
        print(growthTransform.transform(data))