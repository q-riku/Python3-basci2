def get_input():
  command = input(": ").split() #返回是一个列表 以空格符
  verb_word = command[0] #say
  if verb_word in verb_dict:
    verb = verb_dict[verb_word] #verb = say
  else:
    print("Unknown verb {}". format(verb_word))
    return
  if len(command) >= 2:
    noun_word = command[1]
    print (verb(noun_word)) #verb()==say('hello')方法；
  else:
    print(verb("nothing"))
def say(noun):
  return 'You said "{}"'.format(noun)
#这个字典很重要；
verb_dict = {
  "say": say,
}
while True:
  get_input()