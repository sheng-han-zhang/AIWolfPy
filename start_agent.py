#!/usr/bin/env python

# This sample script connects to the AIWolf server, but
# does not do anything else. It will choose itself as the
# target for any actions requested by the server, (voting,
# attacking ,etc) forcing the server to choose a random target.
import logging
from logging import getLogger, StreamHandler, Formatter, FileHandler
import aiwolfpy
import argparse



# logger
def get_logger():
    logger = getLogger("aiwolfpy")
    logger.setLevel(logging.NOTSET)
    # handler
    stream_handler = StreamHandler()
    stream_handler.setLevel(logging.NOTSET)
    handler_format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(handler_format)
    logger.addHandler(stream_handler)
    return logger

# file_handler = FileHandler('aiwolf_game.log')
# file_handler.setLevel(logging.WARNING)
# file_handler.setFormatter(handler_format)
# logger.addHandler(file_handler)

# read args
def get_args():
    # name
    myname = 'sample_python'

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-p', type=int, action='store',default='10000', dest='port')
    parser.add_argument('-h', type=str,action='store',  default='localhost', dest='hostname')
    parser.add_argument('-r', type=str, action='store', dest='role', default='none')
    parser.add_argument('-a', type=str, action='store', default='default', dest='pipeline')
    parser.add_argument('-n', type=str, action='store', dest='name', default=myname)
    input_args = parser.parse_args()
    return input_args

def get_AgentClass(pipeline):
    import importlib
    abs_path = f'aiwolfpy.pipeline.{pipeline}.agent'
    Agent = getattr(importlib.import_module(abs_path), 'Agent')
    return Agent

# run
if __name__ == '__main__':
    input_args = get_args()
    logger = get_logger()
    Agent = get_AgentClass(input_args.pipeline)
    agent = Agent()

    client_agent = aiwolfpy.AgentProxy(
        agent, input_args.name, input_args.hostname, input_args.port, input_args.role, logger, "pandas"
    )
    client_agent.connect_server()