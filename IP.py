import struct
from socket import gethostbyname
from socket import inet_aton


def find_by_ip(name):

    try:
        f = open('17monipdb.dat', 'rb')
    except:
        return "N/A"
    index = f.read(4)
    offset = struct.unpack('>I', index)[0]
    index = f.read(offset - 4)
    nip = gethostbyname(name)
    ipdot = nip.split('.')
    if int(ipdot[0]) < 0 or int(ipdot[0]) > 255 or len(ipdot) != 4:
        return "N/A"
    nip = struct.unpack("!L", inet_aton(nip))[0]
    tmp_offset = int(ipdot[0]) * 4
    start = struct.unpack('<I', index[tmp_offset:tmp_offset + 4])[0]
    max_comp_len = offset - 1028
    start = start * 8 + 1024
    index_offset = 0
    while start < max_comp_len:
        if struct.unpack('>I', index[start:start + 4])[0] >= nip:
            index_offset = struct.unpack('<I', index[start + 4:start + 7] + chr(0))[0]
            index_length = struct.unpack('B', index[start + 7])[0]
            break
        start += 8
    if index_offset == 0:
        return "N/A"
    f.seek(offset + index_offset - 1024, 0)
    result = f.read(index_length)
    f.close()
    return result


if __name__ == "__main__":
    print find_by_ip("www.baidu.com")
