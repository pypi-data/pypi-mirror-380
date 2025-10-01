import programasweights as paw

# 1) "Compile" a natural language description into dummy weights (placeholder compiler)
weights_path = "demo_weights.safetensors"
paw.compile_dummy(
    weights_path,
    spec="Parse informal text into a cleaner response.",  # description is ignored in dummy compiler
    seed=42,   # makes the weights deterministic for demos/tests
    num_tokens=16,
)
