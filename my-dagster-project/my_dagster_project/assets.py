from dagster import asset


@asset
def const_asset():
    return [1, 2, 3]
