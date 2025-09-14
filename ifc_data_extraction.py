import ifcopenshell
import ifcopenshell.geom
import ifcopenshell.util.shape

print(f"IFCOpenShell version: {ifcopenshell.version}")

# Open the IFC file
file_path = "C:/Users/pmls/Desktop/bim3storyfile.ifc"
ifc_model = ifcopenshell.open(file_path)

desired_wall_id = '3yKL7w3aP50Qs40ucQ6MHe'

# Find the wall instance with the desired GlobalId
for wall_instance in ifc_model.by_type('IfcWall'):
    if wall_instance.GlobalId == desired_wall_id:
        wall_name = wall_instance.Name
        print(f"Facade Name: {wall_name}")

        try:
            # Geometry settings
            geometry_settings = ifcopenshell.geom.settings()
            wall_shape = ifcopenshell.geom.create_shape(geometry_settings, wall_instance)
            
            # Extract geometric data
            facade_area = round(ifcopenshell.util.shape.get_area(wall_shape.geometry), 2) if wall_shape.geometry else 0
            facade_volume = round(ifcopenshell.util.shape.get_volume(wall_shape.geometry), 2) if wall_shape.geometry else 0
            facade_x = round(ifcopenshell.util.shape.get_x(wall_shape.geometry), 2) if wall_shape.geometry else 0
            facade_y = round(ifcopenshell.util.shape.get_y(wall_shape.geometry), 2) if wall_shape.geometry else 0
            facade_z = round(ifcopenshell.util.shape.get_z(wall_shape.geometry), 2) if wall_shape.geometry else 0
            facade_height = round(ifcopenshell.util.shape.get_top_elevation(wall_shape.geometry), 2) if wall_shape.geometry else 0
            
            # Custom side area calculations (if needed, adjust this logic)
            facade_side_x = round(ifcopenshell.util.shape.get_side_area(wall_shape.geometry, 'X'), 2) if wall_shape.geometry else 0
            facade_side_y = round(ifcopenshell.util.shape.get_side_area(wall_shape.geometry, 'Y'), 2) if wall_shape.geometry else 0
            facade_side_z = round(ifcopenshell.util.shape.get_side_area(wall_shape.geometry, 'Z'), 2) if wall_shape.geometry else 0
            facade_perimeter = round(ifcopenshell.util.shape.get_footprint_perimeter(wall_shape.geometry), 2) if wall_shape.geometry else 0

            # Print results
            print(f"Facade Area: {facade_area} m²")
            print(f"Facade Volume: {facade_volume} m³")
            print(f"Facade Position: x = {facade_x}, y = {facade_y}, z = {facade_z}")
            print(f"Facade Height: {facade_height} m")
            print(f"Facade Side Areas: x = {facade_side_x} m², y = {facade_side_y} m², z = {facade_side_z} m²")
            print(f"Facade Perimeter: {facade_perimeter} m")

        except Exception as e:
            print(f"Error extracting geometry or data: {e}")