#!/usr/bin/env python3
import os


def get_path(p):
    return os.path.join(os.path.dirname(__file__), p)


INCOMPLETE_JSON = get_path("./data/incomplete.json")
