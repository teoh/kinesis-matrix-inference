import re
import pandas as pd
from constants import (
    KEY_LAYOUT,
    IDENTIFIER_LAYOUT,
    IDENTIFIER_MATRIX,
    NUM_COLS,
    ROW_TO_NAME,
    COL_TO_NAME,
    CLUSTER_PINS,
    CLUSTER_KEYS,
    ELITE_C_ROW_PINS,
    ELITE_C_COL_PINS,
)
for pins in CLUSTER_PINS.values():
    assert len(pins) == 13

# parse KEY_LAYOUT to get a list of keys
keys = [key.strip() for key in KEY_LAYOUT.split(",")]

# parse IDENTIFIER_LAYOUT to get list of identifiers
identifiers = [idfr.strip() for idfr in IDENTIFIER_LAYOUT.split(",")]

# create relationship between the two
df = pd.DataFrame({"key": keys, "identifier": identifiers})

# get coordinates in the IDENTIFIER_MATRIX
# I generated this with chatgpt, so if it's redundant or has problems,
# i want you to flame me as hard as you can with a github issue.
mtx_identifiers = re.findall(r"\b([a-zA-Z0-9_]+)\b", IDENTIFIER_MATRIX)
coords = [
    # (i, j % NUM_COLS)
    (i, j)
    for i, row in enumerate(IDENTIFIER_MATRIX.strip().split("\n"))
    for j, col in enumerate(row.split(","))
    if re.search(r"\b([a-zA-Z0-9_]+|___)\b", col)
]
identifiers_to_coords = {
    _id: coord for _id, coord in zip(mtx_identifiers, coords) if _id != "___"
}

df["mtx_coords"] = df["identifier"].map(identifiers_to_coords)

# parse row names
row_names = [
    re.findall(r"\b([a-zA-Z0-9_]+)\b", row) for row in ROW_TO_NAME.strip().split("\n")
]

# parse column names
col_names = [
    re.findall(r"\b([a-zA-Z0-9_]+)\b", col) for col in COL_TO_NAME.strip().split("\n")
]

df["ROWX_COLY"] = df["mtx_coords"].apply(
    lambda t: (row_names[t[0]][1], col_names[t[1]][1])
)
df["PINX_PINY"] = df["mtx_coords"].apply(
    lambda t: (row_names[t[0]][0], col_names[t[1]][0])
)

# get the number of the pin, given the cluster
# rearrange CLUSTER_KEYS so that we're mapping each key to a cluster
key_to_cluster = {}
for cluster_name, key_list in CLUSTER_KEYS.items():
    for key in key_list:
        if key in key_to_cluster:
            print(
                f"You fool, you doubled up on the key {key} and that should not happen"
            )
        else:
            key_to_cluster[key] = cluster_name
print(key_to_cluster)
df["cluster"] = df["key"].map(key_to_cluster)

df["row_cluster_pins"] = df.apply(
    lambda row: tuple([
        i + 1
        for i, pin_name in enumerate(CLUSTER_PINS.get(row["cluster"]))
        if pin_name == row["ROWX_COLY"][0]
    ]),
    axis=1,
)
df["col_cluster_pins"] = df.apply(
    lambda row: tuple([
        i + 1
        for i, pin_name in enumerate(CLUSTER_PINS.get(row["cluster"]))
        if pin_name == row["ROWX_COLY"][1]
    ]),
    axis=1,
)

# get the elite c pin name for each row coordinate
df["elite_c_row_pin"] = df["mtx_coords"].apply(lambda t: ELITE_C_ROW_PINS[t[0]])

# get the elite c pin name for each col coordinate
df["elite_c_col_pin"] = df["mtx_coords"].apply(lambda t: ELITE_C_COL_PINS[t[1]])

df.to_csv("kinesis_wiring_info.csv", sep="\t", index=False)

df_solder_row_pins = df[["cluster", "row_cluster_pins", "elite_c_row_pin"]].rename(
    columns={"row_cluster_pins": "cluster_pins", "elite_c_row_pin": "elite_c_pin"}
)
df_solder_col_pins = df[["cluster", "col_cluster_pins", "elite_c_col_pin"]].rename(
    columns={"col_cluster_pins": "cluster_pins", "elite_c_col_pin": "elite_c_pin"}
)
df_solder_pins = pd.concat([df_solder_row_pins, df_solder_col_pins]).drop_duplicates().sort_values(["cluster", "cluster_pins"])
df_solder_pins.to_csv("elite_c_solder_guide.csv", sep="\t", index=False)
