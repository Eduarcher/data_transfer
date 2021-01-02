while True:
    data_size_type = input("Enter type of data size(GB, kb, Kb, Byte, bit...) :")
    transfer_rate_type = input("Enter type of data transfer rate(GBps, KBps, Mbps, Bps...) :")

    data_size = int(input("Enter data size :"))
    transfer_rate = int(input("Enter transfer rate :"))

    # convert to bits the size
    if data_size_type == "bit":
        pass
    elif data_size_type == "Kb":
        data_size = data_size * 1e3
    elif data_size_type == "Mb":
        data_size = data_size * 1e6
    elif data_size_type == "Gb":
        data_size = data_size * 1e9
    elif data_size_type == "Tb":
        data_size = data_size * 1e12
    elif data_size_type == "Byte":
        data_size = data_size * 8
    elif data_size_type == "KB":
        data_size = data_size * (2 ** 10) * 8
    elif data_size_type == "MB":
        data_size = data_size * (2 ** 20) * 8
    elif data_size_type == "GB":
        data_size = data_size * (2 ** 30) * 8
    elif data_size_type == "TB":
        data_size = data_size * (2 ** 40) * 8

    # Convert to bits the transfer rate
    if transfer_rate_type == "bps":
        pass
    elif transfer_rate_type == "Kbps":
        transfer_rate = transfer_rate * 1e3
    elif transfer_rate_type == "Mbps":
        transfer_rate = transfer_rate * 1e6
    elif transfer_rate_type == "Gbps":
        transfer_rate = transfer_rate * 1e9
    elif transfer_rate_type == "Tbps":
        transfer_rate = transfer_rate * 1e12
    elif transfer_rate_type == "Bps":
        transfer_rate = transfer_rate * 8
    elif transfer_rate_type == "KBps":
        transfer_rate = transfer_rate * 8 * 1e3
    elif transfer_rate_type == "MBps":
        transfer_rate = transfer_rate * 8 * 1e6
    elif transfer_rate_type == "GBps":
        transfer_rate = transfer_rate * 8 * 1e9
    elif transfer_rate_type == "TBps":
        transfer_rate = transfer_rate * 8 * 1e12

    res = data_size/transfer_rate
    print(round(res, 2), " seconds", "\n")
