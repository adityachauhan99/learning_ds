
\d : All valid digits (0-9)
\D : Everything except numbers
email pattern : "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"


- `A`, `B`, `C`... — literal characters, just match themselves
- `[ABC]` — a **character class**: matches exactly one character, and it must be A, B, or C
- `{n}` — repeat the previous thing exactly `n` times, e.g. `A{3}` matches `AAA`
- `{n,m}` — repeat between `n` and `m` times
- `?` — the preceding thing is optional (0 or 1 times)
- `|` — OR, e.g. `(CM|CD)` matches either `CM` or `CD`
- `()` — groups things together so `?`, `{n}`, etc. apply to the whole group, not just one character
- `^` and `$` — anchors meaning "start of string" and "end of string" — important so your pattern matches the _whole_ string, not just part of it

r"Your String" : python takes it as a raw string (No Changes)


assertion : check that something exists right here , but do not consume it as a match
	(?<=X) = the text right before this point must be X , but X is a gatekeeper

. ====== any single character (the dot)