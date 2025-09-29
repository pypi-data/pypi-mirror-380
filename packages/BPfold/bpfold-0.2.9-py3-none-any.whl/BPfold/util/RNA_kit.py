import re

import numpy as np

from .misc import get_file_name
from .base_pair_probability import CDP_BPPM


def read_fasta(path):
    '''
    Read iterator of all sequences from a fasta file.

    Parameters
    ----------
    path: str
        Path of fasta file.

    Returns
    -------
    yield: (str, str)
        (seq_name, seq)
    '''
    seq_name = None
    with open(path) as fp:
        for line in fp.readlines():
            line = line.strip(' \n\r\t')
            if line.startswith('#') or line=='':
                continue
            elif line.startswith('>'):
                seq_name = line[1:]
            else:
                yield seq_name, line


def write_fasta(path:str, name_seq_pairs:[(str, str)])->None:
    with open(path, 'w') as fp:
        for name, seq in name_seq_pairs:
            fp.write(f'>{name}\n{seq}\n')


def read_SS(path:str, return_index:bool=False):
    '''
    Read secondary structure from bpseq/ct/dbn file.

    Parameters
    ----------
    path: str
        path of ss file, endswith '.bpseq', '.ct', '.dbn'
    return_index : bool
        indicate whether this function returns indexes of all bases

    Returns
    -------
    seq: str, length L
        Containing RNA bases: AUGC.
    connects: [int], length L
        The i-th base connects to `connects[i-1]`-th base, 1-indexed, 0 for no connection.
    index: [int], length L
        list of base indexes, if valid, = list(range(1, 1+L))
    '''
    low_path = path.lower()
    if low_path.endswith('.bpseq'):
        return read_bpseq(path, return_index)
    elif low_path.endswith('.ct'):
        return read_ct(path, return_index)
    elif low_path.endswith('.dbn'):
        return read_dbn(path, return_index)
    else:
        raise Exception(f'[Error] Unkown file type: {path}')


def read_dbn(path:str, return_index:bool=False):
    seq = dbn = ''
    with open(path) as fp:
        for line in fp.readlines():
            line = line.strip('\r\n ')
            if not line or line.startswith('>') or line.startswith('#'):
                continue
            elif line[0].isalpha():
                if dbn:
                    break
                seq += line
            else:
                dbn += line
    connects = dbn2connects(dbn)
    if return_index:
        return seq, connects, list(range(1, 1+len(connects)))
    else:
        return seq, connects


def read_bpseq(path:str, return_index:bool=False):
    '''
    Read bpseq file.

    Parameters
    ----------
    path: str
        Path of bpseq file.
    return_index: bool
        indicate whether this function returns indexes of all bases

    Returns
    -------
    seq: str, length L
        Containing RNA bases: AUGC.
    connects: [int], length L
        The i-th base connects to `connects[i-1]`-th base, 1-indexed, 0 for no connection.
    index: [int], length L
        list of base indexes, if valid, = list(range(1, 1+L))
    '''
    bases = []
    connects = []
    indexes = []
    with open(path) as f:
        for line in f.readlines():
            if not line.startswith('#'):
                idx, base, conn = [item for item in line.strip('\n\t\r ').split() if item]
                bases.append(base)
                connects.append(conn)
                indexes.append(int(idx))
    connects = [int(i) for i in connects]
    if return_index:
        return ''.join(bases), connects, indexes
    else:
        return ''.join(bases), connects


def read_ct(path:str, return_index:bool=False):
    '''
    Read ct file.

    Parameters
    ----------
    path: str
        Path of ct file.
    return_index: bool
        indicate whether this function returns indexes of all bases

    Returns
    -------
    seq: str, length L
        Containing RNA bases: AUGC.
    connects: [int], length L
        The i-th base connects to `connects[i-1]`-th base, 1-indexed, 0 for no connection.
    index: [int], length L
        list of base indexes, if valid, = list(range(1, 1+L))
    '''
    bases = []
    connects = []
    indexes = []
    last_idx = 0
    pattern = r'(?P<idx>\d+)[\t ]+(?P<base>.)[\t ]+(?P<pre>\d+)[\t ]+(?P<nxt>\d+)[\t ]+(?P<conn>-?\d+)[\t ]+(?P<cur>\d+)'
    with open(path) as fp:
        for idx, base, pre, nxt, conn, cur in re.findall(pattern, fp.read()):
            # print(idx, base, pre, nxt, conn, cur)
            try:
                assert int(nxt)==0 or (int(cur) == int(nxt)-1 == int(pre)+1)
            except Exception as e:
                print(e)
                continue
            idx, conn = int(idx), int(conn)
            if conn < 0:
                conn = 0
            if idx!=last_idx+1:
                raise Exception(f'[Error] Inconsistent bases (line={last_idx}): {path}')
            last_idx = idx
            bases.append(base)
            connects.append(conn)
            indexes.append(idx)
    if return_index:
        return ''.join(bases), connects, indexes
    else:
        return ''.join(bases), connects


