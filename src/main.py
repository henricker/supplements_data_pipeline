from etl.extract_engines.strategies.growth_extract_website import GrowthExtractWebsite
from etl.transform_engines.strategies.growth_transform_data import GrowthTransformData
from etl.load_engines.strategies.growth_load_data import GrowthLoadData

if __name__ == "__main__":
    growthExtract = GrowthExtractWebsite()
    growthTransform = GrowthTransformData()
    growthLoader = GrowthLoadData()
    for data in growthExtract.extract():
        transformed_data = growthTransform.transform(data)
        growthLoader.load(transformed_data)
        