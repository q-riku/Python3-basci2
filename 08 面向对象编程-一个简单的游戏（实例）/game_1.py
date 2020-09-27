"""
  我们创建了一个 Goblin 类，它继承自 GameObjects 类。
  我们还创建了一个新的函数 examine，它返回对象的描述。
  现在我们可以添加一个新的 “examine” 动词到我们的字典，并尝试一下！
"""
class GameObject:
  class_name = ""
  desc = ""
  objects = {}
  def __init__(self, name):
    self.name = name
    GameObject.objects[self.class_name] = self #字典
  def get_desc(self):
    return self.class_name + "\n" + self.desc

class Goblin(GameObject): #goblin精灵类
  class_name = "goblin"
  desc = "A foul creature" #肮脏的动物；
goblin = Goblin("Gobbly")

def examine(noun): #添加一个检查的方法；
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc() #GameObject.objects[noun]==self.get_desc()
  else:
    return "There is no {} here.".format(noun)

def get_input():
  command = input(": ").split() #返回一个列表；
  verb_word = command[0]
  if verb_word in verb_dict:
    verb = verb_dict[verb_word] #say examine
  else:
    print("Unknown verb {}". format(verb_word))
    return
  if len(command) >= 2:
    noun_word = command[1]
    print (verb(noun_word)) #可变函数 verb(nonu_word)==say(nonu_word) examine('goblin')
  else:
    print(verb("nothing"))
def say(noun):
  return 'You said "{}"'.format(noun)
verb_dict = {
  "say": say,
  "examine":examine #记得添加到字典里面；
}
while True:
  get_input()