def write_SS(path:str, seq:str, connects:[int])->None:
    '''
    Write secondary structure to bpseq/ct/dbn.

    Parameters
    ----------
    path: str
        Dest path.
    seq: str, length L
        Containing RNA bases: AUGC.
    connects: [int], length L
        The i-th base connects to `connects[i-1]`-th base, 1-indexed, 0 for no connection.
    '''
    low_path = path.lower()
    if low_path.endswith('bpseq'):
        write_bpseq(path, seq, connects)
    elif low_path.endswith('ct'):
        write_ct(path, seq, connects)
    elif low_path.endswith('dbn'):
        write_dbn(path, seq, connects)
    else:
        raise Exception(f'Unkown file type: {path}, only .ct, .bpseq, .dbn are allowed.')


def write_dbn(path:str, seq:str, connects:[int])->None:
    '''
    Write secondary structure to dbn file.

    Parameters
    ----------
    path: str
        Dest path.
    seq: str, length L
        Containing RNA bases: AUGC.
    connects: [int], length L
        The i-th base connects to `connects[i-1]`-th base, 1-indexed, 0 for no connection.
    '''
    with open(path, 'w') as f:
        dbn = connects2dbn(connects)
        f.write(f'{seq}\n{dbn}\n')


def write_ct(path:str, seq:str, connects:[int])->None:
    '''
    Write secondary structure to ct file.

    Parameters
    ----------
    path: str
        Dest path.
    seq: str, length L
        Containing RNA bases: AUGC.
    connects: [int], length L
        The i-th base connects to `connects[i-1]`-th base, 1-indexed, 0 for no connection.
    '''
    with open(path, 'w') as f:
        for i, (base, connect) in enumerate(zip(seq, connects)):
            f.write(f'{i+1} {base.upper()} {i} {i+2} {connect} {i+1}\n')


def write_bpseq(path:str, seq:str, connects:[int], comments=None)->None:
    '''
    Write secondary structure to bpseq file.

    Parameters
    ----------
    path: str
        Dest path.
    seq: str, length L
        Containing RNA bases: AUGC.
    connects: [int], length L
        The i-th base connects to `connects[i-1]`-th base, 1-indexed, 0 for no connection.
    '''
    with open(path, 'w') as f:
        if comments is not None:
            f.write(f'# {comm}\n')
        for i, (base, connect) in enumerate(zip(seq, connects)):
            f.write(f'{i+1} {base.upper()} {connect}\n')


def dispart_nc_pairs(seq:str, connects:[int], extra_nc_positions=None)->[int]:
    '''
    Dispart canonical and noncanonical pairs in connects.

    Parameters
    ----------
    seq: str
        RNA base seq
    connects: [int], length L
        The i-th base connects to `connects[i-1]`-th base, 1-indexed, 0 for no connection.

    Returns
    -------
    connects: [int], length L
    nc_connects: [int], length L
    '''
    L = len(seq)
    assert L == len(connects) != 0
    seq = seq.upper()
    canonical_pairs = {'AU', 'UA', 'GC', 'CG', 'GU', 'UG'}
    conns = [0] * L
    nc_conns = [0] * L
    if extra_nc_positions is None:
        extra_nc_positions = [False] * L
    for idx, (base, conn) in enumerate(zip(seq, connects)):
        if conn!=0 and idx<conn-1:
            pair = base + seq[conn-1]
            if pair in canonical_pairs:
                conns[idx] = conn
                conns[conn-1] = idx+1
            else:
                nc_conns[idx] = conn
                nc_conns[conn-1] = idx+1
            # extra nc positions
            if extra_nc_positions[idx] or extra_nc_positions[conn-1]:
                nc_conns[idx] = conn
                nc_conns[conn-1] = idx+1
    return conns, nc_conns


