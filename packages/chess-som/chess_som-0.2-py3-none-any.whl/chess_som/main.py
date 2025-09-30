import sys
import re

import random


class Board():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    def __init__(self, player_color):
        self.player_color = player_color
        self.set_variables()
        """creates a functional board with lists as rows and dicts as squares"""
        self.fboard = []
        for i in range(8):
            row = []
            for j in range(8):
                """makes checkerboard pattern"""
                color = "⬛️"
                if (i % 2 and j % 2) or (i % 2 == False and j % 2 == False):
                    color = "⬜️"
                row.append({"square": str(Board.letters[j]) + str(abs(8 - i)), "color": color, "piece": None})
            self.fboard.append(row)
        """creates a board for aesthetics. follows x, y coordinates on a plane"""
        self.board = list(self.fboard)
    def place_piece(self, *args, capture=True, ui=None):
        for arg in args:
            """updates the board"""
            """adds piece to captured list if move captures piece"""
            if capture:
                Board.add_captured(self.fboard[int(arg.y)][int(arg.x)]["piece"])
            self.fboard[int(arg.y)][int(arg.x)]["piece"] = arg
            """passes the board to piece objects"""
            arg.fboard, arg.board = self.fboard, self
            if self.is_setup:
                Board.capture_en_passent(arg)
    def move(self, piece, x, y, ui=None):
        """clears previous square, and moves piece to specified square"""
        self.fboard[int(piece.y)][int(piece.x)]["piece"] = None
        captured_p = self.fboard[int(y)][int(x)]["piece"]
        if captured_p and ui:
            ui.moves_from_last_capture = 0
        if abs(piece.y - y) == 2 and piece.__class__ == Pawn:
            piece.moved_two_squares = True
        else:
            piece.moved_two_squares = False
        piece.x = x
        piece.y = y
        self.delete_piece(captured_p)
        self.place_piece(piece)
        if UI.should_promote(piece):
            if ui.game_mode == "random" and UI.color_turn(ui.turns) == ui.op_color: 
                self.promote(piece)
            else:
                self.promote(piece, UI.ask_promote_to(piece.pos()))
    def delete_piece(self, piece):
        if not piece:
            return
        if piece.color == "white":
            print("yes", len(self.white_pieces))
            self.white_pieces.remove(piece)
            print("adsf", len(self.white_pieces))
        else:
            self.black_pieces.remove(piece)
    def __str__(self):
        """prints complete board with pieces and color squares"""
        p = ""
        rows_number = reversed(list(range(8)))
        if self.player_color == "black":
            rows_number = range(8)
        for i in rows_number:
            p = p + str(self.captured_w[i]) + str(self.captured_w[abs(15-i)]) + " "
            p = p + str(i + 1) + " "
            for j in range(8):
                if self.board[i][j]["piece"]:
                    p = p + str(self.board[i][j]["piece"])
                else: 
                    p = p + self.fboard[i][j]["color"]
            p = p + " " + str(self.captured_b[abs(15-i)]) + str(self.captured_b[i]) + "\n"
        p = p + "       " + " ".join(Board.letters)
        return p
    def turn_board(self):
        if self.player_color == "white":
            self.player_color = "black" 
        else:
            self.player_color = "white"
        print(self)
    def places(self):
        """prints square coordinates"""
        p = ""
        for i in range(8):
            if self.player_color == "white":
                p = p + str(abs(8-i)) + " "
            else:
                p = p + i
            for j in range(8):
                p = p + self.board[i][j]["square"] + " "
            p = p + "\n"
        p = p + "  " + "  ".join(Board.letters)
        return p
    def setup(self):
        """sets up normal chess on the board"""
        row = [Rook(0, 0), Knight(1, 0), Bishop(2, 0), Queen(3, 0), King(4, 0), Bishop(5, 0), Knight(6, 0), Rook(7, 0)]
        """sets up first and last rank"""
        for piece in row:
            self.place_piece(piece)
            self.white_pieces.append(piece)
            """collects white pieces in a set and does the same with black"""
            y, x = abs(piece.y - 7), piece.x
            self.place_piece(piece.__class__(x, y, "black"))
            self.black_pieces.append(self.fboard[y][x]["piece"])
        """sets up pawn rows"""
        for i in range(8):
            self.place_piece(Pawn(i, 1), Pawn(i, 6, "black"))
            self.white_pieces.append(self.fboard[1][i]["piece"])
            self.black_pieces.append(self.fboard[6][i]["piece"])
        self.is_setup = True
    def set_variables(self):
        self.is_setup = False
        self.white_pieces = list()
        self.black_pieces = list() 
        self.captured_w = list()
        self.captured_b = list()
        for _ in range(16):
            self.captured_w.append("  ")
            self.captured_b.append("  ")
    def get_pieces(self, color):
        if color == "white":
            return self.white_pieces
        return self.black_pieces
    def castle(self, command, color):
        y = 0 if color != "black" else 7
        if command == "0-0-0":
            self.move(self.fboard[y][4]["piece"], 2, y)
            self.move(self.fboard[y][0]["piece"], 3, y)
        else:
            self.move(self.fboard[y][4]["piece"], 6, y)
            self.move(self.fboard[y][7]["piece"], 5, y)
    def promote(self, piece, to="Q"):
        pos = piece.pos()
        color = piece.color
        del(piece)
        match to:
            case "R": 
                cls = Rook().__class__
            case "B": 
                cls = Bishop().__class__
            case "Q": 
                cls = Queen().__class__
            case "N": 
                cls = Knight().__class__
        self.place_piece(cls(*pos, color, self.fboard, self), capture=False)
    def get_adjacent_piece(piece, dx):
        x = piece.x + dx
        if 0 <= x < 8:
            return piece.fboard[piece.y][x]["piece"]
    def get_behind(piece, get="coordinates", x=None, y=None, color=None):
        x = x if x is not None else piece.x
        y = y if y is not None else piece.y
        color = color if color is not None else piece.color
        dy = -1
        if color == "black":
            dy = 1
        if 0 <= y + dy < 8:
            if get == "piece" and piece.board.fboard[y + dy][x]["piece"]:
                return piece.fboard[y + dy][x]["piece"]
            return ((x, y + dy))
    def add_captured(piece):
        if not piece:
            return
        board = piece.board
        if piece.color == "white":
            board.captured_w.append(piece)
            del(board.captured_w[0])
        else:
            board.captured_b.append(piece)
            del(board.captured_b[0])
    def capture_en_passent(piece):
        if not piece:
            return
        behind_p = Board.get_behind(piece, get="piece")
        if behind_p.__class__ == Pawn:
            if behind_p.moved_two_squares:
                pos = behind_p.pos()
                piece.fboard[int(pos[1])][int(pos[0])]["piece"] = None
                Board.add_captured(behind_p)    
    def get_piece(board, coordinates):
        if coordinates:
            return board[coordinates[1]][coordinates[0]]
