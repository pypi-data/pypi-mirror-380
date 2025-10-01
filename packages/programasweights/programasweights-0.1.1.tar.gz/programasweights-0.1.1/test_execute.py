import programasweights as paw

weights_path = "demo_weights.safetensors"
# Load weights as a callable function via the runtime/interpreter
fn = paw.function(weights_path, model_name="google/flan-t5-small", max_new_tokens=64)
print(fn("hello world"))
