import array
import random


def get_ref_array(size: int):
    return [random.randint(1, 9) for _ in range(size)]

def get_page_frames():
    return random.randint(1, 7)

def optimalPage(pg, pn, fn):
    fr = array.array('i', [-1] * fn)
    hit = 0
    for i in range(pn):
        # Page found in a frame : HIT
        found = False
        for j in range(fn):
            if fr[j] == pg[i]:
                hit += 1
                found = True
                break

        if found:
            continue

        # Page not found in a frame : MISS
        emptyFrame = False
        for j in range(fn):
            if fr[j] == -1:
                fr[j] = pg[i]
                emptyFrame = True
                break

        if emptyFrame:
            continue

        # Find the page to be replaced.
        farthest = -1
        replaceIndex = -1
        for j in range(fn):
            k = i + 1
            while (k < pn):
                if fr[j] == pg[k]:
                    if k > farthest:
                        farthest = k
                        replaceIndex = j
                    break
                k += 1
            if k == pn:
                replaceIndex = j
                break
        fr[replaceIndex] = pg[i]

    print("Hits =", hit)
    print("Misses =", pn - hit)


if __name__ == "__main__":
    ref_size = 10
    pg = get_ref_array(ref_size)
    pn = len(pg)
    fn = get_page_frames()
    print("Reference String =", pg)
    print("Page Frames =", fn)
    optimalPage(pg, pn, fn)