def merge_connects(connects:[int], nc_connects:[int])->[int]:
    '''
    Merge canonical and noncanonical pairs in connects.

    Parameters
    ----------
    connects: [int], length L
        The i-th base connects to `connects[i-1]`-th base, 1-indexed, 0 for no connection.

    Returns
    -------
    connects: [int], length L
    '''
    n = len(connects)
    n1 = len(nc_connects)
    assert n==n1, f'length mismatch: {n}!={n1}'
    ret_connects = connects[:]
    dic = {i+1: conn for i, conn in enumerate(connects)}
    for i, conn in enumerate(nc_connects):
        if conn!=0 and i<conn:
            if connects[i]==0 and connects[conn-1]==0:
                ret_connects[i] = conn
                ret_connects[conn-1] = i+1
    return ret_connects


def remove_lone_pairs(connects:[int], loop_len:int=3)->[int]:
    '''
    Remove lone pairs in connects

    Parameters
    ----------
    connects: [int], length L
        The i-th base connects to `connects[i-1]`-th base, 1-indexed, 0 for no connection.
    loop_len: int
        interval of lone pair and other pair

    Returns
    -------
    connects: [int], length L
        The i-th base connects to `connects[i-1]`-th base, 1-indexed, 0 for no connection.
    '''
    L = len(connects)
    ret_conn = [0] * L
    for idx, conn in enumerate(connects):
        if conn!=0 and idx<conn-1:
            isLone = True
            for center, conj in [(idx, conn-1), (conn-1, idx)]:
                for dire in [-1, 1]:
                    neighbor = center + dire
                    if 0 <= neighbor < L:
                        if connects[neighbor]-1 in [conj-i*dire for i in range(1, loop_len+1)]:
                            isLone = False
                            break
                if not isLone:
                    break
            if not isLone:
                ret_conn[idx] = conn
                ret_conn[conn-1] = idx+1
    return ret_conn


def dbn2connects(dbn:str)->[int]:
    '''
    Convert dbn to connects.

    Parameters
    ----------
    dbn: str
        Dot-bracket notation of secondary structure, including '.()[]{}', with valid brackets.

    Returns
    -------
    connects: [int], length L
        The i-th base connects to `connects[i-1]`-th base, 1-indexed, 0 for no connection.
    '''
    alphabet = ''.join([chr(ord('A')+i) for i in range(26)])
    alphabet_low = alphabet.lower()
    syms = ('([{<' + alphabet)[::-1]
    syms_conj = (')]}>' + alphabet_low)[::-1]
    left2right = {p: q for p, q in zip(syms, syms_conj)}
    right2left = {p: q for p, q in zip(syms_conj, syms)}

    pair_dic = {}
    stack_dic = {char: [] for char in left2right}
    for i, char in enumerate(dbn):
        idx = i+1
        if char=='.':
            pair_dic[idx] = 0
        elif char in left2right:
            stack_dic[char].append((idx, char))
        elif char in right2left:
            cur_stack = stack_dic[right2left[char]]
            if len(cur_stack)==0:
                raise Exception(f'[Error] Invalid brackets: {dbn}')
            p, ch = cur_stack.pop()
            pair_dic[p] = idx
            pair_dic[idx] = p
        else:
            raise Exception(f'[Error] Unknown DBN representation: dbn[{i}]={char}: {dbn}')
    if any(stack for k, stack in stack_dic.items()):
        raise Exception(f'[Error] Brackets dismatch: {dbn}')
    connects = [pair_dic[i] for i in range(1, 1+ len(dbn))]
    return connects


