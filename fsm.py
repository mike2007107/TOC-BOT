from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def on_enter_state1(self, update):
        text = update.message.text
        a = int(text)
        update.message.reply_text(str(a))

    def on_exit_state1(self, update):
        print('Leaving state1')

    def is_going_to_state1_2(self, update):
        text = update.message.text
        return text == 'hhh'
    def on_enter_state1_2(self, update):
        update.message.reply_text("xxx")
    def is_going_to_state1_3(self, update):
        text = update.message.text
        return text == 'ccc'
    def on_enter_state1_3(self, update):
        update.message.reply_text("bbb")
        self.go_back(update)




    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'go to state2'
    def on_enter_state2(self, update):
        update.message.reply_text("I'm entering state2")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')