class Piece():
    def __init__(self, x=0, y=0, color="white", fboard=None, board=None):
        self.x = x
        self.y = y
        self.color = color
        self.fboard = fboard
        self.board = board
    def positions_from_pos(og_pos, direction, fboard, pass_king=False, limit_one=False):
        moves = set()
        x, y = og_pos[0], og_pos[1]
        dx, dy = direction[0], direction[1]
        end_piece = None
        while 0 <= x + dx < 8 and 0 <= y + dy < 8:
            """moves up, down, right, and left by adding and subtracting x and y values"""
            x += dx
            y += dy
            piece = fboard[y][x]["piece"]
            if piece == None:
                moves.add((x, y))
            elif pass_king and fboard[y][x]["piece"].__class__ == King:
                moves.add((x, y))
            else:
                end_piece = ((x, y))
                break
            if limit_one:
                break
        return moves, end_piece
    def check_direction(og_pos, direction, color, fboard, limit_one=False, pass_king=False):
        moves = set()
        """gets moves in a certain direction until it hits a piece"""
        moves, end_piece = Piece.positions_from_pos(og_pos, direction, fboard, limit_one=limit_one, pass_king=pass_king)
        """adds end piece if it is capturable"""
        if end_piece:
            x, y = end_piece[0], end_piece[1]
            if fboard[y][x]["piece"].color != color:
                moves.add((x, y))
        return moves
    def set_values(self, x=None, y=None, color=None, fboard=None):
        """sets values for manual inputs or an input of self"""
        x = x if x is not None else self.x
        y = y if y is not None else self.y
        color = color if color is not None else self.color
        fboard = fboard if fboard is not None else self.fboard
        return x, y, color, fboard
    def directional_moves(self, directions, x=None, y=None, color=None, fboard=None, pass_king=False, limit_one=False):
        """handles assignment with manual inputs and with piece"""
        x, y, color, fboard = self.set_values(x, y, color, fboard)
        """direction moves for x and y respectively"""
        moves = set()
        """adds every possible position in every single direction without considering board states like check and pin"""
        for pos in directions:
            moves |= Piece.check_direction((x, y), pos, color, fboard, pass_king=pass_king, limit_one=limit_one)
        return moves
    def is_attacked(possible_pos, color, fboard, pass_king=False):
        attackers = set()
        x, y = possible_pos[0], possible_pos[1]
        piece_types = [Knight(), Pawn(), Bishop(), Rook(), Queen()]
        """takes piece and puts it in the possible position, if it can capture any of the opponents pieces of the same type, then those must be attackers"""
        for type in piece_types:
            if type.__class__ == Pawn:
                for pos in type.raw_moves(x=x, y=y, color=color, fboard=fboard, captures=True):
                    if fboard[pos[1]][pos[0]]["piece"].__class__ == type.__class__:
                        attackers.add(fboard[pos[1]][pos[0]]["piece"])
            else:
                for pos in type.raw_moves(x=x, y=y, color=color, pass_king=pass_king, fboard=fboard):
                    if fboard[pos[1]][pos[0]]["piece"].__class__ == type.__class__:
                        attackers.add(fboard[pos[1]][pos[0]]["piece"])
        """king is done separately to avoid recursion, but works in the same way as above without the helper function, raw_moves()"""
        for pos in King.positions:
            if 0 <= x + pos[0] < 8 and 0 <= y + pos[1] < 8:
                if fboard[y + pos[1]][x + pos[0]]["piece"].__class__ == King:
                    if fboard[y + pos[1]][x + pos[0]]["piece"].color != color:
                        attackers.add(fboard[y + pos[1]][x + pos[0]]["piece"])
                        break
        if len(attackers) != 0:   
            return attackers                                             
        return False
    def pos(self):
        return ((self.x, self.y))
    def update_var(piece):
        if piece and piece.__class__ == Rook or piece.__class__ == King:
            piece.has_moved = True  
