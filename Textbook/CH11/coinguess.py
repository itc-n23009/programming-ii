import random
guess = ''
while guess not in ('表', '裏'):
    print('コインの裏表を当ててください。表か裏を入力してください:')
    guess = input()
toss = random.randint(['表',' 裏'])
if toss == guess:
    print('当たり！')
else:
    print('はずれ！もう一回当てて！')
    guess = input()
    if toss == guess:
        print('当たり！')
    else:
        print('はずれ。このゲームは苦手ですね。')
