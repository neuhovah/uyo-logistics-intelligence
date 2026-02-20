# Uyo Road Network Impedance Calculator
# Author: Nsikan Uso-essien (Lead Geomatics Engineer)
# Environment: PyQGIS (QGIS 3.44)

from qgis.core import QgsProject, QgsField
from PyQt5.QtCore import QVariant

def calculate_impedance():
    # 1. Target the Network Layer
    layer_name = 'Uyo_Roads_Network' 
    layers = QgsProject.instance().mapLayersByName(layer_name)

    if not layers:
        print(f"Error: Layer '{layer_name}' not found.")
        return

    layer = layers[0]
    
    # 2. Define Traffic Model (Dry Weather / Off-Peak)
    speed_lookup = {
        'trunk': 70,        # Expressways
        'primary': 60,      # Major Arteries (Oron Rd)
        'secondary': 45,    # Collectors
        'tertiary': 35,     # Neighborhood Access
        'residential': 20,  # Local Streets
        'service': 10,      # Alleys
        'track': 15         # Unpaved
    }

    layer.startEditing()
    
    # 3. Create/Update Field
    if layer.fields().indexFromName('speed_kph') == -1:
        layer.addAttribute(QgsField("speed_kph", QVariant.Int))
        layer.updateFields()
    
    idx = layer.fields().indexFromName('speed_kph')
    
    count = 0
    # 4. Iterate and Calculate
    for feature in layer.getFeatures():
        h_type = feature['highway'] if 'highway' in feature.attributeMap() else 'residential'
        speed = speed_lookup.get(h_type, 20)
        
        # Apply Friction Factor for Short Segments (Intersections)
        # If segment < 100m, reduce speed by 30%
        if feature.geometry().length() < 100:
            speed = int(speed * 0.7)
            
        layer.changeAttributeValue(feature.id(), idx, speed)
        count += 1

    layer.commitChanges()
    print(f"SUCCESS: {count} segments updated with dynamic impedance.")

# Execute
calculate_impedance()