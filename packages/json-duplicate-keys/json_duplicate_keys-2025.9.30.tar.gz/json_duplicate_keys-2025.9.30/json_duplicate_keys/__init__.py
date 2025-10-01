# -*- coding: utf-8 -*-
try:
	unicode
except NameError:
	unicode = str

from collections import OrderedDict
import json, re, copy

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # Normalize Key name # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# normalize_key(name: str|unicode, dupSign_start: str|unicode, dupSign_end: str|unicode, _isDebug_: bool) -> str|bool
def normalize_key(name, dupSign_start="{{{", dupSign_end="}}}", _isDebug_=False):
	# User input data type validation
	if type(_isDebug_) is not bool: _isDebug_ = False

	if type(name) not in [str, unicode]:
		if _isDebug_: print("\x1b[31m[-] DataTypeError: the KEY name must be str or unicode, not {}\x1b[0m".format(type(name)))
		return False

	if type(dupSign_start) not in [str, unicode]: dupSign_start = "{{{"

	if type(dupSign_end) not in [str, unicode]: dupSign_end = "}}}"

	return re.sub(re.escape(dupSign_start)+'_\\d+_'+re.escape(dupSign_end)+'$', "", name)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # loads # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# loads(Jstr: str|unicode|bytes, dupSign_start: str|unicode, dupSign_end: str|unicode, ordered_dict: bool, skipDuplicated: bool, _isDebug_: bool) -> JSON_DUPLICATE_KEYS|bool
