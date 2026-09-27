import json, os, glob
results = os.environ["ACTION_BUNDLE_RESULTS"]
out = os.environ["ACTION_BUNDLE_OUTPUT"]
rows = []
for p in sorted(glob.glob(os.path.join(results, "shard-*", "output.json"))):
    rows.extend(json.load(open(p)))
json.dump({"merged": rows, "count": len(rows), "cwd": os.getcwd()}, open(out, "w"))
print(f"[caller-reducer] cwd={os.getcwd()} merged={len(rows)}")
