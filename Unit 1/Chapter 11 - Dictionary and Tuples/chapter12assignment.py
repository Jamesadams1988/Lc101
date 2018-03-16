class Chatbot:
    """ An object that can engage in rudimentary conversation with a human. """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        """ Returns the Chatbot's way of introducing itself. """
        return "Hello, my name is " + self.name

    def response(self, prompt_from_human):
        """ Returns the Chatbot's response to something the human said. """
        return "It is very interesting that you say: '" + prompt_from_human + "'"

class boredChatbot(Chatbot):
    """ An object that can engage in rudimentary conversation with a human. """
    def __init__(self, name):
        self.name = name

    def conversation(self, prompt_from_human):
        if len(prompt_from_human) > 20:
            return (boredChatbot.response(prompt_from_human))
        else:
            return "zzz... Oh excuse me, I dozed off reading your essay."


def main():
    inp = input("Type what you want the chatbot to respond to:")
    print(boredChatbot.conversation(inp))
   

if __name__ == '__main__':
    main()
