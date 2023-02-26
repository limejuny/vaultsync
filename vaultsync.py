import json
import os
# This Program is sync vaultwarden to bitwarden

# read vaultwarden json
v_json = json.load(open('vaultwarden.json'))

# read bitwarden json
b_json = json.load(open('bitwarden.json'))

# json to import
i_json = {
    "encrypted": False,
    "folders": [],
    "items": []
}

# add new folders in vaultwarden to bitwarden and update folders in vaultwarden to bitwarden
v_folder = {d['id']: d['name'] for d in v_json['folders']}
b_folder = {d['id']: d['name'] for d in b_json['folders']}

for v_id, v_name in v_folder.items():
    if v_id not in b_folder:
        i_json['folders'].append({
            "id": v_id,
            "name": v_name
        })
    elif v_name != b_folder[v_id]:
        json_str = json.dumps({
            "id": v_id,
            "name": v_name
        })
        os.system(f"echo {json_str} | bw encode | bw edit folder {v_id}")

# add new items in vaultwarden to bitwarden and update items in vaultwarden to bitwarden
v_item = {d['id']: d for d in v_json['items']}
b_item = {d['id']: d for d in b_json['items']}

for v_id, v_data in v_item.items():
    if v_id not in b_item:
        i_json['items'].append(v_data)
    elif v_data != b_item[v_id]:
        json_str = json.dumps(v_data)
        os.system(f"echo {json_str} | bw encode | bw edit item {v_id}")

# import json to bitwarden
# i_json to file
with open('import.json', 'w') as f:
    json.dump(i_json, f)
    os.system("bw import bitwardenjson import.json")

# delete items not in vaultwarden from bitwarden
for b_id in b_item.keys():
    if b_id not in v_item:
        os.system(f"bw delete item {b_id}")

# delete folders not in vaultwarden from bitwarden
for b_id in b_folder.keys():
    if b_id not in v_folder:
        os.system(f"bw delete folder {b_id}")