def connects2dbn(connects:[int])->str:
    '''
    Convert connects to dbn. [Warning] Can't deal with pseudo knot.

    Parameters
    ----------
    connects: [int], length L
        The i-th base connects to `connects[i-1]`-th base, 1-indexed, 0 for no connection.

    Returns
    -------
    dbn: str
        Dot-bracket notation of secondary structure, including '.()[]{}', with valid brackets.
    '''
    alphabet = ''.join([chr(ord('A')+i) for i in range(26)])
    alphabet_low = alphabet.lower()
    syms = ('([{<' + alphabet)[::-1]
    syms_conj = (')]}>' + alphabet_low)[::-1]
    syms_set = set(syms)
    syms_conj_set = set(syms_conj)
    ret = ['.']*len(connects)
    for i, conn in enumerate(connects):
        pi = conn-1
        if pi != -1 and pi>=i:
            counts = [0] * len(syms)
            for j in range(i+1, pi):
                sym = ret[j]
                if sym in syms_set:
                    ct_idx = syms.index(sym)
                    counts[ct_idx] +=1
                elif sym in syms_conj_set:
                    ct_idx = syms_conj.index(sym)
                    counts[ct_idx] -=1
            for idx, ct in enumerate(counts):
                if ct==0:
                    ret[i] = syms[idx]
                    ret[pi] = syms_conj[idx]
    return ''.join(ret)


def mat2connects(mat, loop_min_len=2, greedy_max_matching=True)->[int]:
    '''
    Convert contact map to connects, enforce single pairing.

    Parameters
    ----------
    mat: numpy.ndarray
        LxL matrix where the mat[i,j]=score, the biger, the more probable to pair.

    Returns
    -------
    connects: [int], length L
        The i-th base connects to `connects[i-1]`-th base, 1-indexed, 0 for no connection.
    '''
    if greedy_max_matching:
        # enforce single pairing
        mat = greedy_max_weight_matching(mat)
    connects = mat.argmax(axis=1)
    connects[connects!=0] +=1
    if connects[0]!=0:
        connects[connects[0]-1] = 1
    return connects.tolist()


def greedy_max_weight_matching(M):
    '''
    Greedy max weight matching, fast, but may not be optimal.
    '''
    n = len(M)
    M_new = np.zeros((n, n), dtype=float)
    used = set()
    
    # Flatten and sort all possible pairs by score (descending)
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            if M[i][j] > 0:
                pairs.append((M[i][j], i, j))
    pairs.sort(reverse=True, key=lambda x: x[0])
    
    # Assign pairs greedily
    for score, i, j in pairs:
        if i not in used and j not in used:
            M_new[i][j] = score
            M_new[j][i] = score
            used.add(i)
            used.add(j)
    return M_new


def nx_max_weight_matching(M):
    '''
    Use pacakge networkx, may be slow when length > 1000.
    '''
    import networkx as nx
    n = len(M)
    G = nx.Graph()
    
    # Add edges with weights (only upper triangle to avoid duplication)
    for i in range(n):
        for j in range(i + 1, n):
            if M[i][j] > 0:
                G.add_edge(i, j, weight=M[i][j])
    
    # Compute maximum weight matching
    matching = nx.max_weight_matching(G, maxcardinality=False)
    
    # Build new contact matrix
    M_new = np.zeros((n, n), dtype=float)
    for i, j in matching:
        M_new[i][j] = M[i][j]
        M_new[j][i] = M[j][i]
    return M_new


def connects2mat(connects:[int], strict=True):
    '''
    Convert connects to contact map.

    Parameters
    ----------
    connects: [int], length L
        The i-th base connects to `connects[i-1]`-th base, 1-indexed, 0 for no connection.
    strict: bool
        if not strict, ignore invalid connects (that exceeds L)

    Returns
    -------
    mat: numpy.ndarray
        LxL matrix where the mat[i,j]=1 represents paired bases, otherwise 0
    '''
    L = len(connects)
    ret = np.zeros((L, L))
    for num, conn in zip(range(1, L+1), connects):
        if conn!=0:
            if (conn-1>=L or num-1 >= L) and not strict:
                continue
            ret[num-1][conn-1] = ret[conn-1][num-1] = 1
    return ret


def read_react(path):
    '''
    Read reactivities from path. It contains white-space-delimited columns. The first column is the nucleotide, the second column is the chemical reactivity. NA reactivity data are denoted as number less than -100, 'NA', or 'nan'.

    Parameters
    ----------
    path: str
        path of reactivity file

    Returns
    -------
    reacts: [float]
    '''
    bases = []
    reacts = []
    with open(path) as fp:
        for line in fp.readlines():
            line = line.strip('\n\t\r ')
            if line:
                if line.startswith('#'):
                    continue
                elif line[0].isdigit():
                    parts = [part for part in line.replace('\t', ' ').split() if part]
                    assert len(parts) in {2,3}, f'[Error] when parsing line {line} from {path}.'
                    idx = int(parts[0])
                    base = react = None
                    if len(parts)==2:
                        react = parts[1]
                    else:
                        base = parts[1]
                        assert base in 'AUGCNT'
                        react = parts[2]
                    bases.append(base)
                    if len(reacts)+1!=idx:
                        reacts += [float('nan') for i in range(idx-1-len(reacts))]
                    if react.lower().startswith('n'):
                        reacts.append(float('nan'))
                    else:
                        reacts.append(float(react))
                else:
                    raise Exception('[Error] when reading react from {path}.')
    return reacts


