from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

class LessonsApp(App):
	def update_label(self):
		self.lbl.text = self.formula

	def add_operation(self, instance):
		if(str(instance.text).lower() == 'формула хартли'):
			self.formula = ""
			self.formula += ' вот формула Хартли:I = Log2 * N'
		elif(str(instance.text).lower() == 'скорость техническая'):
			self.formula = ""
			self.formula += ' техническая скорость вычисляется по формуле:Vт = 1/T     (Т - ед. бод)'
		elif(str(instance.text).lower() == 'скорость передачи информации'):
			self.formula = ""
			self.formula += ' скорость передачи информации по формуле: V = I/t'
		elif(str(instance.text).lower() == 'пропускная способность канала связи'):
			self.formula = ""
			self.formula += ' пропускная способность канала связи: C = Logm I * t'
		else:
			self.formula += str(instance.text)
		self.update_label()

	def build(self):
		self.formula = 'какая формула тебе нужна?'

		bl = BoxLayout(orientation = 'vertical', padding=25)
		gl = GridLayout(cols=1, spacing=3, size_hint = (1, .5))
		self.lbl = Label(text='какая формула тебе нужна?', size_hint = (1, .5))
		bl.add_widget(self.lbl)
		
		gl.add_widget(Button(text='формула хартли', on_press = self.add_operation))
		gl.add_widget(Button(text='скорость техническая', on_press = self.add_operation))
		gl.add_widget(Button(text='скорость передачи информации', on_press = self.add_operation))
		gl.add_widget(Button(text='пропускная способность канала связи', on_press = self.add_operation))
		
		bl.add_widget(gl)
		return bl

if __name__ == '__main__':
	LessonsApp().run()