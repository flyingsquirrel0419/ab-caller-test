import json, os
m = json.load(open(os.environ["ACTION_BUNDLE_MANIFEST"]))
# Report only half the tasks complete — a partial worker.
done = [t["id"] for t in m["tasks"]][:1]
json.dump([], open(os.path.join(os.environ["ACTION_BUNDLE_OUTPUT_DIR"], "output.json"), "w"))
json.dump({"completedTaskIds": done}, open(os.environ["ACTION_BUNDLE_COMPLETIONS"], "w"))
print(f"[partial-worker] reported only {len(done)}/{len(m['tasks'])}")
