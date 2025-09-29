import pytest

from unittest import TestCase

from ztl.core.client import RemoteTask
from ztl.core.server import TaskServer

class TestConstruction(TestCase):

  def test_server_construction(self):
    server = TaskServer(7779)
    server.register("/dummy", None)

  def test_client_construction(self):
    RemoteTask("localhost", 7779, "/dummy")