def write_react(path, reacts, seq=None, delimiter=' '):
    '''
    Write reactivities of seq to path. It contains white-space-delimited columns. The first column is the nucleotide, the second column is the chemical reactivity. NA reactivity data are denoted as number less than -100, 'NA', or 'nan'.

    Parameters
    ----------
    path: str
        path of reactivity file
    reacts: [float]
        reactivities
    seq: str
        AUGCNT
    '''
    if seq is not None:
        assert len(seq) == len(reacts), f'length mismatch, seq={len(seq)}, reacts={len(reacts)}'
    with open(path, 'w') as fp:
        for idx in range(len(reacts)):
            if seq is None:
                fp.write(f'{idx+1}{delimiter}{reacts[idx]}\n')
            else:
                fp.write(f'{idx+1}{delimiter}{seq[idx]}{delimiter}{reacts[idx]}\n')


def valid_ss(seq:str, connects:[int], indexes:[int]=None)->bool:
    return len(seq)>10 and len(seq) == len(connects) and min(connects)>=0 and max(connects)<=len(seq) and (indexes is None or indexes==list(range(1, 1+len(seq))))


def is_valid_bracket(s, ignore_unknown=False):
    chars = set('.()[]{}')
    left2right = {p: q for p, q in ['()', '[]', '{}']}
    right2left = {q: p for p, q in ['()', '[]', '{}']}
    count_dic = {ch: 0 for ch in chars}

    for i, char in enumerate(s):
        count_dic[char] += 1
        if char in '.([{':
            pass
        elif char in ')]}':
            if count_dic[char] > count_dic[right2left[char]]:
                return False
        else:
            if not ignore_unknown:
                raise Exception(f'[Error] Unknown brackets repr: {s}')
    return all(count_dic[char]==count_dic[left2right[char]] for char in '([{')


def mut_seq(seq:str, connects=None)->str:
    '''
    Mutate unknown chars to conj/U.

    Parameters
    ----------
    seq: str, length L
        Containing RNA bases AUGC or other unknown chars.
    connects: [int] or None, length L
        The i-th base connects to `connects[i-1]`-th base, 1-indexed, 0 for no connection.

    Returns
    -------
    new_seq: str, length L
        Containing RNA bases AUGC only.
    '''
    seq = seq.upper().replace('T', 'U')
    if set(seq).issubset(set('AUGC')):
        return seq
    new_seq = []
    chars = {'A', 'U', 'G', 'C'}
    conj = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}
    if connects is None:
        connects = mat2connects(CDP_BPPM(seq))
    for i in range(len(seq)):
        if seq[i] in chars:
            new_seq.append(seq[i])
        else:
            conn = connects[i]
            if conn!=0 and seq[conn-1] in chars:
                new_seq.append(conj[seq[conn-1]])
            else:
                new_seq.append('U')
    return ''.join(new_seq)


def mat2scores(mat, connects, mode)->[float]:
    '''
    NOTICE! Deprecated, discarded!

    Convert contact map to prob scores.

    Parameters
    ----------
    mat: numpy.ndarray
        LxL matrix where the mat[i,j]=1 represents paired bases, otherwise 0
    connects: [int], length L
        The i-th base connects to `connects[i-1]`-th base, 1-indexed, 0 for no connection.
    mode: str
        prob, energy, softmax

    Returns
    -------
    scores: [float], length L
        range [0, 1]
    '''
    def get_pred_score(xs, i, mode):
        if i is None:
            if xs.max()==xs.min()==0:
                return 0
            else:
                return 1
        if mode == 'prob':
            prob = xs[i]
            if prob<=0:
                return 0.0
            if prob>1:
                return 1.0
            else:
                return prob
        elif mode == 'energy':
            RT = 2.4788 # kj/mol
            xs = -xs/RT
            x = xs[i]
            sm_exp = (np.exp(xs)).sum()
            return np.exp(x)/sm_exp
        elif mode == 'softmax':
            x = xs[i]
            sm_exp = (np.exp(xs)).sum()
            return np.exp(x)/sm_exp
    scores = []
    for i in range(len(mat)):
        score = get_pred_score(mat[i], None if connects[i]==0 else connects[i]-1, mode)
        scores.append(score)
    return np.array(scores).tolist()


