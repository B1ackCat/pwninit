from pwn import *
context.terminal = ["tmux", "split", "-h"]
context.arch = "amd64"

# ---------------- helpers ----------------
def start(e):
    # ./exp.py <host> <port>
    if len(sys.argv) >= 3:
        host, port = sys.argv[1], sys.argv[2]
        log.info(f"Running remote @ {{host}}:{{port}}...")
        return remote(host, int(port))

    log.info(f"Running local...")
    return process(e.path)

lg = lambda k, v: log.info(f"{{k}} = {{v}}")
_b  = lambda x: x if isinstance(x, bytes) else str(x).encode()
s   = lambda x: p.send(_b(x))
sl  = lambda x: p.sendline(_b(x))
sa  = lambda d, x: p.sendafter(_b(d), _b(x))
sla = lambda d, x: p.sendlineafter(_b(d), _b(x))
ru  = lambda d: p.recvuntil(_b(d))
rl  = lambda: p.recvline()
rv  = lambda: p.recv()
rvn = lambda n: p.recvn(n)

# ---------------- exploit ----------------
{bindings}
libc = e.libc
p = start(e)

p.interactive()
