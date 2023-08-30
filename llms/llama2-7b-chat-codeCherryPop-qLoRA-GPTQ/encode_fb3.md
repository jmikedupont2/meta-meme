python console3.py
Binding gptq loaded successfully.
/mnt/data1/2023/08/02/lollms/examples/chat_forever/.venv/lib/python3.10/site-packages/torch/cuda/__init__.py:546: UserWarning: Can't initialize NVML
  warnings.warn("Can't initialize NVML")
skip module injection for FusedLlamaMLPForQuantizedModel not support integrate without triton yet.
Context lenghth set to 4096
Couldn't load personality. Please verify your configuration file at /home/mdupont/ggml/configs or use the next menu to select a valid personality
Binding returned this exception : The provided path does not exist.
Traceback (most recent call last):
  File "/mnt/data1/2023/08/02/lollms/lollms/app.py", line 124, in mount_personality
    personality = PersonalityBuilder(self.lollms_paths, self.config, self.model, callback=callback).build_personality(id)
  File "/mnt/data1/2023/08/02/lollms/lollms/personality.py", line 1360, in build_personality
    self.personality = AIPersonality(
  File "/mnt/data1/2023/08/02/lollms/lollms/personality.py", line 147, in __init__
    raise ValueError("The provided path does not exist.")
ValueError: The provided path does not exist.

personalities_zoo_path: /home/mdupont/ggml/personalities_zoo
Personalities:['english/coding/pytorch']
Active personality id:0
Traceback (most recent call last):
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/console3.py", line 242, in <module>
    cv = MyConversation(Path("config.yaml"))
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/console3.py", line 129, in __init__
    super().__init__(cfg, show_welcome_message=False)
  File "/mnt/data1/2023/08/02/lollms/lollms/apps/console/__init__.py", line 39, in __init__
    super().__init__("lollms-console",config, lollms_paths)
  File "/mnt/data1/2023/08/02/lollms/lollms/app.py", line 85, in __init__
    self.mount_personalities()
  File "/mnt/data1/2023/08/02/lollms/lollms/app.py", line 155, in mount_personalities
    self.personality = self.mounted_personalities[self.config.active_personality_id]
IndexError: list index out of range
(.venv) mdupont@mdupont-G470:~/experiments/chat_forever$ python console3.py
Binding gptq loaded successfully.
/mnt/data1/2023/08/02/lollms/examples/chat_forever/.venv/lib/python3.10/site-packages/torch/cuda/__init__.py:546: UserWarning: Can't initialize NVML
  warnings.warn("Can't initialize NVML")
skip module injection for FusedLlamaMLPForQuantizedModel not support integrate without triton yet.
Context lenghth set to 4096
Couldn't load personality. Please verify your configuration file at /home/mdupont/ggml/configs or use the next menu to select a valid personality
Binding returned this exception : The provided path does not exist.
Traceback (most recent call last):
  File "/mnt/data1/2023/08/02/lollms/lollms/app.py", line 124, in mount_personality
    personality = PersonalityBuilder(self.lollms_paths, self.config, self.model, callback=callback).build_personality(id)
  File "/mnt/data1/2023/08/02/lollms/lollms/personality.py", line 1360, in build_personality
    self.personality = AIPersonality(
  File "/mnt/data1/2023/08/02/lollms/lollms/personality.py", line 147, in __init__
    raise ValueError("The provided path does not exist.")
ValueError: The provided path does not exist.

personalities_zoo_path: /home/mdupont/ggml/personalities_zoo
Personalities:['english/coding/pytorch']
Active personality id:0
Traceback (most recent call last):
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/console3.py", line 242, in <module>
    cv = MyConversation(Path("config.yaml"))
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/console3.py", line 129, in __init__
    super().__init__(cfg, show_welcome_message=False)
  File "/mnt/data1/2023/08/02/lollms/lollms/apps/console/__init__.py", line 39, in __init__
    super().__init__("lollms-console",config, lollms_paths)
  File "/mnt/data1/2023/08/02/lollms/lollms/app.py", line 85, in __init__
    self.mount_personalities()
  File "/mnt/data1/2023/08/02/lollms/lollms/app.py", line 155, in mount_personalities
    self.personality = self.mounted_personalities[self.config.active_personality_id]
IndexError: list index out of range
(.venv) mdupont@mdupont-G470:~/experiments/chat_forever$ python console3.py
Binding gptq loaded successfully.
/mnt/data1/2023/08/02/lollms/examples/chat_forever/.venv/lib/python3.10/site-packages/torch/cuda/__init__.py:546: UserWarning: Can't initialize NVML
  warnings.warn("Can't initialize NVML")
skip module injection for FusedLlamaMLPForQuantizedModel not support integrate without triton yet.
Context lenghth set to 4096
Couldn't load personality. Please verify your configuration file at /home/mdupont/ggml/configs or use the next menu to select a valid personality
Binding returned this exception : while scanning for the next token
found character '\t' that cannot start any token
  in "/home/mdupont/ggml/personalities_zoo/english/generic/pytorch/config.yaml", line 48, column 1
Traceback (most recent call last):
  File "/mnt/data1/2023/08/02/lollms/lollms/app.py", line 124, in mount_personality
    personality = PersonalityBuilder(self.lollms_paths, self.config, self.model, callback=callback).build_personality(id)
  File "/mnt/data1/2023/08/02/lollms/lollms/personality.py", line 1360, in build_personality
    self.personality = AIPersonality(
  File "/mnt/data1/2023/08/02/lollms/lollms/personality.py", line 156, in __init__
    self.load_personality(personality_package_path)
  File "/mnt/data1/2023/08/02/lollms/lollms/personality.py", line 189, in load_personality
    config = yaml.safe_load(f)
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/.venv/lib/python3.10/site-packages/yaml/__init__.py", line 125, in safe_load
    return load(stream, SafeLoader)
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/.venv/lib/python3.10/site-packages/yaml/__init__.py", line 81, in load
    return loader.get_single_data()
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/.venv/lib/python3.10/site-packages/yaml/constructor.py", line 49, in get_single_data
    node = self.get_single_node()
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/.venv/lib/python3.10/site-packages/yaml/composer.py", line 36, in get_single_node
    document = self.compose_document()
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/.venv/lib/python3.10/site-packages/yaml/composer.py", line 55, in compose_document
    node = self.compose_node(None, None)
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/.venv/lib/python3.10/site-packages/yaml/composer.py", line 84, in compose_node
    node = self.compose_mapping_node(anchor)
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/.venv/lib/python3.10/site-packages/yaml/composer.py", line 133, in compose_mapping_node
    item_value = self.compose_node(node, item_key)
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/.venv/lib/python3.10/site-packages/yaml/composer.py", line 82, in compose_node
    node = self.compose_sequence_node(anchor)
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/.venv/lib/python3.10/site-packages/yaml/composer.py", line 110, in compose_sequence_node
    while not self.check_event(SequenceEndEvent):
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/.venv/lib/python3.10/site-packages/yaml/parser.py", line 98, in check_event
    self.current_event = self.state()
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/.venv/lib/python3.10/site-packages/yaml/parser.py", line 486, in parse_flow_sequence_entry
    if self.check_token(KeyToken):
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/.venv/lib/python3.10/site-packages/yaml/scanner.py", line 116, in check_token
    self.fetch_more_tokens()
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/.venv/lib/python3.10/site-packages/yaml/scanner.py", line 258, in fetch_more_tokens
    raise ScannerError("while scanning for the next token", None,
yaml.scanner.ScannerError: while scanning for the next token
found character '\t' that cannot start any token
  in "/home/mdupont/ggml/personalities_zoo/english/generic/pytorch/config.yaml", line 48, column 1

personalities_zoo_path: /home/mdupont/ggml/personalities_zoo
Personalities:['english/generic/pytorch']
Active personality id:0
Traceback (most recent call last):
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/console3.py", line 242, in <module>
    cv = MyConversation(Path("config.yaml"))
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/console3.py", line 129, in __init__
    super().__init__(cfg, show_welcome_message=False)
  File "/mnt/data1/2023/08/02/lollms/lollms/apps/console/__init__.py", line 39, in __init__
    super().__init__("lollms-console",config, lollms_paths)
  File "/mnt/data1/2023/08/02/lollms/lollms/app.py", line 85, in __init__
    self.mount_personalities()
  File "/mnt/data1/2023/08/02/lollms/lollms/app.py", line 155, in mount_personalities
    self.personality = self.mounted_personalities[self.config.active_personality_id]
IndexError: list index out of range
(.venv) mdupont@mdupont-G470:~/experiments/chat_forever$ 