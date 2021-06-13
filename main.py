from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import ObjectProperty

from pytube import YouTube
import instaloader
from instaloader import Instaloader
from instaloader.structures import Post

Builder.load_file('main.kv')

class app(App):
    def build(self):
        return tabpanel()


class tabpanel(TabbedPanel):

    txt = ObjectProperty(None)
    quality_txt = ObjectProperty(None)

    post_url = ObjectProperty(None)
    prof = ObjectProperty(None)

    # error_msg= Label(text='error occurred , please try again later!' ,font_name= 'COMIC', size_hint=(.6, .1))

    def download(self):
         url= self.txt.text
         quality= self.quality_txt.text

         try:
             if quality == "highest":
                 yt= YouTube(url).streams.get_highest_resolution()
             elif quality == 'lowest':
                 yt = YouTube(url).streams.get_lowest_resolution()
             elif quality=='quality':
                 pop = Popup(title='please choose a quality', size_hint=(.5, .15))
                 pop.open()

             else:
                 # print(str(quality))
                 yt = YouTube(url).streams.filter(res=str(quality)).first()

             yt.download()
         except:
             pop = Popup(title='error', size_hint=(.7, .2), content=Label(text=
                'error occurred , please try again!',
                font_name='COMIC', size_hint=(.6, .1),
                pos_hint={'x': .1, 'top': .4}))
             pop.open()

    def d_post(self):

        try:
            if self.post_url.text =='':
                pop = Popup(title='please fill the input box with url or link', size_hint=(.5, .03))
                pop.open()
            else:
                page= instaloader.Instaloader()
                link= self.post_shortcode(self.post_url.text)
                # print(link)
                post= Post.from_shortcode(page.context, link)
                page.download_post(post, target='downloads')
        except :
            pop= Popup(title= 'error' ,size_hint=(.7,.2) ,content=Label(text=
                'error occurred , please try again!' ,font_name= 'COMIC', size_hint=(.6, .1) ,
                pos_hint={'x': .1, 'top': .4}))
            pop.open()

    def d_profile(self):
        try:
            if self.prof.text =='':
                pop = Popup(title='please fill the input box with Id', size_hint=(.5, .15))
                pop.open()
            else:
                page = instaloader.Instaloader()
                id = self.prof.text
                page.download_profile(id, profile_pic_only=True )
        except:
            pop = Popup(title='error', size_hint=(.7, .2), content=Label(text=
                'error occurred , please try again!' ,font_name= 'COMIC', size_hint=(.6, .1),
                pos_hint={'x': .1, 'top': .4}))
            pop.open()



    post_shortcode= lambda self,link: link[28:39]

    def remove_post(self):
        self.post_url.text=''

    def remove_id(self):
        self.prof.text = ''


if __name__ == '__main__':
    app().run()
