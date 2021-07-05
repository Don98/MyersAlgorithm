import argparse
import copy

def get_path(all_v,char1,char2):
    d1 = len(all_v)-1
    x1 = len(char1)
    y1 = len(char2)
    path = [(x1,y1)]
    for i in range(0,d1):
        d = d1 - i
        v = all_v[d]
        vP= all_v[d-1]
        k = x1 - y1
        down = False
        if(k == -d or (k != d and v[k - 1] < v[k + 1])):
            down = True
        kPrev = k - 1
        if down:
            kPrev = k + 1
        x0 = vP[kPrev]
        y0 = x0 - kPrev
        x1,y1 = x0,y0
        path.append((x0,y0))
        while(x0 >= 0 and y0 >= 0 and char1[x0-1] == char2[y0-1]):
            x0 -= 1
            y0 -= 1
            path.append((x0,y0))
    return path
        
def char_diff(char1,char2):
    length1 = len(char1)
    length2 = len(char2)
    all_length = len(char1) + len(char2)
    all_v = []
    v = {1:0}
    flag = False
    for d in range(0,all_length):
        for k in range(-d,d+1,2):
            x = 0
            if(k == -d or (k != d and v[k - 1] < v[k + 1])):
                x = v[k+1]
            else:
                x = v[k-1]+1
            y = x - k
            while(x < length1 and y < length2 and char1[x] == char2[y]):
                x += 1
                y += 1
            v[k] = x
            if(x >= length1 and y >= length2):
                flag = True
                break
        all_v.append(copy.deepcopy(v))
        if flag:
            break
    path = get_path(all_v,char1,char2)
    for i in path[::-1]:
        print(i)
        
def main(args=None):
    parser = argparse.ArgumentParser(description='Simple Myer Algorithm')

    parser.add_argument('--char1', help='char1.')
    parser.add_argument('--char2', help='char2')
    parser.add_argument('--file1', help='file1')
    parser.add_argument('--file2', help='file2')
    
    parser = parser.parse_args(args)
    
    if(parser.char1 != None and parser.char2 != None):
        char_diff(parser.char1,parser.char2)
if __name__ == '__main__':
    main()