class Rook(Piece):
    positions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def __init__(self, x=0, y=0, color="white", fboard=None, board=None): 
        super().__init__(x, y, color, fboard, board=None)
        self.has_moved = False
        self.fen_chr = "R" if color == "white" else "r"
    def __str__(self):
        return "♜ " if self.color == "white" else "♖ "
    def raw_moves(self, **kwargs):
        return self.directional_moves(Rook.positions, **kwargs)     
class Queen(Piece):
    positions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    def __init__(self, x=0, y=0, color="white", fboard=None, board=None): 
        super().__init__(x, y, color, fboard, board)
        self.fen_chr = "Q" if color == "white" else "q"
    def __str__(self):
        return "♛ " if self.color == "white" else "♕ "
    def raw_moves(self, **kwargs):
        return self.directional_moves(Queen.positions, **kwargs)
class Bishop (Piece):
    positions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    def __init__(self, x=0, y=0, color="white", fboard=None, board=None): 
        super().__init__(x, y, color, fboard, board)
        self.fen_chr = "B" if color == "white" else "b"
    def __str__(self):
        return "♝ " if self.color == "white" else "♗ "
    def raw_moves(self, **kwargs):
        return self.directional_moves(Bishop.positions, **kwargs)
class King(Piece):
    positions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    def __init__(self, x=0, y=0, color="white", fboard=None, board=None): 
        super().__init__(x, y, color, fboard, board)
        self.fen_chr = "K" if color == "white" else "k"
        self.has_moved = False
    def __str__(self):
        return "♚ " if self.color == "white" else "♔ "
    def raw_moves(self, **kwargs):
        moves = self.directional_moves(King.positions, **kwargs, limit_one=True)
        new_moves = set()
        for move in moves:
            if not Piece.is_attacked(move, self.color, self.fboard, pass_king=True):
                new_moves.add(move)
        return new_moves
