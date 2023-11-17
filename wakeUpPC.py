import socket
import binascii


def wake_on_lan(macaddress):
    # MACアドレスをバイナリ形式に変換
    macaddress = macaddress.replace(":", "").replace("-", "")
    macaddress = binascii.unhexlify(macaddress)

    # Wake-on-LANマジックパケットの作成
    magic_packet = b"\xff" * 6 + macaddress * 16

    # 対象のMacBookのIPアドレスとポート番号
    target_address = ("192.168.11.1", 8080)

    # マジックパケットを送信
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(magic_packet, target_address)


# 対象PCのMACアドレスを指定
target_mac = "08:f8:bc:6c:9f:29"
wake_on_lan(target_mac)
