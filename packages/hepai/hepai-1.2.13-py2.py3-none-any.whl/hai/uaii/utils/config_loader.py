import os, sys
from pathlib import Path
from easydict import EasyDict

import functools
import collections
import copy
import re
import damei as dm
import hai
import json
import argparse

pydir = Path(os.path.abspath(__file__)).parent
logger = dm.get_logger(__name__)


class PyConfigLoader(collections.UserDict):
# class PyConfigLoader(object):
    """
    从字典、.py文件等获取的配置对象
    v1.0.1 支持元数据
    """

    def __init__(self, cfg_file=None, name=None, root_path=None, cfg_dict=None, **kwargs):
        super(PyConfigLoader, self).__init__()
        # super().__init__()
        work_dir = os.getcwd()
        self.root_path = root_path if root_path else f'{work_dir}'  # 默认当前工作目录
        self._name = name if name else f'{cfg_file}'  # 其实是path

        self._items = dict()
        self._load_items(cfg_file, cfg_dict, **kwargs)  # 从配置文件或配置字典初始化配置，配置添加到_items和对应的属性里
        self.check_items()  # TODO

    def _load_items(self, cfg_file=None, cfg_dict=None, **kwargs):
        if cfg_file is None and cfg_dict is None:
            return

        assert cfg_file or cfg_dict, 'Cfg_file or cfg_dict must be not None'
        assert not (cfg_file and cfg_dict), 'Only one of cfg_file and cfg_dict can have value'
        if cfg_file:
            assert os.path.exists(cfg_file), f'Config file {cfg_file} does not exist'
            self.init_config_by_file(cfg_file)  # 根据配置文件把内容和属性注册到items里
        else:
            self.init_config_by_dict(cfg_dict, **kwargs)

    def init_config_by_dict(self, cfg_file, **kwargs):
        """从字典初始化配置"""
        need_replace = kwargs.get('need_replace', False)  # 是否需要替换 - to _，默认不需要, needed when read config from dm.argparse shi xuyao
        for k, v in cfg_file.items():
            attr, attr_value = k, v
            if need_replace and '-' in attr:
                attr = attr.replace('-', '_')

            self._items[attr] = attr_value
            if isinstance(attr_value, dict):
                setattr(self, attr, EasyDict(self._items[attr]))
            else:
                setattr(self, attr, self._items[attr])

    def __len__(self):
        return len(self.items)

    # def __dict__(self):
    #   return self._items

    def __getitem__(self, item):
        return self.items[item]

    def __repr__(self):
        info = self.info(need_head=False, need_tail=False)
        if info == 'Empty config':
            format_str = f"Empty <class 'hai.Config'> "
        else:
            format_str = f"<class 'hai.Config'> " \
                        f"Configs:\n" \
                        f"{self.info(need_head=False, need_tail=False)}"

        return format_str

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        # print(f'__setitem__:{key}')
        # self.data[str(key)] = item
        self._items[str(key)] = item
        self.__setattr__(str(key), item)

    @property
    def path(self):
        return self._name

    @property
    def items(self):
        """
        debug: 
            when call self.some_attr = new_value, the new_value will be set to self.__dict__ only,
            but not to self._items.
            To fix this, we need to copy self.__dict__ to self._items every if the value is changed.
        """
        # for k, v in self._items.items():
        #     __dict__v = self.__dict__[k]
        #     if __dict__v != v:
        #         self._items[k] = __dict__v

        # return self._items
        return self.__dict__

    @staticmethod
    def from_anything(*args, **kwargs):
        """
        从字典、.py文件等获取的配置对象
        """
        if len(args) == 1:
            if isinstance(args[0], dict):
                return PyConfigLoader(cfg_dict=args[0], **kwargs)
            elif isinstance(args[0], str):
                return PyConfigLoader(cfg_file=args[0], **kwargs)
            else:
                raise NotImplementedError('Only support dict and str')
        return PyConfigLoader(**kwargs)

    @staticmethod
    def from_file(cfg_file, name=None, root_path=None):
        return PyConfigLoader(cfg_file, name, root_path)

    @staticmethod
    def fromfile(cfg_file, name=None, root_path=None):
        return PyConfigLoader(cfg_file, name, root_path)

    @staticmethod
    def from_dict(cfg_dict, name=None, root_path=None):
        """从字典创建配置对象"""
        name = name if name else 'cfg_from_dict'
        return PyConfigLoader(name=name, root_path=root_path, cfg_dict=cfg_dict)

    @staticmethod
    def from_argparser(args, name=None, root_path=None):
        """从hai.parser.ArgumentParser对象创建配置对象"""
        name = name if name else 'cfg_from_argparser'
        return PyConfigLoader(name=name, root_path=root_path, cfg_dict=args._args_dict)

    @staticmethod
    def from_argparse(opt, name=None, root_path=None):
        name = name if name else 'cfg_from_argparse'
        __dict__ = opt.__dict__
        # print(opt)
        return PyConfigLoader(name=name, root_path=root_path, cfg_dict=__dict__)

    @staticmethod
    def from_dm_argparse(opt, name=None, root_path=None):
        name = name if name else 'cfg_from_dm_argparse'
        __dict__ = opt._args_dict
        return PyConfigLoader(name=name, root_path=root_path, 
                            cfg_dict=__dict__, need_replace=True)


    def info(self, need_head=True, need_tail=True):
        """
        查看当前所有配置信息
        :param need_head: 是否需要包含头部信息，即：Configs:\n
        :param need_tail: 是否需要包含尾部信息，即：\n回车符
        """
        # info_str = f'{self.__repr__()}\n'
        info_dict = self._items
        if info_dict == {}:
            info_str = 'Empty config\n'
        else:
            info_str = f'Configs:\n' if need_head else ''
            info_str += dm.misc.dict2info(info_dict)
        if not need_tail:
            info_str = info_str[:-1]
        return info_str

    def init_config_by_file(self, cfg_file):
        if cfg_file is None:
            return
        rp = self.root_path
        cp = Path(os.path.abspath(cfg_file))  # config path

        if not os.path.exists(cfg_file):
            raise FileNotFoundError(f'{cfg_file} not found')

        # 提取模块路径：如：modules.detection.seyolov5.config
        method = 'method3'
        current_wd = os.getcwd()  # 当前工作目录
        if method == 'method1':
            module_dir = f'{str(cp.parent).replace(f"{rp}/", "").replace("/", ".")}'
            # print(f'rp: {rp} \ncp: {cp}\nm dir: {module_dir}')
            # code = f'from {module_dir} import {cp.stem}'
            code = f'import {module_dir}.{cp.stem} as {cp.stem}'
            # 不能用这种方法，原因是：from modules.xxx.config imort config 过程中会调起modules下的__init__.py,从而调起注册函数，导致重复注册
        elif method == 'method2':  # 方法2：添加临时环境路径
            # 这个方法在工作路径也存在config文件夹时，会导致from config import xxx 导入失败
            sys.path.append(f'{cp.parent.parent}')  # 添加临时环境路径, 如：/home/user/xx/modules/xx
            module_dir = f'{str(cp.parent.stem)}'  # configs文件夹路径，如：configs
            code = f'from {module_dir} import {cp.stem}'
        elif method == 'method3':  # 方法3：添加临时环境路径
            # sys.path.append(f'{cp.parent}')
            sys.path.insert(0, f'{cp.parent}')  # 添加临时环境路径, 如：/home/user/xx/modules/xx
            module_dir = '.'
            os.chdir(f'{cp.parent}')  # 切换工作目录
            # code = f'from {module_dir} import {cp.stem}'
            code = f'import {cp.stem}'
        else:
            raise ValueError(f'invalid method: {method}')

        # print(cfg_file, code)
        """
        exec(code)
        """
        try:
            exec(code)
        except Exception as e:
            msg = f'Error in "exec(code)": {e}. Error variables:\n' \
                  f'    root path: {rp} \n' \
                  f'    config file: {cfg_file} \n' \
                  f'    code: {code} \n' \
                  f'    module dir: {module_dir} \n' \
                  f'    sys.path[0]: {sys.path[0]} ' \
                  f'    sys.path[-1]: {sys.path[-1]}'
            # logger.error(msg)
            raise Exception(msg)
            # sys.exit(1)

        if method == 'method2':
            sys.path.remove(f'{cp.parent.parent}')  # 删除临时环境路径
        elif method == 'method3':
            sys.path.remove(f'{cp.parent}')
            os.chdir(current_wd)  # 切换回工作目录

        cfg = eval(cp.stem)  # 模块名

        # 读取文件获取顶格写并且不以#开头的属性
        with open(cfg_file, 'r', encoding='utf-8') as f:
            data = f.readlines()
        data = [x for x in data if not (x.startswith(' ') or x.startswith('#'))]  # 非顶格的不要，# 开头的不要
        data = '\n'+'\n'.join(data)
        attrs = re.findall(pattern=r"\s[A-Za-z]\w+ ?= ?", string=data)
        # The egular expression: \s[A-Za-z]\w+ ?= ? to match: ' attr = '
        # i.e. start with a space, then a letter (a to z or A to Z), 
        # then any number of letters, numbers or underscores, 
        # then a space, then an equal sign, then a space
        attrs = [x.split('=')[0].replace('\n', '').strip() for x in attrs]

        # 注册属性到_items里，注册属性到self的属性里。
        for attr in attrs:
            # print('xxx', attr)
            if hasattr(cfg, attr):
                exec(f"self._items[attr] = cfg.{attr}")
                attr_value = self._items[attr]
                if isinstance(attr_value, dict):
                    setattr(self, attr, EasyDict(self._items[attr]))
                else:
                    setattr(self, attr, attr_value)
            else:
                pass

    def check_items(self):
        """初始化末，检查所有配置项，处理：缩略语~转为真实路径。
        递归方法，如果v类型是str,判断替换，如果循环完了，结束，如果v的类型是dict，继续循环
        """
        # print(self._items)
        for k, v in self._items.items():
            new_v = self.recursive_func(v)
            self._items[k] = new_v
            # 更新属性
            if hasattr(self, k):
                delattr(self, k)
            setattr(self, k, EasyDict(new_v)) if isinstance(new_v, dict) else setattr(self, k, new_v)

    def recursive_func(self, value):
        """递归函数,如果v类型是str,判断替换，如果循环完了，结束，如果v的类型是dict，继续循环"""
        if value is None:
            return None
        elif isinstance(value, str):
            return value.replace('~', str(Path.home()))
        elif isinstance(value, int):
            return value
        elif isinstance(value, float):
            return value
        elif isinstance(value, bool):
            return value
        elif isinstance(value, list):
            new_list = [self.recursive_func(x) for x in value]
            return new_list
        elif isinstance(value, dict):
            new_dict = {}
            for k, v in value.items():
                new_dict[k] = self.recursive_func(v)
            return new_dict
        # elif isinstance(value, argparse.Namespace):  # TODO: suport argparse.Namespace
            # items = value.items()
        elif isinstance(value, hai.Config):
            new_dict = {}
            for k, v in value._items.items():
                new_dict[k] = self.recursive_func(v)
            new_config = PyConfigLoader.from_dict(new_dict)
            return new_config
        else:
            raise TypeError(f'Config file only support basic python types but the value type is: {type(value)}.')

    def update_item(self, attrs, value):
        """更新配置条目
        attrs: 长度为0时代表，更新全部value，长度为1时，代表第1个元素是第一层，
        """
        if len(attrs) == 0:
            self.merge(value)
        elif len(attrs) == 1:
            self._items[attrs[0]] = value
        elif len(attrs) == 2:
            self._items[attrs[0]][attrs[1]] = value
        elif len(attrs) == 3:
            self._items[attrs[0]][attrs[1]][attrs[2]] = value
        else:
            self._items[attrs[0]][attrs[1]][attrs[2]][attrs[3]] = value
        self.check_items()

    def merge2opt(self, opt):
        """
        合并配置文件到opt, 合并规则：没想好，先放着
        return: opt
        """
        assert isinstance(opt, argparse.Namespace), 'opt must be argparse.Namespace'
        raise NotImplementedError(f'未实现')

    def merge(self, cfg2, **kwargs):
        """合并另一个配置文件到内部，是inplace的"""
        if cfg2 is None:
            return self

        if isinstance(cfg2, dict):
            cfg2 = PyConfigLoader.from_dict(cfg2)

        for k2, v2 in cfg2._items.items():
            merged_v = self.recursive_func2(v2, k2=k2, sub_items=self._items)
            # self._items[k2] = merged_v
            self.__dict__[k2] = merged_v
        self.check_items()
        return self

    def recursive_func2(self, v2, k2=None, sub_items=None):
        """v1是之前的值，v2是现在的值"""
        if k2 and (k2 not in list(sub_items.keys())):
            return v2
        else:
            v1 = sub_items[k2]

            if type(v1) != type(v2):
                return v2
            f = functools.partial(isinstance, v1)
            if f(str) or f(int) or f(float) or f(bool):
                return v2
            elif f(list):
                tmp = [x for x in v2 if x not in v1]
                return v1 + tmp
            elif f(dict):  # v1v2都是dict
                new_dict = v1  # 保留v1
                for kk, vv in v2.items():
                    new_dict[kk] = self.recursive_func2(vv, k2=kk, sub_items=v1)
                return new_dict

    def map_keys(self, map_dict, new=True):
        """map_dict: {old_key: new_key}"""
        assert isinstance(map_dict, dict), 'map_dict must be dict'
        if new:
            new_cfg = copy.deepcopy(self)
            new_cfg.map_keys(map_dict, new=False)
            return new_cfg
        else:
            for k, v in map_dict.items():  # k是旧的，v是新的
                if k in self._items:
                    self.__dict__[v] = self.items[k]
                    del self.__dict__[k]
        

    def keys(self):
        return self._items.keys()

    def get(self, key, default=None):
        if key in list(self._items.keys()):
            return self._items[key]
        else:
            return default

    def to_dict(self):
        # raise NotImplementedError('to_dict is not implemented.')
        return self._items

    def to_json(self):
        return json.dumps(self._items, indent=4, ensure_ascii=False)
