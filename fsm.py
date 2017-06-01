from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'i want graduate'
    def on_enter_state1(self, update):
        text = update.message.text
        update.message.reply_text("Poor guy, how many credits you want earn this semester?")
    def is_going_to_state1_2(self, update):
        text = update.message.text
        return text.lower() == '25'
    def on_enter_state1_2(self, update):
        update.message.reply_text("Be sure not to earn less than 13 credits...")
    def is_going_to_state1_3(self, update):
        text = update.message.text
        return text.lower() == 'thanks'
    def on_enter_state1_3(self, update):
        update.message.reply_text("You are welcome.")
        self.go_back(update)

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'i want eat'
    def on_enter_state2(self, update):
        text = update.message.text
        update.message.reply_text("OK, go out and find something to eat!!")
    def is_going_to_state2_2(self, update):
        text = update.message.text
        return text.lower() == 'can you buy for me'
    def on_enter_state2_2(self, update):
        update.message.reply_text("Dude, i am just a robot...")
    def is_going_to_state2_3(self, update):
        text = update.message.text
        return text.lower() == 'useless'
    def on_enter_state2_3(self, update):
        update.message.reply_text("YOU credit me.")
        self.go_back(update)

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'i am 21ed'
    def on_enter_state3(self, update):
        text = update.message.text
        update.message.reply_text("Told you not to play LOL to much...")
    def is_going_to_state3_2(self, update):
        text = update.message.text
        return text.lower() == 'what can i do'
    def on_enter_state3_2(self, update):
        update.message.reply_text("Don't be 21ed twice of course!!")
    def is_going_to_state3_3(self, update):
        text = update.message.text
        return text.lower() == 'already twice'
    def on_enter_state3_3(self, update):
        update.message.reply_text("Holy,sxxt...")
        self.go_back(update)