class Knight(Piece):
    positions = [(1, 2), (-1, 2), (2, 1), (2, -1), (-2, 1), (-2, -1), (1, -2), (-1, -2)]
    def __init__(self, x=0, y=0, color="white", fboard=None, board=None): 
        super().__init__(x, y, color, fboard, board)
        self.fen_chr = "N" if color == "white" else "n"
    def __str__(self):
        return "♞ " if self.color == "white" else "♘ "
    def raw_moves(self, **kwargs):
        return self.directional_moves(Knight.positions, limit_one=True, **kwargs)
class Pawn(Piece):
    def __init__(self, x=0, y=0, color="white", fboard=None, board=None): 
        super().__init__(x, y, color, fboard, board)
        self.moved_two_squares = False
        self.fen_chr = "P" if color == "white" else "p"
    def __str__(self):
        return "♟ " if self.color == "white" else "♙ "
    def raw_moves(self, x=None, y=None, color=None, fboard=None, captures=False, pass_king=False):
        """handles assignment with manual inputs and with piece"""
        x, y, color, fboard = self.set_values(x, y, color, fboard)
        moves = set()
        dy = 1
        if color == "black":
            dy = -1
        """adds to moves if pawn can capture pieces diagonal of it"""
        for i in [-1, 1]:
            if 0 <= x + i < 8:
                if fboard[y + dy][x + i]["piece"]:
                    if fboard[y + dy][x + i]["piece"].color != color:
                        moves.add((x + i, y + dy))
        if captures:
            return moves
        """adds forward one"""
        if 0 <= y + dy <= 7 and fboard[y + dy][self.x]["piece"] == None:
            moves.add((x, y + dy))
        """adds forward 2 spaces move if legal"""
        try:
            if (y == 1 or y == 6) and self.fboard[y + (dy * 2)][x]["piece"] == None and fboard[y + dy][x]["piece"] == None:
                    moves.add((x, y + (dy * 2)))
        except:
            pass
        return moves
