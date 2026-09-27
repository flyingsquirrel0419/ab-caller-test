import json, os, sys
m = json.load(open(os.environ["ACTION_BUNDLE_MANIFEST"]))
# shard 1 always fails; others complete
if os.environ["ACTION_BUNDLE_SHARD_INDEX"] == "1":
    print("[fail-worker] shard 1 intentionally failing", file=sys.stderr)
    sys.exit(17)
rows = [{"id": t["id"]} for t in m["tasks"]]
json.dump(rows, open(os.path.join(os.environ["ACTION_BUNDLE_OUTPUT_DIR"], "output.json"), "w"))
json.dump({"completedTaskIds": [t["id"] for t in m["tasks"]]}, open(os.environ["ACTION_BUNDLE_COMPLETIONS"], "w"))
print(f"[fail-worker] shard {os.environ['ACTION_BUNDLE_SHARD_INDEX']} ok")
