import json

if __name__ == '__main__':
    a = json.load(open('train.json', 'r'))
    refer = 0
    sentence_len = 0
    error = 0
    total = 0
    for item in a:
        refer += len(item['target'])
        sentence_len += len(item['source'])
        if item['source'] != item['target'][0]:
            error += 1
        total += 1

    print('sentence_len', sentence_len/total)
    print('refer', refer/total)
    print('error_rate', error/total)