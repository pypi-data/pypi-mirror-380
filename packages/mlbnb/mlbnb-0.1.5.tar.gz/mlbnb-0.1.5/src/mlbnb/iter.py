from typing import Iterable, Iterator


class StepIterator:
    def __init__(self, delegate: Iterable, steps: int, step_per_iter: int = 1) -> None:
        """
        An iterator that repeats the delegate iterator until the
        specified number of steps is reached.

        :param delegate: An iterable to delegate the iteration to.
        :param steps: The total number of steps to yield items.
        :param step_per_iter: The number of steps to yield per iteration.
        """
        self.steps = steps
        self.delegate = delegate
        self.steps_per_iter = step_per_iter

    def __iter__(self) -> Iterator:
        current_step = 0
        while current_step < self.steps:
            delegate_iterator = iter(self.delegate)
            items_yielded_this_pass = 0
            for item in delegate_iterator:
                yield item
                current_step += self.steps_per_iter
                items_yielded_this_pass += 1
                if current_step >= self.steps:
                    break
            if items_yielded_this_pass == 0:
                # If the delegate is empty or exhausted and no items were yielded in this pass,
                # it means we can't make progress.
                break

    def __len__(self) -> int:
        return self.steps // self.steps_per_iter
