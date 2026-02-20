Uyo Urban Investment & Logistics Intelligence
A Spatial Decision Support System (SDSS) and WebGIS for Last-Mile Optimization.

!(https://img.shields.io/badge/Status-Complete-success)

Live Interactive Map: https://neuhovah.github.io/uyo-logistics-intelligence/

Project Overview
This repository contains a survey-grade WebGIS platform analyzing the spatial economy and logistics network of Uyo, Akwa Ibom State. Leveraging Spatial Econometrics and Graph Theory, the project identifies high-value commercial agglomeration zones (Hotspots) and underserved residential expansion areas (Service Deserts) to optimize real estate capital allocation and fleet routing.

By analyzing 80,723 building footprints and 5,200 topologically corrected road segments across a 188.0 km² study area, the spatial model successfully achieved a 56% reduction in logistics fleet mileage.

Key Findings & Results
VRP Route Optimization: Graph-theory routing reduced the baseline delivery distance from 100.91 km to 44.42 km, demonstrating a 55.98% efficiency gain and generating operational savings of ₦195,250 / vehicle / month.

The "Congestion Tax": The Ibom Plaza core is empirically identified as an oversaturated logistics bottleneck experiencing severe traffic delays.

Blue Ocean Markets: The Ring Road III corridor and Mbiabong axis are identified as high-density residential areas lacking commercial infrastructure, representing prime development targets.

Technical Specifications
Geodetic Framework: WGS 84 / UTM Zone 32N (EPSG:32632).

Positional Accuracy: Horizontal RMSE of 2.14m (NSSDA Class 1), validated against 50cm high-resolution satellite imagery.

Statistical Engine: Getis-Ord Gi* (Local) executed in Analytical Mode.

Tech Stack & Tooling
Geospatial Processing: QGIS 3.34 (Advanced Cartography & Topology Repair).

Network Algorithms: OpenRouteService (VRP & TSP Solvers) & Python (speed_calculator.py).

WebGIS Frontend: Leaflet.js and Tailwind CSS (Data loaded asynchronously via variable-wrapped GeoJSON to bypass strict CORS hosting limits).

Lead Engineer: [Uso-essien Nsikan Eno]