"""A simplified Promise implementation in Python, modeled after JavaScript's Promise.
Supports pending, resolved, and rejected states with then() chaining.
"""

PENDING = 'pending'
RESOLVED = 'resolved'
REJECTED = 'rejected'


class MyPromise:
    """A simple Promise implementation inspired by JavaScript Promises."""

    def __init__(self, fn):
        self.state = PENDING
        self.value = None
        self.resolved_callbacks = []
        self.rejected_callbacks = []

        def resolve(value):
            if self.state == PENDING:
                self.state = RESOLVED
                self.value = value
                for cb in self.resolved_callbacks:
                    cb(self.value)

        def reject(value):
            if self.state == PENDING:
                self.state = REJECTED
                self.value = value
                for cb in self.rejected_callbacks:
                    cb(self.value)

        try:
            fn(resolve, reject)
        except Exception as e:
            reject(e)

    def then(self, on_fulfilled=None, on_rejected=None):
        """Register callbacks for resolved and rejected states."""
        if on_fulfilled is None:
            on_fulfilled = lambda v: v
        if on_rejected is None:
            on_rejected = lambda r: r  # noqa: E731

        if self.state == PENDING:
            self.resolved_callbacks.append(on_fulfilled)
            self.rejected_callbacks.append(on_rejected)
        elif self.state == RESOLVED:
            on_fulfilled(self.value)
        elif self.state == REJECTED:
            on_rejected(self.value)
