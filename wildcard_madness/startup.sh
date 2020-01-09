
# Run this in the background as wildcard_priv
socat tcp-l:8081,reuseaddr,fork EXEC:./one_char.py,pty,stderr & 