class GameRules(Piece, Board):
    """helper functions"""
    def get_king(color, board):
        for piece in board.get_pieces(color):
            if piece.__class__ == King:
                return piece
    def legal_moves(piece):
        """stores special cases to filter out later, if not special case, return normal moves"""
        adj_p = GameRules.can_en_passent(piece)
        if GameRules.check_if_check(piece.color, piece.board):
            possible_moves, error_message = GameRules.king_is_check(piece), "King is checked"
        elif GameRules.is_pinned(piece):
            possible_moves, error_message = GameRules.is_pinned(piece), "Piece is pinned"
        else:
            legal_moves = piece.raw_moves()
            """adds castling if possible"""
            if piece.__class__ == King or piece.__class__ == Rook:
                legal_moves.update(GameRules.castle_moves(piece.color, piece.fboard))
            """adds en passent to moves player can do"""
            if adj_p:
                legal_moves.add(Board.get_behind(adj_p))
            return legal_moves, "Invalid move"
        """picks out piece's raw moves if they are not valid"""
        legal_moves = set()
        for move in piece.raw_moves():
            if move in possible_moves:
                legal_moves.add(move)
        
        if GameRules.check_if_check(piece.color, piece.board):
            """en passent piece could have possibly checked king. If so, add to legal moves."""
            if adj_p not in GameRules.king_is_check(piece):
                return legal_moves, error_message
        if piece.__class__ == King or piece.__class__ == Rook:
                legal_moves.extend(GameRules.castle_moves(piece.color, piece.board))
        if adj_p:
            legal_moves.add(Board.get_behind(adj_p))
        return legal_moves, error_message
    def check_if_legal(piece, move):
        """called before moving piece. Checks if given move is legal"""
        legal_moves, error_message= GameRules.legal_moves(piece)
        if move in legal_moves:
            return True
        else:
            return error_message
    """checks game state"""
    def check_if_check(color, board):
        #checks if either king is checked, will activate after move!!
        king = GameRules.get_king(color, board)
        if Piece.is_attacked(king.pos(), color, king.fboard):
            return color
        return False
    def check_end_game(piece):
        """checks for both checkmate and stalemate"""
        """is called after opponent moves and checks opponents pieces"""
        color = "black"
        if piece.color == "black":
            color = "white"
        """generates message if king is checked or not"""
        if GameRules.check_if_check(color, piece.board):
            message = "Checkmate!"
        else:
            message = "Stalemate!"
        """checks if any of player's pieces can move. Returns False and no message if can"""
        for piece in piece.board.get_pieces(color):
            legal_moves, error_message = GameRules.legal_moves(piece)
            if len(legal_moves) > 0:
                return False, None
        return True, message
    """returns moves for pieces with limiting factors"""
    def is_pinned(piece):
        fboard = piece.fboard
        king = GameRules.get_king(piece.color, piece.board)
        for direction in King.positions:
            empty, mid = Piece.positions_from_pos((king.x, king.y), direction, fboard)
            if mid != piece.pos():
                continue
            empty2, end = Piece.positions_from_pos(piece.pos(), direction, fboard)
            if not end:
                continue
            end = fboard[end[1]][end[0]]["piece"]
            if piece.pos() in end.raw_moves():
                empty.add(end.pos())
                return empty | empty2
        return False
    def king_is_check(piece):
        """called when player inputs a piece to move. Returns a list of valid moves which would stop the check"""
        """if player tries to move king then it returns the normal king moves"""
        if piece.__class__ == King:
            return piece.raw_moves()
        king = GameRules.get_king(piece.color, piece.board)
        """returns piece threatening king"""
        attackers = Piece.is_attacked(king.pos(), king.color, king.fboard)
        """handles double check"""
        if len(attackers) > 1:
            return set()
        for a in attackers:
            attacker = a   
        """when attacking piece is a knight or a pawn, the player can only stop check by capturing the piece"""
        if attacker.__class__ == Knight or attacker.__class__ == Pawn:
            return attacker.pos()
        """gives list of moves that can block/capture attacking piece"""
        for direction in attacker.positions:
            empty, end = Piece.positions_from_pos(king.pos(), direction, king.fboard)
            if end == attacker.pos():
                break
        empty.add(end)
        return empty
    def castle_moves(color, board):
        valid_commands = []
        y = 0
        if color == "black":
            y = 7
        """checks if king is checked when castled"""
        if not Piece.is_attacked((2, y), color, board):
            """gives x-values of the king and rook and all of the pieces in between for long castling"""
            if GameRules.check_castle(list(range(4, 8)), y, board):
                valid_commands.append("0-0")
        """Same thing, but short castling"""
        if not Piece.is_attacked((6, y), color, board):
            if GameRules.check_castle(list(range(0, 5)), y, board):
                valid_commands.append("0-0-0")
        return valid_commands
        
    def check_castle(x_list, y, board):
        pieces = set()
        """gets pieces in places a-e or e-h in relation to the player based on x values"""
        for x in x_list:
            if board[y][x]["piece"]:
                pieces.add(board[y][x]["piece"])
        """checks if the only pieces are the rook and king and if they have moved"""
        if len(pieces) != 2:
            return False
        for piece in pieces:
            if piece.__class__ != Rook and piece.__class__ != King:
                return False
            elif piece.has_moved == True:
                return False
        return True
    def should_promote(piece):
        return piece.__class__ == Pawn and piece.y in [0, 7]
    def can_en_passent(piece, get=""):
        adj_p = None
        adjacent_pieces = [Board.get_adjacent_piece(piece, -1), Board.get_adjacent_piece(piece, 1)]
        for p in adjacent_pieces:
            if p.__class__ == Pawn and p.color != piece.color:
                if p.moved_two_squares:
                    adj_p = p
        if not adj_p:
            return
        piece.fboard[adj_p.y][adj_p.x]["piece"] = None
        if GameRules.is_pinned(piece):
            piece.fboard[adj_p.y][adj_p.x]["piece"] = adj_p
            return
        return adj_p
