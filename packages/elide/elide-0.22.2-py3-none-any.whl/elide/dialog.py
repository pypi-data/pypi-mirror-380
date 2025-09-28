# This file is part of Elide, frontend to Lisien, a framework for life simulation games.
# Copyright (c) Zachary Spector, public@zacharyspector.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""Generic dialog boxes and menus, for in front of a Board"""

from functools import partial

from kivy.app import App
from kivy.clock import Clock, mainthread
from kivy.core.text import DEFAULT_FONT
from kivy.logger import Logger
from kivy.properties import (
	DictProperty,
	ListProperty,
	NumericProperty,
	ObjectProperty,
	StringProperty,
	VariableListProperty,
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget

from .util import devour, logwrap, store_kv


class Box(Widget):
	padding = VariableListProperty(6)
	border = VariableListProperty(4)
	font_size = StringProperty("15sp")
	font_name = StringProperty(DEFAULT_FONT)
	background = StringProperty()
	background_color = VariableListProperty([1, 1, 1, 1])
	foreground_color = VariableListProperty([0, 0, 0, 1])


class ScrollableLabel(ScrollView):
	font_size = StringProperty("15sp")
	font_name = StringProperty(DEFAULT_FONT)
	color = VariableListProperty([0, 0, 0, 1])
	line_spacing = NumericProperty(0)
	text = StringProperty()


class MessageBox(Box):
	"""Looks like a TextInput but doesn't accept any input.

	Does support styled text with BBcode.

	"""

	line_spacing = NumericProperty(0)
	text = StringProperty()


class DialogMenu(Box):
	"""Some buttons that make the game do things.

	Set ``options`` to a list of pairs of ``(text, function)`` and the
	menu will be populated with buttons that say ``text`` that call
	``function`` when pressed.

	"""

	options = ListProperty()
	"""List of pairs of (button_text, callable)"""

	def _set_sv_size(self, *_):
		self._sv.width = self.width - self.padding[0] - self.padding[2]
		self._sv.height = self.height - self.padding[1] - self.padding[3]

	def _set_sv_pos(self, *_):
		self._sv.x = self.x + self.padding[0]
		self._sv.y = self.y + self.padding[3]

	@mainthread
	@partial(logwrap, section="DialogMenu")
	def on_options(self, *_):
		binds = App.get_running_app()._bindings
		if not hasattr(self, "_sv"):
			self._sv = ScrollView(size=self.size, pos=self.pos)
			assert not binds["DialogMenu", "size"]
			binds["DialogMenu", "size"].add(
				self.fbind("size", self._set_sv_size)
			)
			assert not binds["DialogMenu", "pos"]
			binds["DialogMenu", "pos"].add(self.fbind("pos", self._set_sv_pos))
			layout = BoxLayout(orientation="vertical")
			self._sv.add_widget(layout)
			self.add_widget(self._sv)
		else:
			layout = self._sv.children[0]
			layout.clear_widgets()
		for txt, part in self.options:
			if not callable(part):
				raise TypeError("Menu options must be callable")
			butn = Button(
				text=txt,
				on_release=part,
				font_name=self.font_name,
				font_size=self.font_size,
				valign="center",
				halign="center",
			)
			if not binds["DialogMenu", "Button", id(butn), "size"]:
				binds["DialogMenu", "Button", id(butn), "size"].add(
					butn.fbind("size", butn.setter("text_size"))
				)
			layout.add_widget(butn)


class Dialog(BoxLayout):
	"""MessageBox with a DialogMenu beneath it.

	Set the properties ``message_kwargs`` and ``menu_kwargs``,
	respectively, to control them -- but you probably want
	to do that by returning a pair of dicts from an action
	in lisien.

	"""

	message_kwargs = DictProperty({})
	menu_kwargs = DictProperty({})

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		app = App.get_running_app()
		binds = app._bindings
		assert not binds["Dialog", id(self), "message_kwargs"]
		binds["Dialog", id(self), "message_kwargs"].add(
			self.fbind("message_kwargs", self._propagate_msg_kwargs)
		)
		assert not binds["Dialog", id(self), "menu_kwargs"]
		binds["Dialog", id(self), "menu_kwargs"].add(
			self.fbind("menu_kwargs", self._propagate_menu_kwargs)
		)
		self._propagate_msg_kwargs()
		self._propagate_menu_kwargs()
		app._unbinders.append(self.unbind_all)

	def unbind_all(self):
		binds = App.get_running_app()._bindings
		for uid in devour(binds["Dialog", id(self), "message_kwargs"]):
			self.unbind_uid("message_kwargs", uid)
		for uid in devour(binds["Dialog", id(self), "menu_kwargs"]):
			self.unbind_uid("menu_kwargs", uid)

	@partial(logwrap, section="Dialog")
	def _propagate_msg_kwargs(self, *_):
		if "msg" not in self.ids:
			Clock.schedule_once(self._propagate_msg_kwargs, 0)
			return
		kw = dict(self.message_kwargs)
		kw.setdefault(
			"background", "atlas://data/images/defaulttheme/textinput"
		)
		for k, v in kw.items():
			setattr(self.ids.msg, k, v)

	@partial(logwrap, section="Dialog")
	def _propagate_menu_kwargs(self, *_):
		if "menu" not in self.ids:
			Clock.schedule_once(self._propagate_menu_kwargs, 0)
			return
		kw = dict(self.menu_kwargs)
		kw.setdefault(
			"background",
			"atlas://data/images/defaulttheme/vkeyboard_background",
		)
		for k, v in kw.items():
			setattr(self.ids.menu, k, v)


class DialogLayout(FloatLayout):
	"""A layout, normally empty, that can generate dialogs

	To make dialogs, set my ``todo`` property to a list. It may contain:

	* Strings, which will be displayed with an "OK" button to dismiss them
	* Lists of pairs of strings and callables, which generate buttons with the
	  string on them that, when clicked, call the callable
	* Lists of pairs of dictionaries, which are interpreted as keyword
	  arguments to :class:`MessageBox` and :class:`DialogMenu`

	In place of a callable you can use the name of a function in my
	``usermod``, a Python module given by name. I'll import it when I need it.

	Needs to be instantiated with a lisien ``engine`` -- probably an
	:class:`EngineProxy`.

	"""

	dialog = ObjectProperty()
	todo = ListProperty()
	usermod = StringProperty("user")
	userpkg = StringProperty(None, allownone=True)

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.dialog = Dialog()
		self._finalize()

	@logwrap(section="DialogLayout")
	def _finalize(self, *_):
		app = App.get_running_app()
		if not hasattr(app, "engine"):
			Clock.schedule_once(self._finalize, 0)
			return
		engine = app.engine
		todo = engine.universal.get("last_result")
		if isinstance(todo, list):
			self.todo = todo
		else:
			self.todo = []
		self.idx = engine.universal.get("last_result_idx", 0)
		engine.universal.connect(self._pull)
		if self.todo:
			self.advance_dialog()

	@logwrap(section="DialogLayout")
	def _pull(self, *_, key, value):
		if key == "last_result":
			self.todo = value if value and isinstance(value, list) else []
		elif key == "last_result_idx":
			self.idx = value if value and isinstance(value, int) else 0

	@logwrap(section="DialogLayout")
	def on_idx(self, *_):
		lidx = self.engine.universal.get("last_result_idx")
		if lidx is not None and lidx != self.idx:
			self.engine.universal["last_result_idx"] = self.idx
		Logger.debug(f"DialogLayout.idx = {self.idx}")

	@mainthread
	@logwrap(section="DialogLayout")
	def advance_dialog(self, after_ok=None, *args):
		"""Try to display the next dialog described in my ``todo``.

		:param after_ok: An optional callable. Will be called after the user clicks
		a dialog option--as well as after any game-specific code for that option
		has run.

		"""
		self.clear_widgets()
		try:
			Logger.debug(f"About to update dialog: {self.todo[0]}")
			self._update_dialog(self.todo.pop(0), after_ok)
		except IndexError:
			if after_ok is not None:
				after_ok()

	@mainthread
	@logwrap(section="DialogLayout")
	def _update_dialog(self, diargs, after_ok, **kwargs):
		if diargs is None:
			Logger.debug("DialogLayout: null dialog")
			return
		if isinstance(diargs, tuple) and diargs[0] == "stop":
			if len(diargs) == 1:
				Logger.debug("DialogLayout: null dialog")
				return
			diargs = diargs[1]
		dia = self.dialog
		# Simple text dialogs just tell the player something and let them click OK
		if isinstance(diargs, str):
			dia.message_kwargs = {"text": diargs}
			dia.menu_kwargs = {
				"options": [("OK", partial(self.ok, cb=after_ok))]
			}
		# List dialogs are for when you need the player to make a choice and don't care much
		# about presentation
		elif isinstance(diargs, list):
			dia.message_kwargs = {"text": "Select from the following:"}
			dia.menu_kwargs = {
				"options": list(
					map(partial(self._munge_menu_option, after_ok), diargs)
				)
			}
		# For real control of the dialog, you need a pair of dicts --
		# the 0th describes the message shown to the player, the 1th
		# describes the menu below
		elif isinstance(diargs, tuple):
			if len(diargs) != 2:
				# TODO more informative error
				raise TypeError("Need a tuple of length 2")
			msgkwargs, mnukwargs = diargs
			if isinstance(msgkwargs, dict):
				dia.message_kwargs = msgkwargs
			elif isinstance(msgkwargs, str):
				dia.message_kwargs["text"] = msgkwargs
			else:
				raise TypeError("Message must be dict or str")
			if isinstance(mnukwargs, dict):
				mnukwargs["options"] = list(
					map(
						partial(self._munge_menu_option, after_ok),
						mnukwargs["options"],
					)
				)
				dia.menu_kwargs = mnukwargs
			elif isinstance(mnukwargs, (list, tuple)):
				dia.menu_kwargs["options"] = list(
					map(partial(self._munge_menu_option, after_ok), mnukwargs)
				)
			else:
				raise TypeError("Menu must be dict or list")
		else:
			raise TypeError(
				"Don't know how to turn {} into a dialog".format(type(diargs))
			)
		if dia.parent != self:
			Logger.debug("DialogLayout: Adding the dialog to the layout")
			self.add_widget(dia)
		else:
			Logger.debug("DialogLayout: Dialog is already in the layout")

	@logwrap(section="DialogLayout")
	def ok(self, *_, cb=None, cb2=None):
		"""Clear dialog widgets, call ``cb`` if provided, and advance the dialog queue

		``cb2`` will be called after advancing the dialog."""
		self.clear_widgets()
		if cb:
			cb()
		self.advance_dialog(after_ok=cb2)

	@logwrap(section="DialogLayout")
	def _lookup_func(self, funcname):
		from importlib import import_module

		if not hasattr(self, "_usermod"):
			self._usermod = import_module(self.usermod, self.userpkg)
		return getattr(self.usermod, funcname)

	@logwrap(section="DialogLayout")
	def _munge_menu_option(self, after_ok, option):
		if not isinstance(option, tuple):
			raise TypeError
		name, func = option
		if func is None:
			return name, partial(self.ok, cb2=after_ok)
		if callable(func):
			return name, partial(self.ok, cb=func, cb2=after_ok)
		if isinstance(func, tuple):
			fun = func[0]
			if isinstance(fun, str):
				fun = self._lookup_func(fun)
			args = func[1]
			if len(func) == 3:
				kwargs = func[2]
				func = partial(fun, *args, **kwargs)
			else:
				func = partial(fun, *args)
		if isinstance(func, str):
			func = self._lookup_func(func)
		return name, partial(self.ok, cb=func, cb2=after_ok)


store_kv(
	__name__,
	"""
<Box>:
	canvas.before:
		Color:
			rgba: self.background_color
		BorderImage:
			border: self.border
			pos: self.pos
			size: self.size
			source: self.background
		Color:
			rgba: 1, 1, 1, 1
<ScrollableLabel>:
	Label:
		size_hint_y: None
		height: self.texture_size[1]
		text_size: self.width, None
		text: root.text
		color: root.color
<MessageBox>:
	ScrollableLabel:
		x: root.x + root.padding[0]
		y: root.y + root.padding[3]
		width: root.width - root.padding[2]
		height: root.height - root.padding[1]
		text: root.text
		color: root.foreground_color
<Dialog>:
	orientation: 'vertical'
	pos_hint: {'x': 0, 'y': 0}
	size_hint: 1, 0.3
	MessageBox:
		id: msg
	DialogMenu:
		id: menu
""",
)
