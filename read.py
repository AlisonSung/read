import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value = 1000000)
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        bar.update(count)
print('Done the file reading, there are',len(data),'reviews')

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print('The average length of review is', sum_len/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('There are', len(new), 'reviews shorter than 100 words')
print(new[0])
print(new[1])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('There are', len(good),'review mentioned good')

# count words
start_time = time.time()
wc = {} #word_count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 # add new key to wc

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])
end_time = time.time()
print('It spends', end_time-start_time, 'seconds')

print(len(wc)) 

while True:
    word = input('What do you want to search:')
    if word == 'q':
        break
    if word in wc:
        print('The', word, 'printed', wc[word], 'times.' )
    else:
        print('No data')
print('Thank you for searching.')             



















