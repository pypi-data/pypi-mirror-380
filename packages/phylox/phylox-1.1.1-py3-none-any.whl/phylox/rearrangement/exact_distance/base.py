import time

from phylox.exceptions import NoSolutionException, TimeoutException
from phylox.isomorphism import is_isomorphic
from phylox.rearrangement.move import (
    Move,
    MoveType,
    all_valid_moves,
    apply_move_sequence,
)


class ExactMethodsMixin(object):
    def solve_depth_first(self, max_time=False, show_bounds=True):
        """
        An implementation of Algorithm 1 from R. Janssen's PhD thesis.
        Uses an iterated Depth First Search to simulate a Breath First Search.

        :param max_time: a float, a time limit for the function in seconds. If False, no time limit is used, and the function continues until it finds a sequence.
        :param show_bounds: a boolean parameter, if True the current lower bounds are printed to the terminal, used for debugging.
        :return: a shortest sequence of moves between the networks if it is found within the time limit, otherwise it returns an integer: a lower bound for the length of the shortest sequence between the networks.

        :example:
        >>> from phylox.rearrangement.rearrangementproblem import RearrangementProblem

        """
        lower_bound = 0
        stop_time = False
        if max_time:
            stop_time = time.time() + max_time
        while True:
            output = self.solve_depth_first_bounded(
                max_depth=lower_bound, stop_time=stop_time
            )
            if type(output) == list:
                break
            lower_bound += 1
            if show_bounds:
                print(lower_bound)
        return output

    # Finds a shortest sequence between network1 and network2 using DFS with bounded depth
    def solve_depth_first_bounded(self, max_depth=0, stop_time=False):
        """
        A subroutine of Algorithm 1 of R. Janssen's PhD thesis.
        A depth-bounded Depth First Search used to simulate
        a Breath First Search.

        :param max_depth: a integer, the maximum depth for the search tree.
        :param stop_time: a float, a time limit for the function in clock time.
            If False, no time limit is used, and the function continues until
            it finds a sequence.
        :return: a shortest sequence of at most max_depth moves between the
            networks if it is found before the stop_time, otherwise it returns an False.
        """
        # Make a stack and search
        stack = [[]]
        while stack:
            current_moves = stack.pop()
            current_length = len(current_moves)
            current_network = apply_move_sequence(self.network1, current_moves)
            if current_length == max_depth and is_isomorphic(
                current_network, self.network2
            ):
                return current_moves
            if current_length < max_depth:
                stack += [
                    current_moves + [move]
                    for move in all_valid_moves(current_network, self.move_type)
                ]
            if stop_time and time.time() > stop_time:
                raise TimeoutException
        return False


# # Finds a shortest sequence between network1 and network2 using BFS
# def Breadth_First(network1, network2, tail_moves=True, head_moves=True, max_time=False):
#     """
#     A true BFS implementation to find a shortest sequence between two networks. This implementation uses too much memory, use Depth_First!

#     :param network1: a phylogenetic network.
#     :param network2: a phylogenetic network.
#     :param tail_moves: a boolean value determining whether tail moves are used.
#     :param head_moves: a boolean value determining whether head moves are used.
#     :param max_time: a float, a time limit for the function in seconds. If False, no time limit is used, and the function continues until it finds a sequence.
#     :return: a shortest sequence of moves between the networks if it is found within the time limit, otherwise it returns an integer: a lower bound for the length of teh shortest sequence between the networks.
#     """
#     # If we cannot do any moves:
#     if not tail_moves and not head_moves:
#         if Isomorphic(network1, network2):
#             return 0
#         else:
#             return False
#     # Else, make a queue and search
#     queue = deque([[]])
#     start_time = time.time()
#     while queue:
#         current_moves = queue.popleft()
#         current_network = network1
#         for move in current_moves:
#             current_network = DoMove(current_network, *move)
#         if Isomorphic(current_network, network2):
#             return current_moves
#         validMoves = AllValidMoves(current_network, tail_moves=tail_moves, head_moves=head_moves)
#         for move in validMoves:
#             queue.append(current_moves + [move])
#         if max_time and time.time() - start_time > max_time:
#             return len(current_moves)
#     return False
