import time

# print('Starting: %s' % time.ctime())
#
# time.sleep(3)
# print('After: %s' % time.ctime())
#


# timer

seconds = 4
while seconds != 0:
    print(f"Voce tem {seconds} segundos para responder...")
    time.sleep(2)
    seconds -=1
print('Game Over, você morreu!')