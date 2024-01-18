import pathlib


CACHED_FILE = pathlib.Path("/tmp/cache/cached.bin")

if __name__ == "__main__":
  if CACHED_FILE.exists():
    print("Cached file exists!")
  else:
    print("Cached file does not exist, creating...")
    CACHED_FILE.write_bytes(b"1234"*1000)