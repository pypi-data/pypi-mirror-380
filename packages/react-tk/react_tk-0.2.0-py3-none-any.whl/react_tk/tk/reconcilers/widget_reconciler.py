from abc import abstractmethod
from dataclasses import dataclass
import threading
from tkinter import Tk, Widget, Label as TkLabel
from react_tk.renderable.node.prop_value_accessor import PropValuesAccessor
from react_tk.rendering.actions.node_reconciler import Compat
from react_tk.renderable.node.shadow_node import ShadowNode
from react_tk.props.impl.prop import Prop_ComputedMapping
from react_tk.rendering.actions.actions import (
    Create,
    Place,
    Recreate,
    Replace,
    RenderedNode,
    Unplace,
    Update,
)
from react_tk.rendering.actions.compute import AnyNode, ReconcileAction, logger
from react_tk.rendering.actions.reconcile_state import PersistentReconcileState

from react_tk.rendering.actions.node_reconciler import ReconcilerBase

from typing import Any, Callable, Iterable, override

from react_tk.tk.types.font import to_tk_font


@dataclass
class WidgetReconciler(ReconcilerBase[Widget]):
    state: PersistentReconcileState
    waiter = threading.Event()

    @classmethod
    def create(cls, state: PersistentReconcileState) -> "WidgetReconciler":
        return cls(state)

    @classmethod
    @override
    def get_compatibility(cls, older: RenderedNode[Widget], newer: AnyNode) -> Compat:
        if older.node.__class__.__name__ != newer.__class__.__name__:
            return "recreate"
        elif PropValuesAccessor(older.node).get().diff(PropValuesAccessor(newer).get()):
            return "replace"
        else:
            return "update"

    @abstractmethod
    def _create(self, container: Widget, node: AnyNode) -> RenderedNode[Widget]: ...

    def _pack(self, resource: Widget, diff: Prop_ComputedMapping):
        resource.pack_configure(
            **diff.values.get("Pack", {}),
        )

    def _pack_replace(self, what: Widget, replaces: Widget, diff: Prop_ComputedMapping):
        pack = diff.values.get("Pack")
        if not pack:  # pragma: no cover
            return
        pack["after"] = replaces
        self._pack(what, diff)

    def _pack_at(self, resource: Widget, diff: Prop_ComputedMapping, at: int):
        pack = diff.values.get("Pack", {})
        if not pack:  # pragma: no cover
            return
        slaves = resource.master.slaves()
        if slaves:
            if at >= len(slaves):
                pack["after"] = slaves[-1]
            elif at <= 0:
                pack["before"] = slaves[0]
            else:
                pack["after"] = slaves[at - 1]
        self._pack(resource, diff)

    def _update(self, resource: Widget, props: Prop_ComputedMapping) -> None:
        diff = props.values
        configure = diff.get("configure", {})
        if "font" in diff:
            configure["font"] = to_tk_font(diff["font"])
        if not configure:
            return
        resource.configure(**diff.get("configure", {}))

    def _get_some_ui_resource(self, node: ReconcileAction[Widget]) -> Widget | Tk:
        match node:
            case Update(existing):
                return existing.resource
            case x:
                container = x.container
                return self.state.existing_resources[container.__uid__].resource

    def _do_create_action(self, action: Update[Widget] | Create[Widget]):
        match action:
            case Create(next, container) as c:
                parent = self.state.existing_resources[container.__uid__].resource
                new_resource = self._create(parent, next)
                self._update(new_resource.resource, c.diff)
                self._register(next, new_resource.resource)
                return new_resource
            case Update(existing, next, diff):
                if diff:
                    self._update(existing.resource, diff)
                return existing.migrate(next)
            case _:
                assert False, f"Unknown action: {action}"

    def _run_action_main_thread(self, action: ReconcileAction[Widget]):
        try:
            if action:
                # FIXME: This should be an externalized event
                logger.info(f"⚖️  RECONCILE {action}")
            else:
                logger.info(f"🚫 RECONCILE {action.key} ")
                return

            match action:
                case Update(existing, next):
                    self._do_create_action(action)
                case Unplace(existing):
                    existing.resource.pack_forget()
                case Place(_, at, Recreate(old, next, container)) as x:
                    new_resource = self._do_create_action(Create(next, container))
                    old.resource.destroy()
                    self._pack_at(new_resource.resource, x.diff, at)
                case Place(container, at, createAction) as x if not isinstance(
                    createAction, Recreate
                ):
                    cur = self._do_create_action(createAction)
                    self._pack_at(cur.resource, x.diff, at)
                case Replace(_, existing, Recreate(old, next, container)) as x:
                    cur = self._do_create_action(Create(next, container))
                    self._pack_replace(cur.resource, existing.resource, x.diff)
                    old.resource.destroy()
                case Replace(container, existing, createAction) if not isinstance(
                    createAction, Recreate
                ):
                    cur = self._do_create_action(createAction)
                    self._pack_replace(
                        cur.resource, existing.resource, createAction.diff
                    )
                case _:
                    assert False, f"Unknown action: {action}"
        finally:
            self.waiter.set()

    def run_action(self, action: ReconcileAction[Widget], log=True):
        existing_parent = self._get_some_ui_resource(action)
        self.waiter.clear()
        existing_parent.after(0, lambda: self._run_action_main_thread(action))
        self.waiter.wait()


class LabelReconciler(WidgetReconciler):
    def _create(self, container: Widget, node: AnyNode) -> RenderedNode[Widget]:
        return RenderedNode(
            TkLabel(container),
            node,
        )


class FrameReconciler(WidgetReconciler):
    def _create(self, container: Widget, node: AnyNode) -> RenderedNode[Widget]:
        from tkinter import Frame as TkFrame

        return RenderedNode(
            TkFrame(container),
            node,
        )
