import joblib
import os

# Load your existing trained pipeline
model = joblib.load("mental_health_pipeline.pkl")

# Save a compressed copy
joblib.dump(
    model,
    "mental_health_pipeline_compressed.pkl",
    compress=3
)

# Check file sizes
old_size = os.path.getsize("mental_health_pipeline.pkl") / (1024 * 1024)
new_size = os.path.getsize("mental_health_pipeline_compressed.pkl") / (1024 * 1024)

print(f"Original size: {old_size:.2f} MB")
print(f"Compressed size: {new_size:.2f} MB")