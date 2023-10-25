import arcpy

# Set the input GDB path
gdb_path = r'\\172.26.0.20\root$\Observatorio_Inmobiliario_Catastral\ProyectoAnalitica_OIC_DTIC\requerimientosSIG\_Insumos\Colombia_Septiembre_Privada.gdb'

#define the workspace
arcpy.env.workspace = gdb_path

# Create a list of feature datasets in the GDB
datasets = arcpy.ListDatasets("*", "Feature")
print(datasets)
# If there are feature datasets, loop through them
if datasets:
    for dataset in datasets:
        print(f"Feature Dataset: {dataset}")
        
        # List feature classes within the feature dataset
        feature_classes = arcpy.ListFeatureClasses(feature_dataset=dataset)
        for fc in feature_classes:
            print(f"  Feature Class: {fc}")
            
            # Get the count of records in the feature class
            count = arcpy.GetCount_management(dataset + "\\" + fc)
            print(f"    Number of Records: {count}")

            # List fields in the feature class
            fields = arcpy.ListFields(dataset + "\\" + fc)
            print("    Fields:")
            for field in fields:
                print(f"      {field.name}")

# List feature classes in the root of the GDB (outside feature datasets)
root_feature_classes = arcpy.ListFeatureClasses()
for fc in root_feature_classes:
    print(f"Feature Class: {fc}")
    
    # Get the count of records in the feature class
    count = arcpy.GetCount_management(fc)
    print(f"  Number of Records: {count}")

    # List fields in the feature class
    fields = arcpy.ListFields(fc)
    print("  Fields:")
    for field in fields:
        print(f"    {field.name}")
