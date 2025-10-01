import programasweights as paw

spec = "Parse a string like '(A) ... (B) ... (C) ...' into a JSON dictionary mapping each option letter (A, B, C, ...) to its text. Keys must be plain letters only (no parentheses). Be robust to noise: extra spaces, bullets, and phrases like 'both (A) and (B)'. Output only the JSON dictionary, with no extra text or explanation."
fn = paw.function('outputs_1spec/prefix_kv/eval_program/', interpreter_name='yuntian-deng/paw-interpreter')

for s in [
    "(A) cat  (B) dog  (C) both (A) and (B) are possible",
    "(A). cat  (B) dog  (C) both (A) and (B) are possible",
    "(A):. cat  (B): dog  (C) both (A) and (B) are possible",
    "(A:. cat  B): dog  C) both (A) and (B) are possible",
    "A) cat  B) dog  C) both (A) and (B) are possible",
    "A)\tcat  B)\tdog  C)\tboth (A) and (B) are possible",
    "1) Alpha 2) Beta 3) Gamma",
    "[1] Red [2] Green [3] Blue",
]:
    print("SPEC:", spec)
    print("INPUT:", s)
    print("OUTPUT:", fn(s))
