import re

with open('Index.html', 'r', encoding='utf-8') as f:
    content = f.read()

zones_match = re.search(r'const zonesData = \[(.*?)\];', content, re.DOTALL)
if zones_match:
    zones_text = zones_match.group(1)
    coords = re.findall(r'\[(\d+\.\d+),\s*(\d+\.\d+)\]', zones_text)
    coords = [(float(lat), float(lng)) for lat, lng in coords]
    
    if coords:
        min_lat = min(c[0] for c in coords)
        max_lat = max(c[0] for c in coords)
        min_lng = min(c[1] for c in coords)
        max_lng = max(c[1] for c in coords)
        
        print(f"Zones Bounds: Lat({min_lat}, {max_lat}), Lng({min_lng}, {max_lng})")
        print(f"Total zone points: {len(coords)}")
        print(f"Zones Centroid: Lat({sum(c[0] for c in coords)/len(coords)}), Lng({sum(c[1] for c in coords)/len(coords)})")
    else:
        print("No coords found in zonesData")
else:
    print("zonesData not found")