def parse_stockholm(lines):
    '''
    Stockholm format (e.g. Rfam seed file).

    Parameters
    ----------
    lines : [str]
        lines read from file

    Returns
    -------
    ret: dict
        {'headers': {tag: value}, 'seqs': {name: seq}, 'SS': dbn}
    '''
    ret = {'headers': {}, 'seqs': {}, 'SS': ''}
    for line in lines:
        line = line.strip('\r\n')
        parts = [part for part in line.split() if part]
        if line.startswith('#=GF'):
            ret['headers'][parts[1]] = parts[2]
        elif not line.startswith('#'):
            if len(parts) == 2:
                seq_name, seq = parts
                seq_id = '_'.join(seq_name.split('/'))
                if seq_id in ret['seqs']:
                    ret['seqs'][seq_id] += seq
                else:
                    ret['seqs'][seq_id] = seq
        elif line.startswith('#=GC SS_cons'):
            ret['SS'] += parts[2]
    return ret


def read_stockholm(path):
    '''
    Stockholm format (e.g. Rfam seed file).
    Other method to read: scikit-bio
    ``
        from skbio import Protein, TabularMSA
        msa = TabularMSA.read(fp, constructor=Protein)
    ```

    Parameters
    ----------
    path: str
        stockholm file path

    Returns
    -------
    ret: dict
        {'headers': {tag: value}, 'seqs': {name: seq}, 'SS': dbn}
    '''
    with open(path) as fp:
        return parse_stockholm(fp.readlines())


def process_stockholm_SS(seq, dbn):
    '''
        _：表示间隔区域。
        -：表示缺失或未配对的区域。
        :：表示这些位置的碱基保守性较高或成对概率较高。
        ~: 
        The RNA SS letters are taken from WUSS (Washington University Secondary Structure) notation. Matching nested parentheses characters <>, (), [], or {} indicate a basepair. The symbols '.', ',' and ';' indicate unpaired regions. Matched upper and lower case characters from the English alphabet indicate pseudoknot interactions. The 5' nucleotide within the knot should be in uppercase and the 3' nucleotide lowercase.
    '''
    base_set = set('AUGC')
    unpaired_sym = set('.,_-:~')
    seq = seq.upper()
    ref_dbn = ['.' if sym in unpaired_sym else sym for sym in dbn]
    connects = dbn2connects(ref_dbn)
    # firstly, process ref_dbn, unpair unkown base pairs
    for idx, base in enumerate(seq):
        if base not in base_set: # discard
            if connects[idx]!=0: # if have pair, unpair it
                ref_dbn[idx] = ref_dbn[connects[idx]-1] = '.'
    # then, get final seq and dbn
    seq_lst = []
    dbn_lst = []
    for idx, base in enumerate(seq):
        if base in base_set:
            seq_lst.append(base)
            dbn_lst.append(ref_dbn[idx])
    return ''.join(seq_lst), ''.join(dbn_lst)


def compute_confidence(mat1, mat2, scale_k:float=1.5220298, scale_b:float=-0.08571319, ceiling_01:bool=True)->float:
    return cos_row(mat1, mat2, scale_k, scale_b, ceiling_01)


