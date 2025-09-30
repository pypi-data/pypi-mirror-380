from decouple import Config, RepositoryEnv
from functools import wraps
import inspect
import os
from loguru import logger
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env.example')
def load_config(env_path=env_path):
    """配置加载装饰器"""
    config = Config(RepositoryEnv(env_path))
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 获取函数参数
            sig = inspect.signature(func)
            params = sig.parameters
            
            # 为每个参数从配置中获取值
            config_values = {}
            for param_name in params:
                param = params[param_name]
                # 跳过self参数
                if param_name == 'self':
                    continue
                    
                # 获取参数默认值和类型
                default = param.default if param.default != inspect.Parameter.empty else None
                annotation = param.annotation if param.annotation != inspect.Parameter.empty else type(default) if isinstance(default,type(None)) else type(default)
                # 从配置中读取值
                # if param_name.startswith('mysql_'):
                config_key = param_name

                if isinstance(default,type(None)) and annotation is type(None):
                    config_value = config(config_key) 
                elif isinstance(default,type(None)) and annotation is not type(None):
                    config_value = config(config_key, cast=annotation) 
                else:
                    config_value = config(config_key, cast=annotation, default=default) 
               
                config_values[param_name] = config_value
            
            # 使用配置值调用原函数
            return func(*args, **{**kwargs, **config_values})
            
        return wrapper
    return decorator





if __name__ == '__main__':
    
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env.example')
    @load_config(env_path=env_path)
    def get_config(MYSQL_HOST: str,
                MYSQL_PORT: int,
                MYSQL_USER: str = None,
                MYSQL_PASSWORD: str = None,
                MYSQL_DATABASE: str = None,
                EXTRA_INFO=111):
        # 函数实现...
        
        logger.info(f"MYSQL_HOST: {MYSQL_HOST}, MYSQL_PORT: {MYSQL_PORT}, MYSQL_USER: {MYSQL_USER}, MYSQL_PASSWORD: {MYSQL_PASSWORD}, MYSQL_DATABASE: {MYSQL_DATABASE}, EXTRA_INFO: {EXTRA_INFO}")

        
    get_config()