def loads(Jstr, dupSign_start="{{{", dupSign_end="}}}", ordered_dict=False, skipDuplicated=False, _isDebug_=False):
	# User input data type validation
	if type(_isDebug_) is not bool: _isDebug_ = False

	if type(Jstr) not in [str, unicode, bytes]:
		if _isDebug_: print("\x1b[31m[-] DataTypeError: the JSON object must be str, unicode or bytes, not {}\x1b[0m".format(type(Jstr)))
		return False

	if type(dupSign_start) not in [str, unicode]: dupSign_start = "{{{"

	if type(dupSign_end) not in [str, unicode]: dupSign_end = "}}}"

	if type(ordered_dict) is not bool: ordered_dict = False

	if type(skipDuplicated) is not bool: skipDuplicated = False

	def __convert_Jloads_to_Jobj(Jloads, Jobj):
		if type(Jloads) in [dict, OrderedDict]:
			for k in Jloads.keys():
				_key = re.split(dupSign_start_escape_regex+"_\\d+_"+dupSign_end_escape_regex+"$", k)[0]

				if _key not in Jobj.keys():
					if type(Jloads[k]) not in [list, dict, OrderedDict]:
						Jobj[_key] = Jloads[k]
					else:
						if type(Jloads[k]) == list:
							Jobj[_key] = list()
						elif type(Jloads[k]) == dict:
							Jobj[_key] = dict()
						else:
							Jobj[_key] = OrderedDict()

						__convert_Jloads_to_Jobj(Jloads[k], Jobj[_key])
				else:
					countObj = len([i for i in Jobj.keys() if _key==re.split(dupSign_start_escape_regex+"_\\d+_"+dupSign_end_escape_regex+"$", i)[0]])
					if type(Jloads[k]) not in [list, dict, OrderedDict]:
						Jobj[_key+dupSign_start+"_"+str(countObj+1)+"_"+dupSign_end] = Jloads[k]
					else:
						if type(Jloads[k]) == list:
							Jobj[_key+dupSign_start+"_"+str(countObj+1)+"_"+dupSign_end] = list()
						elif type(Jloads[k]) == dict:
							Jobj[_key+dupSign_start+"_"+str(countObj+1)+"_"+dupSign_end] = dict()
						else:
							Jobj[_key+dupSign_start+"_"+str(countObj+1)+"_"+dupSign_end] = OrderedDict()

						__convert_Jloads_to_Jobj(Jloads[k], Jobj[_key+dupSign_start+"_"+str(countObj+1)+"_"+dupSign_end])
		elif type(Jloads) == list:
			for i in range(len(Jloads)):
				if type(Jloads[i]) not in [list, dict, OrderedDict]:
					Jobj.append(Jloads[i])
				else:
					if type(Jloads[i]) == list:
						Jobj.append(list())
					elif type(Jloads[i]) == dict:
						Jobj.append(dict())
					else:
						Jobj.append(OrderedDict())

					__convert_Jloads_to_Jobj(Jloads[i], Jobj[i])

	try:
		Jloads = json.loads(Jstr)
		if ordered_dict: Jloads = json.loads(Jstr, object_pairs_hook=OrderedDict)

		if skipDuplicated:
			if type(Jloads) in [list, dict, OrderedDict]:
				return JSON_DUPLICATE_KEYS(Jloads)
			else:
				if _isDebug_: print("\x1b[31m[-] DataError: Invalid JSON format\x1b[0m")
				return False

		if type(Jloads) in [list, dict, OrderedDict]:
			dupSign_start_escape = "".join(["\\\\u"+hex(ord(c))[2:].zfill(4) for c in dupSign_start])
			dupSign_start_escape_regex = re.escape(dupSign_start)

			dupSign_end_escape = "".join(["\\\\u"+hex(ord(c))[2:].zfill(4) for c in dupSign_end])
			dupSign_end_escape_regex = re.escape(dupSign_end)


			if type(Jstr) == bytes:
				Jstr = re.sub(r'\\\\'.encode(), '\x00\x01'.encode(), Jstr)
				Jstr = re.sub(r'\\"'.encode(), '\x02\x03'.encode(), Jstr)
				Jstr = re.sub(r'"([^"]*)"[\s\t\r\n]*([,\]}])'.encode(), '\x04\x05\\1\x04\x05\\2'.encode(), Jstr)


				Jstr = re.sub(r'"([^"]+)"[\s\t\r\n]*:'.encode(), (r'"\1'+dupSign_start_escape+'_dupSign_'+dupSign_end_escape+'":').encode(), Jstr)

				Jstr = re.sub(r'""[\s\t\r\n]*:'.encode(), ('"'+dupSign_start_escape+'_dupSign_'+dupSign_end_escape+'":').encode(), Jstr)

				i = 0
				while re.search((dupSign_start_escape+'_dupSign_'+dupSign_end_escape+r'"[\s\t\r\n]*:').encode(), Jstr):
					Jstr = re.sub((dupSign_start_escape+'_dupSign_'+dupSign_end_escape+r'"[\s\t\r\n]*:').encode(), (dupSign_start_escape+"_"+str(i)+"_"+dupSign_end_escape+'":').encode(), Jstr, 1)
					i += 1

				Jstr = re.sub('\x00\x01'.encode(), r'\\\\'.encode(), Jstr)
				Jstr = re.sub('\x02\x03'.encode(), r'\\"'.encode(), Jstr)
				Jstr = re.sub('\x04\x05'.encode(), r'"'.encode(), Jstr)
			else:
				Jstr = re.sub(r'\\\\', '\x00\x01', Jstr)
				Jstr = re.sub(r'\\"', '\x02\x03', Jstr)
				Jstr = re.sub(r'"([^"]*)"[\s\t\r\n]*([,\]}])', '\x04\x05\\1\x04\x05\\2', Jstr)

				Jstr = re.sub(r'"([^"]+)"[\s\t\r\n]*:', r'"\1'+dupSign_start_escape+'_dupSign_'+dupSign_end_escape+'":', Jstr)

				Jstr = re.sub(r'""[\s\t\r\n]*:', '"'+dupSign_start_escape+'_dupSign_'+dupSign_end_escape+'":', Jstr)

				i = 0
				while re.search(dupSign_start_escape+'_dupSign_'+dupSign_end_escape+r'"[\s\t\r\n]*:', Jstr):
					Jstr = re.sub(dupSign_start_escape+'_dupSign_'+dupSign_end_escape+r'"[\s\t\r\n]*:', dupSign_start_escape+"_"+str(i)+"_"+dupSign_end_escape+'":', Jstr, 1)
					i += 1

				Jstr = re.sub('\x00\x01', r'\\\\', Jstr)
				Jstr = re.sub('\x02\x03', r'\\"', Jstr)
				Jstr = re.sub('\x04\x05', r'"', Jstr)

			Jloads = json.loads(Jstr)
			if ordered_dict:
				Jloads = json.loads(Jstr, object_pairs_hook=OrderedDict)

			if type(Jloads) == list:
				Jobj = list()
			elif type(Jloads) == dict:
				Jobj = dict()
			else:
				Jobj = OrderedDict()

			__convert_Jloads_to_Jobj(Jloads, Jobj)

			return JSON_DUPLICATE_KEYS(Jobj)
		else:
			if _isDebug_: print("\x1b[31m[-] DataError: Invalid JSON format\x1b[0m")
			return False
	except Exception as e:
		if _isDebug_: print("\x1b[31m[-] ExceptionError: {}\x1b[0m".format(e))
		return False
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # load # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# load(Jfilepath: str|unicode, dupSign_start: str|unicode, dupSign_end: str|unicode, ordered_dict: bool, skipDuplicated: bool, _isDebug_: bool) -> JSON_DUPLICATE_KEYS|bool
def load(Jfilepath, dupSign_start="{{{", dupSign_end="}}}", ordered_dict=False, skipDuplicated=False, _isDebug_=False):
	# User input data type validation
	if type(_isDebug_) is not bool: _isDebug_ = False

	if type(Jfilepath) not in [str, unicode]:
		if _isDebug_: print("\x1b[31m[-] DataTypeError: the JSON file path must be str or unicode, not {}\x1b[0m".format(type(Jfilepath)))
		return False

	if type(dupSign_start) not in [str, unicode]: dupSign_start = "{{{"

	if type(dupSign_end) not in [str, unicode]: dupSign_end = "}}}"

	if type(ordered_dict) is not bool: ordered_dict = False

	if type(skipDuplicated) is not bool: skipDuplicated = False

	try:
		try:
			with open(Jfilepath) as Jfile: Jstr = Jfile.read()
		except Exception as e:
			with open(Jfilepath, "rb") as Jfile: Jstr = Jfile.read()

		return loads(Jstr, dupSign_start=dupSign_start, dupSign_end=dupSign_end, ordered_dict=ordered_dict, skipDuplicated=skipDuplicated, _isDebug_=_isDebug_)
	except Exception as e:
		if _isDebug_: print("\x1b[31m[-] ExceptionError: {}\x1b[0m".format(e))
		return False
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # JSON_DUPLICATE_KEYS # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class JSON_DUPLICATE_KEYS:
	# __init__(Jobj: dict|list|OrderedDict) -> None
	def __init__(self, Jobj):
		self.__Jobj = dict()
		if type(Jobj) in [dict, OrderedDict, list]:
			self.__Jobj = Jobj

	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # getObject # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# getObject() -> dict|list|OrderedDict
	def getObject(self):
		return self.__Jobj
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # get # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# get(name: str|unicode, case_insensitive: bool, separator: str||unicode, parse_index: str||unicode, _isDebug_: bool) -> dict{name: str|unicode, value: any}
	def get(self, name, case_insensitive=False, separator="||", parse_index="$", _isDebug_=False):
		# User input data type validation
		if type(_isDebug_) is not bool: _isDebug_ = False

		if type(name) not in [str, unicode]:
			if _isDebug_: print("\x1b[31m[-] DataTypeError: the KEY name must be str or unicode, not {}\x1b[0m".format(type(name)))
			return {"name":name, "value":"JSON_DUPLICATE_KEYS_ERROR"}

		if type(case_insensitive) is not bool: case_insensitive = False

		if type(separator) not in [str, unicode]: separator = "||"

		if type(parse_index) not in [str, unicode]: parse_index = "$"

		if type(self.getObject()) not in [list, dict, OrderedDict]:
			if _isDebug_: print("\x1b[31m[-] DataTypeError: the JSON object must be list, dict or OrderedDict, not {}\x1b[0m".format(type(self.getObject())))
			return {"name":name, "value":"JSON_DUPLICATE_KEYS_ERROR"}

		if re.search(re.escape(separator)+"$", name):
			if _isDebug_: print("\x1b[31m[-] KeyNameInvalidError: \x1b[0m"+name)
			return {"name":name, "value":"JSON_DUPLICATE_KEYS_ERROR"}

		Jobj = JSON_DUPLICATE_KEYS(self.__Jobj)
		Jobj.flatten()
		Jname = []
		Jval = self.__Jobj
		name_split = name.split(separator)

		if type(Jobj.getObject()) in [dict, OrderedDict]:
			for k in Jobj.getObject().keys():
				if len(k.split(separator)) >= len(name_split):
					if case_insensitive:
						if separator.join(k.split(separator)[:len(name_split)]).lower() == name.lower():
							Jname = k.split(separator)[:len(name_split)]
							break
					else:
						if separator.join(k.split(separator)[:len(name_split)]) == name:
							Jname = name_split
							break

		if len(Jname) > 0:
			for k in Jname:
				if re.search("^"+re.escape(parse_index)+"\\d+"+re.escape(parse_index)+"$", k):
					Jval = Jval[int(k.split(parse_index)[1])]
				else:
					Jval = Jval[k]
			return {"name":separator.join(Jname), "value":Jval}
		else:
			if _isDebug_: print("\x1b[31m[-] KeyNotFoundError: \x1b[0m"+name)
			return {"name":name, "value":"JSON_DUPLICATE_KEYS_ERROR"}
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # set # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# set(name: str|unicode, value: any, case_insensitive: bool, separator: str||unicode, parse_index: str||unicode, dupSign_start: str||unicode, dupSign_end: str||unicode, ordered_dict: bool, _isDebug_: bool) -> bool
	def set(self, name, value, case_insensitive=False, separator="||", parse_index="$", dupSign_start="{{{", dupSign_end="}}}", ordered_dict=False, _isDebug_=False):
		# User input data type validation
		if type(_isDebug_) is not bool: _isDebug_ = False

		if type(name) not in [str, unicode]:
			if _isDebug_:  print("\x1b[31m[-] DataTypeError: the KEY name must be str or unicode, not {}\x1b[0m".format(type(name)))
			return False

		if type(case_insensitive) is not bool: case_insensitive = False

		if type(separator) not in [str, unicode]: separator = "||"

		if type(parse_index) not in [str, unicode]: parse_index = "$"

		if type(dupSign_start) not in [str, unicode]: dupSign_start = "{{{"

		if type(dupSign_end) not in [str, unicode]:  dupSign_end = "}}}"

		if type(ordered_dict) is not bool: ordered_dict = False

		if type(self.getObject()) not in [list, dict, OrderedDict]:
			if _isDebug_: print("\x1b[31m[-] DataTypeError: the JSON object must be list, dict or OrderedDict, not {}\x1b[0m".format(type(self.getObject())))
			return False

		if re.search(re.escape(separator)+"$", name):
			if _isDebug_: print("\x1b[31m[-] KeyNameInvalidError: \x1b[0m"+name)
			return False

		if re.search("^"+re.escape(parse_index)+"\\d+"+re.escape(parse_index)+"$", name.split(separator)[-1]):
			if _isDebug_: print("\x1b[31m[-] KeyNameInvalidError: The key name does not end with the list index\x1b[0m")
			return False

		Jget = self.get(name, case_insensitive=case_insensitive, separator=separator, parse_index=parse_index)

		def traverse_and_set(obj, keys, val):
			cur = obj
			for i, k in enumerate(keys):
				is_index = re.match("^"+re.escape(parse_index)+"(\\d+)"+re.escape(parse_index)+"$", k)
				if i == len(keys) - 1:
					if is_index:
						cur[int(is_index.group(1))] = val
					else:
						cur[k] = val
					return True
				else:
					if is_index:
						cur = cur[int(is_index.group(1))]
					else:
						cur = cur[k]
			return False

		# Case 1: key exists => add dupSign
		if Jget["value"] != "JSON_DUPLICATE_KEYS_ERROR":
			index = 2
			while True:
				dup_name = Jget["name"]+dupSign_start+"_"+str(index)+"_"+dupSign_end
				if self.get(dup_name, case_insensitive=case_insensitive, separator=separator, parse_index=parse_index)["value"] == "JSON_DUPLICATE_KEYS_ERROR":
					break
				index += 1
			keys = dup_name.split(separator)
			return traverse_and_set(self.getObject(), keys, value)

		# Case 2: key not exists => set directly
		else:
			if len(name.split(separator)) == 1:
				if type(self.getObject()) in [dict, OrderedDict]:
					self.getObject()[name] = value
					return True
				else:
					if _isDebug_:  print("\x1b[31m[-] DataTypeError: Cannot set name and value for a list object\x1b[0m")
					return False
			else:
				parent_name = separator.join(name.split(separator)[:-1])
				Jget_parent = self.get(parent_name, case_insensitive=case_insensitive, separator=separator, parse_index=parse_index)
				if Jget_parent["value"] != "JSON_DUPLICATE_KEYS_ERROR":
					if type(Jget_parent["value"]) in [dict, OrderedDict]:
						keys = Jget_parent["name"].split(separator)+[name.split(separator)[-1]]
						return traverse_and_set(self.getObject(), keys, value)
					else:
						if _isDebug_: 
							print("\x1b[31m[-] KeyNameInvalidError: \x1b[0m"+name)
						return False
				else:
					if _isDebug_: 
						print("\x1b[31m[-] KeyNameNotExistError: {}\x1b[0m".format(parent_name))
					return False
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # insert # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# insert(name: str|unicode|None, value: any, position: int|None, case_insensitive: bool, separator: str||unicode, parse_index: str||unicode, dupSign_start: str||unicode, dupSign_end: str||unicode, _isDebug_: bool) -> bool
	def insert(self, name, value, position=None, case_insensitive=False, separator="||", parse_index="$", dupSign_start="{{{", dupSign_end="}}}", _isDebug_=False):
		# User input data type validation
		if type(_isDebug_) is not bool: _isDebug_ = False

		if type(name) not in [str, unicode, type(None)]:
			if _isDebug_: print("\x1b[31m[-] DataTypeError: the KEY name must be str, unicode or None, not {}\x1b[0m".format(type(name)))
			return False

		if type(position) is not int: position = None

		if type(case_insensitive) is not bool: case_insensitive = False

		if type(separator) not in [str, unicode]: separator = "||"

		if type(parse_index) not in [str, unicode]: parse_index = "$"

		if type(dupSign_start) not in [str, unicode]: dupSign_start = "{{{"

		if type(dupSign_end) not in [str, unicode]: dupSign_end = "}}}"

		if type(self.getObject()) not in [list, dict, OrderedDict]:
			if _isDebug_: print("\x1b[31m[-] DataTypeError: the JSON object must be list, dict or OrderedDict, not {}\x1b[0m".format(type(self.getObject())))
			return False
		
		if (name is None or name == "") and type(self.getObject()) == list:
			if position is None: position = len(self.getObject())

			self.getObject().insert(position, value)
			return True

		if re.search(re.escape(separator)+"$", name):
			if _isDebug_: print("\x1b[31m[-] KeyNameInvalidError: \x1b[0m"+name)
			return False

		Jget = self.get(name, case_insensitive=case_insensitive, separator=separator, parse_index=parse_index, _isDebug_=_isDebug_)

		if Jget["value"] != "JSON_DUPLICATE_KEYS_ERROR":
			if type(Jget["value"]) == list:
				if position == None: position = len(Jget["value"])

				Jget["value"].insert(position, value)

				return self.update(Jget["name"], Jget["value"], separator=separator, parse_index=parse_index, dupSign_start=dupSign_start, dupSign_end=dupSign_end, _isDebug_=_isDebug_)
			else:
				if _isDebug_: print("\x1b[31m[-] DataTypeError: The data type of {} must be list, not {}\x1b[0m".format(Jget["name"], type(Jget["value"])))
		return False


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # update # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# update(name: str|unicode, value: any, case_insensitive: bool, allow_new_key: bool, separator: str||unicode, parse_index: str||unicode, dupSign_start: str||unicode, dupSign_end: str||unicode, ordered_dict: bool, _isDebug_: bool) -> bool
	def update(self, name, value, case_insensitive=False, allow_new_key=False, separator="||", parse_index="$", dupSign_start="{{{", dupSign_end="}}}", ordered_dict=False, _isDebug_=False):
		# User input data type validation
		if type(_isDebug_) is not bool: _isDebug_ = False

		if type(name) not in [str, unicode]:
			if _isDebug_: print("\x1b[31m[-] DataTypeError: the KEY name must be str or unicode, not {}\x1b[0m".format(type(name)))
			return False
		
		if type(case_insensitive) is not bool: case_insensitive = False

		if type(allow_new_key) is not bool: allow_new_key = False

		if type(separator) not in [str, unicode]: separator = "||"

		if type(parse_index) not in [str, unicode]: parse_index = "$"

		if type(dupSign_start) not in [str, unicode]: dupSign_start = "{{{"

		if type(dupSign_end) not in [str, unicode]: dupSign_end = "}}}"

		if type(ordered_dict) is not bool: ordered_dict = False

		_debug_ = _isDebug_
		if allow_new_key: _debug_ = False

		current = self.get(name, case_insensitive=case_insensitive, separator=separator, parse_index=parse_index, _isDebug_=_debug_)
		if current["value"] != "JSON_DUPLICATE_KEYS_ERROR":
			Jname = current["name"]
			try:
				parts = Jname.split(separator)
				target = self.getObject()

				for i, k in enumerate(parts):
					if re.search("^"+re.escape(parse_index)+"\\d+"+re.escape(parse_index)+"$", k):
						idx = int(k.strip(parse_index))
						if i < len(parts) - 1:
							target = target[idx]
						else:
							target[idx] = value
					else:
						if i < len(parts) - 1:
							target = target[k]
						else:
							target[k] = value
				return True
			except Exception as e:
				if _isDebug_: print("\x1b[31m[-] ExceptionError: {}\x1b[0m".format(e))
		elif allow_new_key:
			return self.set(name, value, case_insensitive=case_insensitive, separator=separator, parse_index=parse_index, dupSign_start=dupSign_start, dupSign_end=dupSign_end, ordered_dict=ordered_dict, _isDebug_=_isDebug_)
		return False
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # #  delete   # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# delete(name: str|unicode, case_insensitive: bool, separator: str||unicode, parse_index: str||unicode, _isDebug_: bool) -> bool
	def delete(self, name, case_insensitive=False, separator="||", parse_index="$", _isDebug_=False):
		# User input data type validation
		if type(_isDebug_) is not bool: _isDebug_ = False

		if type(name) not in [str, unicode]:
			if _isDebug_: print("\x1b[31m[-] DataTypeError: the KEY name must be str or unicode, not {}\x1b[0m".format(type(name)))
			return False

		if type(case_insensitive) is not bool: case_insensitive = False

		if type(separator) not in [str, unicode]: separator = "||"

		if type(parse_index) not in [str, unicode]: parse_index = "$"

		Jget = self.get(name, case_insensitive=case_insensitive, separator=separator, parse_index=parse_index, _isDebug_=_isDebug_)
		if Jget["value"] == "JSON_DUPLICATE_KEYS_ERROR":
			return False

		Jname = Jget["name"]
		keys = Jname.split(separator)

		try:
			cur = self.getObject()
			for i, k in enumerate(keys):
				is_index = re.match("^"+re.escape(parse_index)+"(\\d+)"+re.escape(parse_index)+"$", k)
				if i == len(keys) - 1:
					# last key => delete
					if is_index:
						del cur[int(is_index.group(1))]
					else:
						del cur[k]
					return True
				else:
					# not last key => traverse
					if is_index:
						cur = cur[int(is_index.group(1))]
					else:
						cur = cur[k]
		except Exception as e:
			if _isDebug_: print("\x1b[31m[-] ExceptionError: {}\x1b[0m".format(e))
		return False
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # filter_keys  # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	def filter_keys(self, name, separator="||", parse_index="$", ordered_dict=False):
		JDKSObject = copy.deepcopy(self)
		JDKSObject.flatten(separator=separator, parse_index=parse_index, ordered_dict=ordered_dict)
		newJDKSObject = loads("{}", ordered_dict=ordered_dict)

		for k, v in JDKSObject.getObject().items():
			if type(k) == str and type(name) == str:
				if re.search(name, k):
					newJDKSObject.set(k, v, separator=u"§§"+separator+u"§§", parse_index=u"§§"+parse_index+u"§§", ordered_dict=ordered_dict)
			else:
				if name == k:
					newJDKSObject.set(k, v, separator=u"§§"+separator+u"§§", parse_index=u"§§"+parse_index+u"§§", ordered_dict=ordered_dict)

		return newJDKSObject
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # filter_values  # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	def filter_values(self, value, separator="||", parse_index="$", ordered_dict=False):
		JDKSObject = copy.deepcopy(self)
		JDKSObject.flatten(separator=separator, parse_index=parse_index, ordered_dict=ordered_dict)
		newJDKSObject = loads("{}", ordered_dict=ordered_dict)

		for k, v in JDKSObject.getObject().items():
			if type(v) == str and type(value) == str:
				if re.search(value, v):
					newJDKSObject.set(k, v, separator=u"§§"+separator+u"§§", parse_index=u"§§"+parse_index+u"§§", ordered_dict=ordered_dict)
			else:
				if value == v:
					newJDKSObject.set(k, v, separator=u"§§"+separator+u"§§", parse_index=u"§§"+parse_index+u"§§", ordered_dict=ordered_dict)

		return newJDKSObject
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	 # # # # # # # # # # # # # # dumps # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	def dumps(self, dupSign_start="{{{", dupSign_end="}}}", _isDebug_=False, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False):
		# User input data type validation
		if type(_isDebug_) != bool: _isDebug_ = False

		if type(dupSign_start) not in [str, unicode]: dupSign_start = "{{{"

		if type(dupSign_end) not in [str, unicode]: dupSign_end = "}}}"

		if type(self.getObject()) not in [list, dict, OrderedDict]:
			if _isDebug_: print("\x1b[31m[-] DataTypeError: the JSON object must be list, dict or OrderedDict, not {}\x1b[0m".format(type(self.getObject())))
			return "JSON_DUPLICATE_KEYS_ERROR"

		dupSign_start_escape_regex = re.escape(json.dumps({dupSign_start:""})[2:-6])

		dupSign_end_escape_regex = re.escape(json.dumps({dupSign_end:""})[2:-6])

		return re.sub(dupSign_start_escape_regex+'_\\d+_'+dupSign_end_escape_regex+'":', '":', json.dumps(self.getObject(), skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular, allow_nan=allow_nan, cls=cls, indent=indent, separators=separators, default=default, sort_keys=sort_keys))
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	 # # # # # # # # # # # # # # dump  # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	def dump(self, Jfilepath, dupSign_start="{{{", dupSign_end="}}}", _isDebug_=False, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False):
		Jstr = self.dumps(dupSign_start=dupSign_start, dupSign_end=dupSign_end, _isDebug_=_isDebug_, skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular, allow_nan=allow_nan, cls=cls, indent=indent, separators=separators, default=default, sort_keys=sort_keys)

		try:
			Jfile = open(Jfilepath, "wb")
			Jfile.write(Jstr.encode("utf-8"))
			Jfile.close()
		except Exception as e:
			if _isDebug_: print("\x1b[31m[-] ExceptionError: {}\x1b[0m".format(e))
			return False
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	 # # # # # # # # # # # # # flatten # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# flatten(separator: str||unicode, parse_index: str||unicode, ordered_dict: bool, _isDebug_: bool) -> bool
	def flatten(self, separator="||", parse_index="$", ordered_dict=False, _isDebug_=False):
		# User input data type validation
		if type(_isDebug_) is not bool: _isDebug_ = False

		if type(separator) not in [str, unicode]: separator = "||"

		if type(parse_index) not in [str, unicode]: parse_index = "$"

		if type(ordered_dict) is not bool: ordered_dict = False

		if type(self.getObject()) not in [list, dict, OrderedDict]:
			if _isDebug_: print("\x1b[31m[-] DataTypeError: the JSON object must be list, dict or OrderedDict, not {}\x1b[0m".format(type(self.getObject())))
			return False

		if len(self.getObject()) > 0:
			try:
				Jflat = dict()
				if ordered_dict:
					Jflat = OrderedDict()

				def __convert_Jobj_to_Jflat(Jobj, key=None):
					if type(Jobj) in [dict, OrderedDict]:
						if len(Jobj) == 0:
							Jflat[key] = dict()
							if ordered_dict:
								Jflat[key] = OrderedDict()
						else:
							for k,v in Jobj.items():
								_Jobj = v
								_key = key+separator+k if key != None else k

								__convert_Jobj_to_Jflat(_Jobj, _key)
					elif type(Jobj) == list:
						if len(Jobj) == 0:
							Jflat[key] = list()
						else:
							for i,v in enumerate(Jobj):
								_Jobj = v
								_key = key+separator+parse_index+str(i)+parse_index if key != None else parse_index+str(i)+parse_index

								__convert_Jobj_to_Jflat(_Jobj, _key)
					else:
						Jflat[key] = Jobj

				__convert_Jobj_to_Jflat(self.getObject())

				self.__Jobj = Jflat
				return True
			except Exception as e:
				if _isDebug_: print("\x1b[31m[-] ExceptionError: {}\x1b[0m".format(e))
				return False
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	 # # # # # # # # # # # # # unflatten # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# unflatten(separator: str||unicode, parse_index: str||unicode, ordered_dict: bool, _isDebug_: bool) -> bool
	def unflatten(self, separator="||", parse_index="$", ordered_dict=False, _isDebug_=False):
		# User input data type validation
		if type(_isDebug_) is not bool: _isDebug_ = False

		if type(separator) not in [str, unicode]: separator = "||"

		if type(parse_index) not in [str, unicode]: parse_index = "$"

		if type(ordered_dict) is not bool: ordered_dict = False

		if type(self.getObject()) not in [dict, OrderedDict]:
			if _isDebug_: print("\x1b[31m[-] DataTypeError: the JSON object must be dict or OrderedDict, not {}\x1b[0m".format(type(self.getObject())))
			return False

		if len(self.getObject()) > 0:
			try:
				Jobj = list() if len([k for k in self.__Jobj.keys() if re.compile("^"+re.escape(parse_index)+"\\d+"+re.escape(parse_index)+"$").match(str(k).split(separator)[0])]) == len(self.__Jobj.keys()) else OrderedDict() if ordered_dict else dict()

				for k, v in self.__Jobj.items():
					Jtmp = Jobj
					Jkeys = k.split(separator)

					for count, (Jkey, next_Jkeys) in enumerate(zip(Jkeys, Jkeys[1:] + [v]), 1):
						v = next_Jkeys if count == len(Jkeys) else list() if re.compile("^"+re.escape(parse_index)+"\\d+"+re.escape(parse_index)+"$").match(next_Jkeys) else OrderedDict() if ordered_dict else dict()

						if type(Jtmp) == list:
							Jkey = int(re.compile(re.escape(parse_index)+"(\\d+)"+re.escape(parse_index)).match(Jkey).group(1))

							while Jkey >= len(Jtmp):
								Jtmp.append(v)

						elif Jkey not in Jtmp:
							Jtmp[Jkey] = v

						Jtmp = Jtmp[Jkey]

				self.__Jobj = Jobj
				return True
			except Exception as e:
				if _isDebug_: print("\x1b[31m[-] ExceptionError: {}\x1b[0m".format(e))
				return False
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #