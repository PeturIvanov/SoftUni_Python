from abc import ABC, abstractmethod

class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass

class IContent(ABC):
    def __init__(self, text ,content_type):
        self.content_type = content_type
        self.text = text

    @abstractmethod
    def format_content(self):
        pass

class MyContent(IContent):
    def format_content(self):
        return ''.join([self.content_type, self.text, self.content_type])

class IReceiver(ABC):
    def __init__(self, protocol, receiver):
        self.protocol = protocol
        self.receiver = receiver

    @abstractmethod
    def format_receiver(self):
        pass

class Receiver(IReceiver):
    def format_receiver(self):
        return ' '.join([self.protocol, self.receiver])

class ISender(ABC):
    def __init__(self, sender):
        self.sender = sender

    @abstractmethod
    def format_sender(self, protocol: str):
        pass

class Sender(ISender):
    def format_sender(self, protocol: str):
        return ' '.join([protocol, self.sender])


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender: ISender):
        self.__sender = sender.format_sender(self.protocol)

    def set_receiver(self, receiver: IReceiver):
        self.__receiver = receiver.format_receiver()

    def set_content(self, content):
        self.__content = content.format_content()

    def __repr__(self):
        return f"Sender: {self.__sender}\n" \
               f"Receiver: {self.__receiver}\n" \
               f"Content:\n" \
               f"{self.__content}"



email = Email("I'm")

sender = Sender("qmal")
email.set_sender(sender)

receiver = Receiver("Hi i'm", 'james')
email.set_receiver(receiver)

content = MyContent('Hello, there!', '<MyML>')
email.set_content(content)

print(email)


