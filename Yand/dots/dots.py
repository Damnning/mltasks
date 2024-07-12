def add_to_output(res):
    with open('output.txt', "w") as file:
    	file.write(res)
    
def read_input():
    with open('input.txt') as file:
    	inp = file.read()
    inp = inp.split('\n')
    return inp
    
def count_narrow(gen):
    n = 0
    nums = gen.split(' ')
    nums = list(filter(None, nums))
    nums = list(map(float, nums))
    for i in range(len(nums), 2):
        if(nums[i]**2 + nums[i+1]**2 < 0.5):
            n+=1
    return n

if __name__ == '__main__':
    inp = input()
    result = ''
    for i in inp:
        if(count_narrow(i) > 600):
            result += '1\n'
        else:
            result += '2\n'
    print(result)