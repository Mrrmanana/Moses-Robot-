from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import requests

class MosesApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        self.title = Label(text='MOSES ROBOT\n346224474 XM Demo\nEURUSD M15', font_size=18)
        self.price = Label(text='Connecting...', font_size=40, bold=True)
        self.trend = Label(text='Loading real market...', font_size=16)
        self.signal = Label(text='Waiting...', font_size=18, bold=True)
        self.layout.add_widget(self.title)
        self.layout.add_widget(self.price)
        self.layout.add_widget(self.trend)
        self.layout.add_widget(self.signal)
        Clock.schedule_interval(self.update, 10)
        self.update(0)
        return self.layout
    def get_price(self):
        try:
            url = "https://query1.finance.yahoo.com/v8/finance/chart/EURUSD=X?interval=15m&range=1d"
            r = requests.get(url, headers={"User-Agent":"Mozilla/5.0"}, timeout=10).json()
            closes = r['chart']['result'][0]['indicators']['quote'][0]['close']
            closes = [c for c in closes if c is not None]
            return closes[-30:]
        except:
            return None
    def update(self, dt):
        candles = self.get_price()
        if not candles or len(candles) < 20:
            return
        fast = sum(candles[-10:])/10
        slow = sum(candles[-20:])/20
        price = candles[-1]
        gap = abs(fast-slow)*10000
        self.price.text = f"{price:.5f}"
        self.trend.text = f"Fast {fast:.5f} Slow {slow:.5f}\nGap {gap:.1f} pips"
        if fast > slow and gap < 2:
            self.signal.text = f"BUY NOW {price:.5f}\nBUY 0.01 in XM!"
        elif fast < slow and gap < 2:
            self.signal.text = f"SELL NOW {price:.5f}\nSELL 0.01 in XM!"
        else:
            self.signal.text = "Waiting for cross..."
MosesApp().run()
