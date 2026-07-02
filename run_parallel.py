import subprocess
import threading

FEATURE_FILES = [
    "features/prelogin.feature",
    "features/navigation.feature",
    "features/logout.feature",
]


def run_feature(feature_file):
    cmd = ["behave", feature_file]
    print(f"[START] {feature_file}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(f"\n{'='*60}")
    print(f"[RESULT] {feature_file}")
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
    print(f"{'='*60}\n")


threads = [threading.Thread(target=run_feature, args=(f,)) for f in FEATURE_FILES]

for t in threads:
    t.start()

for t in threads:
    t.join()

print("All 3 workers finished.")
