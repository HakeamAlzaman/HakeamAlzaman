import re

with open('Index.html', 'r', encoding='utf-8') as f:
    content = f.read()

roads_match = re.search(r'const roadsData = \[(.*?)\];', content, re.DOTALL)
if roads_match:
    roads_text = roads_match.group(1)
    # Extract all [lat, lng] pairs
    coords = re.findall(r'\[(\d+\.\d+),\s*(\d+\.\d+)\]', roads_text)
    coords = [(float(lat), float(lng)) for lat, lng in coords]
    
    if coords:
        min_lat = min(c[0] for c in coords)
        max_lat = max(c[0] for c in coords)
        min_lng = min(c[1] for c in coords)
        max_lng = max(c[1] for c in coords)
        
        print(f"Bounds: Lat({min_lat}, {max_lat}), Lng({min_lng}, {max_lng})")
        print(f"Total points: {len(coords)}")
        
        # Check center of Mecca area (approx 21.42, 39.82)
        print(f"Centroid: Lat({sum(c[0] for c in coords)/len(coords)}), Lng({sum(c[1] for c in coords)/len(coords)})")
    else:
        print("No coords found in roadsData")
else:
    print("roadsData not found")
