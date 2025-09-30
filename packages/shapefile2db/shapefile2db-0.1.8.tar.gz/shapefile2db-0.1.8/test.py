from shapefile2db import StateShapeFileToDB, ShapeFileToDB, export_shapefile_to_db
from printpop import print_lime
from datetime import datetime

print_lime("Test - Starting Export")
shapeFilePath = "C:\\Users\\ryan\\Visual Code Projects\\shapefile\\tl_2020_us_zcta520.shp"
databasepath = f'zcta-{datetime.now().strftime("%Y%m%d%H%M%S")}.db'
state = "CA"
digit_max = 4
point_max = 500

##### exporting for given state
# result = export_shapefile_to_db(state=state, 
#                                 shape_file_name=shapeFilePath, 
#                                 database_name=databasepath, 
#                                 digit_max=digit_max, 
#                                 point_max=point_max)

##### exporting entire US
export_shapefile_to_db(shape_file_name=shapeFilePath, 
                        database_name=databasepath, 
                        digit_max=digit_max, 
                        point_max=point_max)
