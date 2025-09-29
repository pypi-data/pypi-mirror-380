# -*- encoding: utf-8 -*-
import asyncio
import atexit
import inspect
import os
import warnings
from functools import partial, wraps
from pathlib import Path
from typing import Any, Callable, Dict, Optional, cast

from jsonrpcserver import method
from loguru import logger

from simplejrpc import exceptions  # type:ignore
from simplejrpc._sockets import JsonRpcServer  # type:ignore
from simplejrpc._types import WtfForm as _BaseForm  # type:ignore
from simplejrpc.config import Settings  # type:ignore
from simplejrpc.daemon.daemon import DaemonContext  # type:ignore
from simplejrpc.i18n import T as i18n  # type:ignore
from simplejrpc.interfaces import RPCMiddleware  # type:ignore
from simplejrpc.parse import (  # type:ignore
    IniConfigParser,
    JsonConfigParser,
    YamlConfigParser,
)
from simplejrpc.validate import BaseForm, Form  # type:ignore


class ServerApplication:
    """ """

    def __init__(
        self,
        socket_path: str,
        config: Optional[Settings] = Settings(),
        config_path: Optional[str] = os.path.join(os.getcwd(), "config.yaml"),
        i18n_dir: Optional[str] = os.path.join(os.getcwd(), "app", "i18n"),
    ):
        self.server = JsonRpcServer(socket_path)
        self.config_path = config_path
        self.config = config
        i18n.set_path(i18n_dir)  # type:ignore
        if self.config_path is not None and os.path.exists(self.config_path):
            self.from_config(config_path=self.config_path)

    def from_config(
        self,
        config_content: Optional[Dict[str, Any]] = None,
        config_path: Optional[str] = None,
    ) -> Settings:
        """ """
        if config_content:
            self.config = Settings(config_content)
        elif config_path:
            """ """
            config_content = self.load_config(config_path)
        if self.config is None:
            raise exceptions.ValueError("Config could not be loaded and is None")
        return self.config

    def route(
        self,
        name: Optional[str] = None,
        form: Optional[Any] = BaseForm,
        fn: Any = None,
    ) -> Callable[..., Any]:
        """路由装饰器"""
        if fn is None:
            return partial(self.route, name, form)

        @wraps(fn)
        def wrapper(*args, **kwargs):
            """ """
            if form:
                if not issubclass(form, Form):
                    warnings.warn(
                        "Please use form.Form instead, Please refer to version 2.2.0 for details"
                    )
                params = dict(zip(inspect.getfullargspec(fn).args, args))
                params.update(kwargs)
                form_validate = form(**params)  # type:ignore
                form_validate = cast(Form, form_validate)
                form_validate.raise_all_errors()
            return fn(*args, **kwargs)

        method(wrapper, name=name or fn.__name__)
        return wrapper

    def load_config(self, config_path: str) -> Dict[str, Any]:
        """ """

        if not os.path.exists(config_path):
            """ """
            raise exceptions.FileNotFoundError(f"Not found path {config_path}")

        path = Path(config_path)
        base_file = path.name
        _, filetype = base_file.split(".")

        match filetype:
            case "yml" | "yaml":
                parser = YamlConfigParser(config_path)
            case "ini":
                parser = IniConfigParser(config_path)
            case "json":
                parser = JsonConfigParser(config_path)
            case _:
                raise exceptions.ValueError("Unable to parse the configuration file")
        config_content: Dict[str, Any] = parser.read()
        self.config = Settings(config_content)
        self.setup_logger(config_content)
        return config_content

    def setup_logger(self, config_content: Dict[str, Any]):
        """ """
        # NOTE:: logger必须携带且sink必须携带
        logger_config_items = config_content.get("logger", {})
        if "sink" not in logger_config_items:
            return

        if (
            self.config is not None
            and hasattr(self.config, "logger")
            and hasattr(self.config.logger, "sink")
        ):
            sink: Any = self.config.logger.sink
            os.makedirs(Path(sink).parent, exist_ok=True)
            logger.add(**logger_config_items)
        else:
            warnings.warn(
                "Logger sink configuration is missing; skipping logger setup."
            )

    def clear_socket(self):
        """ """
        self.server.clear_socket()

    def middleware(self, middleware_instance: RPCMiddleware):
        """中间件配置"""
        return self.server.middleware(middleware_instance)

    def run_daemon(
        self,
        fpidfile: Optional[str],
        callback: Optional[Callable[[], Any]] = None,
    ) -> Any:
        """Start service in daemon mode"""
        with DaemonContext(fpidfile=fpidfile):
            # 创建异步事件循环
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            try:
                # 启动服务器并等待其结束
                server_task = loop.create_task(self.server.run())

                # 添加回调到服务器任务完成时
                if callback:
                    server_task.add_done_callback(lambda _: callback())

                loop.run_until_complete(server_task)
            except Exception as e:
                logger.error(f"Server error: {e}")
            finally:
                loop.close()

    async def run(
        self,
        daemon: bool = False,
        fpidfile: Optional[str] = None,
        callback: Optional[Callable[[], Any]] = None,
    ) -> Any:
        """
        :param daemon: Whether to run as a daemon process
        :param fpidfile: Guardian process PID file
        :return:
        """
        atexit.register(self.clear_socket)
        if daemon:
            self.run_daemon(fpidfile, callback=callback)
        else:
            await self.server.run()