class UI(GameRules):
    def start(self, game_mode="player"):
        self.game_mode = game_mode
        self.set_players()
        self.setup_board(self.player_color)
        self.turns = 0
        self.moves_from_last_capture = 0
        command = ""
        print(self.board)
        while True:
            """gets move from player or opponent(dunno if robot) then will execute it. player move and op move alr checks it and stuff then will display 
            board after move wont show board if player gets wrong, will just display error message"""
            command = self.get_move()
            print(command)
            
            if not command:
                sys.exit("No command generated")
            if command == "0-0-0" or command == "0-0":
                self.board.castle(command, UI.color_turn(self.turns))
            else:
                self.board.move(*command, ui=self)
                result, message = GameRules.check_end_game(piece=command[0])
                if result:
                    print(self.board)
                    print(message)
                    break  
            self.moves_from_last_capture += 1
            if self.moves_from_last_capture == 100:
                UI.ask_draw(UI.color_turn(self.turns), "50 Moves Rule")
            self.turns += 1
            print(self.board)
        return 
    def get_move(self):
        while True:
            
            color = UI.color_turn(self.turns)
            if color == self.player_color:
                command = UI.ask_move(color)
            else:
                match self.game_mode:
                    case "player":
                        command = UI.ask_move(color)
                    case "random":
                        command = Random.generate_random_move(color, self.board)
            """checks if it's a help command or if it is invalid"""
            if not UI.is_chess_notation(command):
                if UI.is_command(command):
                    print(self.execute_command(command))
                else:
                    print("Invalid response")
                continue
            if command == "0-0" or command == "0-0-0":
                return command
            piece, move = UI.convert_cmd_info(self.board, command, color)
            print(command)
            if piece:
                return piece, move[0], move[1]
            else:
                """if there's no piece, move contains an error string"""
                print(move)
    def ask_move(color):
            """get move from user"""
            return input(str(color).capitalize().strip() + " move? ")
    def convert_cmd_info(board, move, color):
        if not UI.is_chess_notation(move):
            return None, "Invalid move"
        if move == "0-0-0" or move == "0-0":
            if move in GameRules.castle_moves(color, board.fboard):
                return move, ""
            else:
                return None, "Cannot castle"
        """splits move into information for the execute function"""
        piece, move, message= UI.get_piece(*UI.decode(color, move), board)
        if message:
            return None, message
        """updates piece variables for special cases"""
        piece.update_var()
        return piece, move

    def execute_command(self, move):
        """executes commands to help the player like help, stop, or show moves"""
        match move:
            case "stop":
                sys.exit("Game Terminated")
            case "turn board":
                self.board.turn_board()
                return "Board Turned"
            case "piece moves":
                """returns moves for specified piece"""
                square = input("What square? ")
                """checks if command is a square"""
                piece = UI.get_piece_from_square(square, self.board.fboard)
                """checks if piece exists, else returns False"""
                if piece:
                    moves, message = GameRules.legal_moves(piece)
                    if not moves:
                        moves = "No possible moves"
                    else:
                        moves = UI.convert_coordinates(moves)
                    if message == "Invalid move":
                        return moves
                    return moves + " | " + str(message)
                return False
            case "en passent":
                square = input("What square? ")
                piece = UI.get_piece_from_square(square, self.board.fboard)
                if piece:
                    return "Yes, piece " + UI.convert_coordinates([piece.pos()])
            case _:
                return False
    def set_players(self):
        player = UI.ask_player_color()
        if player == "white":
            self.player_color, self.op_color = player, "black"
        else:
            self.player_color, self.op_color =  player, "white"
        if self.game_mode == "ai":
            self.ai = AI(self.op_color)
    def ask_player_color():
        while True:
            color = input("Black or White? ")
            if str.lower(color) in ["black", "white"]:
                break
            print("Invalid response")
        return color
    def ask_draw(color, message):
        print(message)
        player_response = input((f"{color.title()} Draw? Y/N "))
        op_response = input((f"{UI.op_color(color).title()} Draw? Y/N "))
        if player_response == "Y" and op_response == "Y":
            sys.exit("Draw by agreement!")
    def ask_promote_to(piece_pos):
        while True:
            promotion = input(f"Promote Pawn {UI.convert_coordinates([piece_pos])} to? (Q/R/B/N) ").strip().upper()
            if promotion in ["Q", "R", "B", "N"]:
                return promotion
    def setup_board(self, player_color):
        self.board = Board(player_color)
        self.board.setup()
    def get_piece(color, cls, x, y, info, board):
        """actually, gets piece that player is talking abt"""
        for piece in board.get_pieces(color):
            if piece.__class__ != cls: 
                continue
            message = GameRules.check_if_legal(piece, (x, y))
            if message.__class__ == str:
                continue
            """gets x and y of piece and handles double disambiguation"""
            if info == piece.x or info == piece.y:
                return piece, ((x, y)), None
            elif info == None:
                return piece, ((x, y)), None
        """if no piece is found that can do the move, returns error message """
        return None, None, message
    def decode(color, cmd):
        """intakes chess notation and interprets it into useful data"""
        match cmd[0:1]:
            case "R": 
                piece_cls = Rook().__class__
            case "B": 
                piece_cls = Bishop().__class__
            case "Q": 
                piece_cls = Queen().__class__
            case "N": 
                piece_cls = Knight().__class__
            case "K": 
                piece_cls = King().__class__
            case _:
                piece_cls = Pawn().__class__
                cmd = "P" + cmd
        if len(cmd) == 4 and (cmd[1:3].isalpha() or (cmd[1:2].isdigit() and cmd[3:4].isdigit())):
            extra_info, h, v = cmd[1:2], cmd[2:3], cmd[3:4]
        else:
            extra_info, h, v = None, cmd[1:2], cmd[2:3]
        if extra_info == "x":
            extra_info = None
        if extra_info:
            extra_info = UI.convert_letter(extra_info)
        h = UI.convert_letter(h)
        v = int(v) - 1
        return color, piece_cls, h, v, extra_info
    def convert_letter(l):
        """converts player coordinates to fboard coordinates"""
        l = str(l)
        if l.isdigit():
            return int(l) -1
        for i in range(8):
            if l == Board.letters[i]: 
                return i
    def convert_number(l):
        """converts fboard coordinate to player letter coordinate"""
        l = int(l)
        return Board.letters[l]
    def convert_coordinates(tuple_set, letter=False, list=False):
        """converts fboard coordinates to string list of places"""
        new_set = set()
        for tuple in tuple_set:
            """filters out castle notation"""
            if tuple == "0-0" or tuple == "0-0-0":
                new_set.add(tuple)
                continue
            if letter:
                new_set.add(letter + UI.convert_number(tuple[0]) + str(tuple[1] + 1))
                continue
            new_set.add(UI.convert_number(tuple[0]) + str(tuple[1] + 1))
        if list:
            return new_set
        return ", ".join(new_set)
    def get_letter(piece):
        if piece.__class__ == Pawn:
            return ""
        return piece.fen_chr.upper()
    def color_turn(moves):
        if moves % 2 == 0:
            return "white"
        return "black"
    def is_chess_notation(cmd):
        """checks if the command is in proper chess_notation"""
        if re.search(r"^\s*[KQRBN]?[a-h1-8]?x?[a-h][1-8][+#]?\s*$", cmd):
            return True
        elif cmd == "0-0-0" or cmd == "0-0":
            return True
        return False
    def op_color(color):
        if color == "white":
            return "black"
        return "white"
    def color_direction(color):
        if color == "white":
            return 1
        return -1
    def get_piece_from_square(square, board):
        if len(square) == 2:
            if square[1:2].isnumeric():
                if square[0:1] in Board.letters and int(square[1:2]) in list(range(1, 9)):
                    x, y = UI.convert_letter(square[0:1]), UI.convert_letter(square[1:2])
                    return board[y][x]["piece"]
    def is_command(move):
        return move in ["turn board", "piece moves", "stop", "en passent"]
class Random():
    """holds all functions for game mode random"""
    def generate_random_move(color, board):
        player_pieces = board.white_pieces
        if color == "black":
            player_pieces = board.black_pieces
        player_pieces = list(player_pieces)
        for p in player_pieces:
            print(p, sep="", end="")
        while True:
            random_int = random.randint(0, len(player_pieces) - 1)
            piece = player_pieces[random_int]
            moves, error = GameRules.legal_moves(piece)
            if moves:
                moves = UI.convert_coordinates(moves, letter=UI.get_letter(piece), list=True)
                print("|", piece, piece.pos(), moves)
                print(len(player_pieces))

                return random.choice(list(moves))
            del player_pieces[random_int]
    def get_piece(pieces):
        return random.choice(pieces)
    

"add castle notation to king and rook piece. when random promotes, default to queen"

"""
TO DO
instructions
initial program
make checker for if the rook and king moved for fen converter
"""
"""
export GEMINI_API_KEY="AIzaSyCHf1XUIY983O4geC2HIBugdlgkjNMgNPw"
"""