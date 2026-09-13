from __future__ import annotations

import unittest
from types import SimpleNamespace
from unittest.mock import patch

from ui import pages


class SceneLaunchContractTests(unittest.TestCase):
    def _state(self, *, active_scene_id: str | None, has_run: bool) -> SimpleNamespace:
        return SimpleNamespace(
            active_scene_id=active_scene_id,
            run_state=object() if has_run else None,
            sealed_scene_ids=set(),
        )

    def test_launch_card_uses_restart_for_current_scene(self) -> None:
        scene = object()
        state = self._state(active_scene_id="scene_test", has_run=True)
        with patch.object(pages, "get_state", return_value=state), patch.object(
            pages, "validate_scene"
        ), patch.object(pages, "card_open"), patch.object(pages, "card_close"), patch.object(
            pages, "primary_button", return_value=True
        ), patch.object(pages.st, "markdown"), patch.object(pages.st, "caption"), patch.object(
            pages.st, "rerun"
        ), patch.object(pages, "restart_scene") as restart_scene, patch.object(
            pages, "start_scene"
        ) as start_scene:
            pages._render_scene_launch_card("Test", "scene_test", "scenes.test", scene)

        restart_scene.assert_called_once_with("scene_test", scene)
        start_scene.assert_not_called()

    def test_launch_card_uses_start_for_different_scene(self) -> None:
        scene = object()
        state = self._state(active_scene_id="scene_other", has_run=True)
        with patch.object(pages, "get_state", return_value=state), patch.object(
            pages, "validate_scene"
        ), patch.object(pages, "card_open"), patch.object(pages, "card_close"), patch.object(
            pages, "primary_button", return_value=True
        ), patch.object(pages.st, "markdown"), patch.object(pages.st, "caption"), patch.object(
            pages.st, "rerun"
        ), patch.object(pages, "restart_scene") as restart_scene, patch.object(
            pages, "start_scene"
        ) as start_scene:
            pages._render_scene_launch_card("Test", "scene_test", "scenes.test", scene)

        start_scene.assert_called_once_with("scene_test", scene)
        restart_scene.assert_not_called()


if __name__ == "__main__":
    unittest.main()
