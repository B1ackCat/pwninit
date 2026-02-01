from pwn import *
context.terminal = ["tmux", "split", "-h"]
context.arch = "amd64"

# log helper
slog = lambda k, v: log.info(f"{{k}} = {{v}}")

# pwntools send/recv helper
_b = lambda x: x if isinstance(x, bytes) else str(x).encode()
sl = lambda d, x: p.sendlineafter(_b(d), _b(x))
sa = lambda d, x: p.sendafter(_b(d), _b(x))
ru = lambda d: p.recvuntil(_b(d))
rl = lambda: p.recvline()
rv = lambda: p.recv()
rvn = lambda n: p.recvn(n)

{bindings}
libc = e.libc
p = process(e.path)

p.interactive()
