import chess
import chess.svg


def suggest_moves(moves):
    board = chess.Board()

    for move in moves:
        board.push_uci(move)

    legal_moves = list(board.legal_moves)

    if legal_moves:
        suggested_move = legal_moves[0]
        return suggested_move.uci()
    else:
        return None


def save_board_as_svg(board, filename):
    with open(filename, "w") as f:
        f.write(chess.svg.board(board=board))


if __name__ == "__main__":
    previous_moves = ["e2e4", "e7e5", "g1f3", "b8c6", "f1c4"]
    suggested_move = suggest_moves(previous_moves)

    board = chess.Board()
    for move in previous_moves:
        board.push_uci(move)

    print("Current Board:")
    save_board_as_svg(board, "current_board.svg")

    if suggested_move:
        print(f"Suggested move: {suggested_move}")
        next_board = board.copy()
        next_board.push_uci(suggested_move)

        print("Next Board with Suggested Move:")
        save_board_as_svg(next_board, "next_board.svg")
    else:
        print("No legal moves available.")
