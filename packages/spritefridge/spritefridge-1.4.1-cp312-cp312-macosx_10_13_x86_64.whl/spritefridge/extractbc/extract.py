import logging
from match import match_with_errors
from .ioutils import reads_to_byteblocks


def hash_match(seq, bc_dict, min_len, max_len):
    # if we only deal with one length we skip the loop
    if min_len == max_len:
        match = bc_dict.get(seq)
        return match['name'] if match else b'', max_len

    match_name = b''
    for bc_len in range(min_len, max_len + 1):
        match = bc_dict.get(seq[:bc_len])
        if match:
            match_name = match['name']
            break

    return match_name, bc_len


def extract_barcodes(read, bc_dicts, layout, laxity = 6):
    start = 0
    read_bcs = []

    if not layout:
        return read_bcs

    readseq = memoryview(read['seq'])
    # print(readseq)
    for bc_cat, min_bc_len, max_bc_len, allowed_mismatches in layout:
        # this is a shortcut to avoid matching the full SPACER cat
        if bc_cat.startswith('S'):
            # print(bc_cat, start, start + max_bc_len)
            # print(' '* start + readseq[start: start + max_bc_len])
            start += max_bc_len
            continue

        if not allowed_mismatches:
            bc_match, match_len = hash_match(
                readseq[start: start + max_bc_len],
                bc_dicts[bc_cat],
                min_bc_len,
                max_bc_len
            )
            # print(bc_cat, start, start + match_len)
            # print(' '* start + readseq[start: start + match_len])
            read_bcs.append(bc_match)
            start += match_len
            continue
        
        bc_match, match_pos = match_with_errors(
            readseq[start: start + max_bc_len + laxity].tobytes(),
            bc_dicts[bc_cat],
            laxity
        )
        # print(bc_cat, start, start + match_pos + max_bc_len)
        # print(' '* (start + match_pos)  + readseq[start + match_pos : start + match_pos + max_bc_len])
        read_bcs.append(bc_match)
        start += (match_pos + max_bc_len)

    return read_bcs


def extract_parallel(
    bc_dicts,
    layout1,
    layout2,
    laxity,
    input_queue, 
    output_queue
):
    logging.info('start extractor process')
    while True:
        reads = input_queue.get()
        if not reads:
            break

        n_reads = len(reads)
        
        for readpair in reads:
            read1, read2 = readpair
            readpair.append(
                extract_barcodes(read1, bc_dicts, layout1, laxity) +
                extract_barcodes(read2, bc_dicts, layout2, laxity)
            )

        byteblocks, blockstats = reads_to_byteblocks(reads)
        output_queue.put([byteblocks, blockstats, n_reads])

    # termination signal
    logging.info('received empty readlist, shutting down extractor')
    output_queue.put([{}, {}, 0])
