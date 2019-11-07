PORT = 8000
HOST = "127.0.0.1"
CHUNK_SIZE = 1024 * 16
USERS = 100
HEADER_SIZE = 3 + 1 + 3
CLIENT_FILES_LOC = "tests/client_test_data/"


"""
- HEADER: "(3 - digit p_no)" + "," + "(3 - digit data_sz)"

- p_no:
    - 001: user-name authentication
    - 002: join other room
    - 003: disconnect room
    - 004: quit application
    - 005: get room information
    - 006: send message in room
"""
