
(.venv) mdupont@mdupont-G470:~/experiments/chat_forever$ python console3.py
Binding gptq loaded successfully.
/mnt/data1/2023/08/02/lollms/examples/chat_forever/.venv/lib/python3.10/site-packages/torch/cuda/__init__.py:546: UserWarning: Can't initialize NVML
  warnings.warn("Can't initialize NVML")
Couldn't load model. Please verify your configuration file at /home/mdupont/ggml/configs or use the next menu to select a valid model
Binding returned this exception : CUDA out of memory. Tried to allocate 20.00 MiB (GPU 0; 11.73 GiB total capacity; 3.05 GiB already allocated; 4.00 MiB free; 3.24 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF
Traceback (most recent call last):
  File "/mnt/data1/2023/08/02/lollms/lollms/app.py", line 107, in load_model
    model = ModelBuilder(self.binding).get_model()
  File "/mnt/data1/2023/08/02/lollms/lollms/binding.py", line 309, in __init__
    self.build_model()
  File "/mnt/data1/2023/08/02/lollms/lollms/binding.py", line 312, in build_model
    self.model = self.binding.build_model()
  File "/mnt/data1/2023/08/02/ggml/bindings_zoo/gptq/__init__.py", line 169, in build_model
    self.model = AutoGPTQForCausalLM.from_quantized(model_path, **params)
  File "/mnt/data1/2023/08/02/lollms/vendor/AutoGPTQ/auto_gptq/modeling/auto.py", line 108, in from_quantized
    return quant_func(
  File "/mnt/data1/2023/08/02/lollms/vendor/AutoGPTQ/auto_gptq/modeling/_base.py", line 890, in from_quantized
    accelerate.utils.modeling.load_checkpoint_in_model(
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/.venv/lib/python3.10/site-packages/accelerate/utils/modeling.py", line 1335, in load_checkpoint_in_model
    checkpoint = load_state_dict(checkpoint_file, device_map=device_map)
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/.venv/lib/python3.10/site-packages/accelerate/utils/modeling.py", line 1164, in load_state_dict
    return safe_load_file(checkpoint_file, device=list(device_map.values())[0])
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/.venv/lib/python3.10/site-packages/safetensors/torch.py", line 310, in load_file
    result[k] = f.get_tensor(k)
torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 20.00 MiB (GPU 0; 11.73 GiB total capacity; 3.05 GiB already allocated; 4.00 MiB free; 3.24 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

personal_models_path: /home/mdupont/ggml/models
Binding name:gptq
Model name:llama2-7b-chat-codeCherryPop-qLoRA-GPTQ
Please select a valid model or install a new one from a url
mounting 0
Couldn't load personality. Please verify your configuration file at /home/mdupont/ggml/configs or use the next menu to select a valid personality
Binding returned this exception : The provided folder 
Traceback (most recent call last):
  File "/mnt/data1/2023/08/02/lollms/lollms/app.py", line 124, in mount_personality
    personality = PersonalityBuilder(self.lollms_paths, self.config, self.model, callback=callback).build_personality(id)
  File "/mnt/data1/2023/08/02/lollms/lollms/personality.py", line 1361, in build_personality
    self.personality = AIPersonality(
  File "/mnt/data1/2023/08/02/lollms/lollms/personality.py", line 156, in __init__
    self.load_personality(personality_package_path)
  File "/mnt/data1/2023/08/02/lollms/lollms/personality.py", line 186, in load_personality
    raise ValueError(f"The provided folder {package_path} does not exist.")
ValueError: The provided folder /home/mdupont/ggml/personalities_zoo/english/generic/pytorch does not exist.

personalities_zoo_path: /home/mdupont/ggml/personalities_zoo
Personalities:['english/generic/pytorch']
Active personality id:0
No active persona

      ___       ___           ___       ___       ___           ___      
     /\__\     /\  \         /\__\     /\__\     /\__\         /\  \     
    /:/  /    /::\  \       /:/  /    /:/  /    /::|  |       /::\  \    
   /:/  /    /:/\:\  \     /:/  /    /:/  /    /:|:|  |      /:/\ \  \   
  /:/  /    /:/  \:\  \   /:/  /    /:/  /    /:/|:|__|__   _\:\~\ \  \  
 /:/__/    /:/__/ \:\__\ /:/__/    /:/__/    /:/ |::::\__\ /\ \:\ \ \__\ 
 \:\  \    \:\  \ /:/  / \:\  \    \:\  \    \/__/~~/:/  / \:\ \:\ \/__/ 
  \:\  \    \:\  /:/  /   \:\  \    \:\  \         /:/  /   \:\ \:\__\   
   \:\  \    \:\/:/  /     \:\  \    \:\  \       /:/  /     \:\/:/  /   
    \:\__\    \::/  /       \:\__\    \:\__\     /:/  /       \::/  /    
     \/__/     \/__/         \/__/     \/__/     \/__/         \/__/     

Version: 2.3.1
By : ParisNeo


-----------------------------------------------------------------
Current personality : None
Traceback (most recent call last):
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/console3.py", line 242, in <module>
    cv = MyConversation(Path("config.yaml"))
  File "/mnt/data1/2023/08/02/lollms/examples/chat_forever/console3.py", line 129, in __init__
    super().__init__(cfg, show_welcome_message=False)
  File "/mnt/data1/2023/08/02/lollms/lollms/apps/console/__init__.py", line 50, in __init__
    print(f"{ASCIIColors.color_green}Version : {ASCIIColors.color_reset}{self.personality.version}")
AttributeError: 'NoneType' object has no attribute 'version'
(.venv) mdupont@mdupont-G470:~/experiments/chat_forever$ 