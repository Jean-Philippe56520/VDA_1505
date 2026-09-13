from __future__ import annotations

import os
import unittest
from unittest.mock import patch

# repositories.scenes imports the real domain package in the repository. This
# test is intended to run from the checked-out project, where domain/ exists.
from repositories import scenes


class SceneBackendContractTests(unittest.TestCase):
    def test_default_backend_is_local(self) -> None:
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("VDA_SCENE_BACKEND", None)
            self.assertEqual(scenes.scene_backend(), "local")

    def test_hybrid_keeps_local_catalog_when_remote_is_empty(self) -> None:
        sentinel = {"s": ("scenes.test", object())}
        with patch.dict(os.environ, {"VDA_SCENE_BACKEND": "hybrid"}), patch.object(
            scenes, "load_local_scenes", return_value=dict(sentinel)
        ), patch.object(scenes, "load_supabase_scenes", return_value={}):
            self.assertEqual(scenes.load_scenes(), sentinel)

    def test_supabase_backend_falls_back_to_snapshot_then_local(self) -> None:
        local = {"local": ("scenes.local", object())}
        snapshot = {"snap": ("runtime:snap", object())}
        with patch.dict(os.environ, {"VDA_SCENE_BACKEND": "supabase"}), patch.object(
            scenes, "load_supabase_scenes", side_effect=RuntimeError("offline")
        ), patch.object(scenes, "load_snapshot_scenes", return_value=snapshot), patch.object(
            scenes, "load_local_scenes", return_value=local
        ):
            self.assertEqual(scenes.load_scenes(), snapshot)


if __name__ == "__main__":
    unittest.main()
