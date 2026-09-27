import json, os
m = json.load(open(os.environ["ACTION_BUNDLE_MANIFEST"]))
rows = [{"id": t["id"], "len": len(t["id"])} for t in m["tasks"]]
out = os.environ["ACTION_BUNDLE_OUTPUT_DIR"]
json.dump(rows, open(os.path.join(out, "output.json"), "w"))
json.dump({"completedTaskIds": [t["id"] for t in m["tasks"]]}, open(os.environ["ACTION_BUNDLE_COMPLETIONS"], "w"))
print(f"[caller-worker] cwd={os.getcwd()} tasks={len(rows)}")
