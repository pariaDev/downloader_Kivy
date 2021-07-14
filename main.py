from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.accordion import Accordion,AccordionItem



class app(App):

    title='pariaa'
    def build(self):
        acc=Accordion(orientation='vertical')
        for i in range(6):
            item =AccordionItem(title= str(i))
            item.add_widget(Label(text='fool '*i))
            acc.add_widget(item)

        return acc

if __name__ == "__main__":
    app().run()