def cos_row(mat1, mat2, scale_k:float=1, scale_b:float=0, ceiling_01:bool=True)->float:
    '''
    Compute confidence index according to contact maps before and after postprocessing.

    Parameters
    ----------
    mat: np.ndarray
        Contact map.

    Returns
    -------
    CI: float
        confidence index
    '''
    CEILING = 0.98
    FLOOR = 0.0
    inner_prod = 0
    norm1 = norm2 = 0
    for arr1, arr2 in zip(mat1, mat2):
        # np.linalg.norm, np.linalg.det
        norm1 += np.dot(arr1, arr1)
        norm2 += np.dot(arr2, arr2)
        inner_prod += np.dot(arr1, arr2)
    if norm1 == 0 and norm2 == 0: # NOTICE! zero vector
        return CEILING # don't use 1
    elif norm1 == 0 or norm2 == 0:
        return FLOOR
    else:
        CI = inner_prod/((norm1*norm2)**0.5)
        # The linear coeffs are for rescale CI to [0, 1], which is the range of F1
        if scale_k and scale_b is not None:
            CI = scale_k*(CI.item()) + scale_b
        if ceiling_01:
            return min(CEILING, max(FLOOR, CI))
        else:
            return CI


def _cal_metric_from_tp(length, pred_p, gt_p, tp, eps=1e-12):
    '''
        pred_p, gt_p, tp can be tensors, can be on GPUs

        accuracy: acc = (TP+TN)/(TP+FP+FN+TN)
        precision: p = TP/(TP+FP)
        recall: r = TP/(TP+FN)
        F1: F1 = 2*p*r / (p+r)
        sensitivity = recal = TPR (true positive rate)
        specificity = TN/(TN+FP)
        YoudenIndex = sen + spe - 1
        false positive rate: FPR = FP/(TN+FP) = 1-spe
        positive predicted value: PPV = precision
        negative predicted value: NPV = TN/(TN+FN)
    '''
    assert 0 <= tp <= pred_p <= length and 0 <= tp <= gt_p <= length, f'length={length}, pred_p={pred_p}, gt_p={gt_p}, tp={tp}'
    fp = pred_p - tp
    fn = gt_p - tp
    tn = length - tp - fp - fn
    metric_dic = {
            'F1': (2*tp + eps)/(2*tp + fp + fn + eps),
            'ACC': (tp + tn + eps)/(tp + fp + fn + tn + eps),
            'MCC': (tp * tn - fp * fn + eps)/(((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))**0.5+eps),
            'Precision': (tp + eps)/(tp+fp+eps),
            'Recall': (tp + eps)/(tp+fn+eps),
           }
    metric_dic['INF'] = (metric_dic['Precision']*metric_dic['Recall'])**0.5
    # print(length, pred_p, gt_p, tp, fp, tn, fn)
    # print(metric_dic)
    for k, v in metric_dic.items():
        if k in ['F1', 'ACC', 'Precision', 'Recall', 'INF']:
            assert 0 <= v <= 1, f'{k}={v}'
        elif k == 'MCC':
            assert -1 <= v <= 1, f'{k}={v}'
        else:
            raise Exception(f'Unkonwn metric name: {k}')
    return metric_dic


def cal_metric(pred_mat, gt_mat):
    '''
        pred_mat, gt_mat: LxL, 0, 1 valued
    '''
    L = len(pred_mat)
    if L!=len(gt_mat):
        raise Exception(f'[Error]: lengthes dismatch: pred {L}!= gt {len(gt_mat)}')
    if L==0:
        return 1
    assert len(pred_mat[0])==len(gt_mat[0])==L, f'[Error] Contact map shape inconsistent: {L}!={pred_mat[0]}, {gt_mat[0]}'
    pred_p = gt_p = tp = 0 # predpair, gtpair, paired
    for i in range(L):
        for j in range(L):
            pred = pred_mat[i, j]
            gt = gt_mat[i, j]
            if gt!=0:
                gt_p +=1
            if pred!=0:
                pred_p +=1
                if pred==gt:
                    tp +=1
    return _cal_metric_from_tp(L*L, pred_p, gt_p, tp)


def cal_metric_pairwise(pred_pairs:[int], gt_pairs:[int]):
    '''
        # deprecated
        pred_pairs, gt_pairs: connections, 1-indexed
        return: MCC, INF, F1, precision, recall
    '''
    length = len(pred_pairs)
    if length!=len(gt_pairs):
        raise Exception(f'[Error]: lengthes dismatch: pred {length}!= gt {len(gt_pairs)}')
    pred_p = gt_p = tp = 0 # predpair, gtpair, paired
    for pred, gt in zip(pred_pairs, gt_pairs):
        if gt!=0:
            gt_p +=1
        if pred!=0:
            pred_p +=1
            if pred==gt:
                tp +=1
    return _cal_metric_from_tp(length, pred_p, gt_p, tp)
