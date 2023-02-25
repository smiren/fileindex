import sys
import hashlib

if sys.version_info[:3] >= (3, 11, 0):
    def sha256sum(filename, bufsize=64*1024):
        with open(inputFile, "rb") as f:
            digest = hashlib.file_digest(f, "sha256", _bufsize=bufsize)
        return digest.hexdigest()
else:
    def sha256sum(filename, bufsize=64*1024):
        h = hashlib.sha256()
        buffer = bytearray(bufsize)
        # using a memoryview so that we can slice the buffer without copying it
        buffer_view = memoryview(buffer)
        with open(filename, 'rb', buffering=0) as f:
            while True:
                n = f.readinto(buffer_view)
                if not n:
                    break
                h.update(buffer_view[:n])
        return h.hexdigest()
