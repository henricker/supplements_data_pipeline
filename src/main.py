from etl.extract_engines.strategies.growth_extract_website import GrowthExtractWebsite

if __name__ == "__main__":
    obj = GrowthExtractWebsite()
    for data in obj.extract():
        print(data)